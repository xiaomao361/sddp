# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from django import forms
from sentry.plugins.bases.notify import NotificationPlugin
import sddp

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class AccessTokenForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='钉钉机器人access_token'
    )


class DingTalkPlugin(NotificationPlugin):
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

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            self.logger.info('dingtalk token config error')
            return None

        if self.should_notify(group, event):
            self.logger.info('send msg to dingtalk yes')
            self.send_msg(group, event, *args, **kwargs)
        else:
            self.logger.info('send msg to dingtalk no')
            return None

    def send_msg(self, group, event, *args, **kwargs):
        del args, kwargs

        error_title = u'项目【%s】报错' % event.project.slug

        data = {
            "msgtype": 'markdown',
            "markdown": {
                "title": error_title,
                "text": u'#### {title} \n\n > {message} \n\n [点击查看问题]({url})'.format(
                    title=error_title,
                    message=event.message,
                    url=u'{url}events/{id}/'.format(
                        url=group.get_absolute_url(),
                        id=event.event_id if hasattr(event, 'event_id') else event.id
                    ),
                )
            }
        }

        requests.post(
            url=DingTalk_API.format(token=self.get_option('access_token', group.project)),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(data).encode('utf-8')
        )
