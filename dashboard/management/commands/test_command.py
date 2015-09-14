# -*- coding:utf-8 -*-


# 类名必须为 Command (约定好的)
from medweb_utils.django_ext.multi_target_command import MultiTargetCommand


class Command(MultiTargetCommand):

    def handle_daily_request(self, *args):
        """
            ./MANAGE.sh test_command handle_daily_request hello world
        :param args:
        :return:
        """
        print "My Args: ", args

