# 应用的配置信息
from django.apps import AppConfig


class MysiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite_app'
