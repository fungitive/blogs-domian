# blogs/hosts.py

"""
创建一个包含默认主机模式的新模块的hosts.py文件中。
"""
from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',  # 配置模式的正则表达式，如果要使用https，在需要的host中增加 scheme='https://' 属性（第7步）
    host(r'www', settings.ROOT_URLCONF, name='www'),  # http://www.domain.cn/ 直接请求主urls中配置的路由
    host(r'api', 'api.urls', name='api'),   # http://api.mydomain.cn/
    host(r'blog', 'blog.urls', name='blog'),  # http://blog.mydomain.cn/
)