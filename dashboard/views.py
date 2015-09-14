# -*- coding:utf-8 -*-


import json

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from kazoo.client import KazooClient


def home(request):
    """
        url: /
    """
    product_name = request.REQUEST.get("product_name", "online_medweb")

    zk = KazooClient(hosts=settings.ZK_HOSTS)
    zk.start()
    try:

        products = zk.get_children("/zk/product")

        try:
            idx = products.index(product_name)
        except:
            idx = 0

        product_path = "/zk/product/%s/services" % (products[idx], )
        services = zk.get_children(product_path)

        services.sort()

        services_info = []
        for service in services:
            service_path = "%s/%s" % (product_path, service, )
            nodes = zk.get_children(service_path)

            nodes.sort()

            service_info = {
                "service_name": service,
                "path": service_path,
                "nodes": []
            }
            for node in nodes:
                node_path = "%s/%s" % (service_path, node, )
                data, stat = zk.get(node_path) # 期待的信息: 包含什么时候Load, 服务的路径，机器信息
                node_info = json.loads(data)
                node_info["node_path"] = node_path
                service_info["nodes"].append(node_info)
                url, version = parse_code_version(node_info.get("code_url_version", None))
                node_info["version"] = version
                node_info["url"] = url

            services_info.append(service_info)

        context = {
            "product": products[idx],
            "products": products,
            "idx": idx,
            "services_info": services_info,
        }
        template_name = "index.html"
        return render_to_response(template_name, context, context_instance=RequestContext(request))

    finally:
        zk.stop()

def parse_code_version(url):
    # git@git.chunyu.me:server/medweb.git
    # https://git.chunyu.me/server/medweb.git
    # git@git.chunyu.me:python/chunyu_typo.git@936d577
    # https://git.chunyu.me/python/chunyu_typo/commit/936d577
    if not url:
        return None, None

    if url.startswith("http"):
        # https://git.chunyu.me/server/medweb.git@936d577
        # ---> https://git.chunyu.me/server/medweb/commit/936d577
        fields = url.split("@")
        path = fields[0].strip()[:-4]
        version = fields[1].strip()
        url = "%s/commit/%s" % (path, version)

        return url, version
    else:
        # git@git.chunyu.me:server/medweb.git@a211a715
        # ---> git.chunyu.me/python/chunyu_typo.git
        fields = url.split("@")
        path = fields[1].strip()
        path = path.replace(":", "/")[:-4]

        version = fields[2].strip()
        url = "https://%s/commit/%s" % (path, version)
        return url, version