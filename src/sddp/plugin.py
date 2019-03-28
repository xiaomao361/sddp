# -*- coding: utf-8 -*-

import requests
from django import forms
from sentry.plugins.bases.notify import NotifyPlugin
import sddp
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class AccessTokenForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='钉钉机器人access_token'
    )


class DingTalkPlugin(NotifyPlugin):
    author = 'zhouwei'
    author_url = 'https://github.com/xiaomao361/sddp'
    version = sddp.VERSION
    description = "错误消息发送到钉钉的插件"
    resource_links = [
        ('Bug Tracker', 'https://github.com/xiaomao361/sddp/issues'),
        ('Source', 'https://github.com/xiaomao361/sddp'),
    ]
    slug = 'dingtalk'
    title = 'dingtalk'
    conf_key = slug
    conf_title = title
    project_conf_form = AccessTokenForm

    def is_configured(self, project):
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, fail_silently=False):
        access_token = self.get_option('access_token', group.project)
        send_url = DingTalk_API.format(token=access_token)
        title = "项目{}报错".format(event.project.name)
        message = event.message
        event_url = "{0}events/{1}/".format(group.get_absolute_url(), event.id)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": "#### {title} \n > {message} \n [点击查看问题]({event_url})".format(
                    title=title,
                    message=message,
                    event_url=event_url,
                ),
            },
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
