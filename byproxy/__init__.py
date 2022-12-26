"""
# ByProxy

ByProxy is a simple package contains simple tools for proxy management and usage. You can generate proxy dictionaries from a list of urls and gain information about the proxies.

"""
from byproxy.proxy_maker import ProxyMaker
from byproxy.proxy_checker import ProxyChecker

__version__ = '0.1.0'
__author__ = 'vimevim <vimevim@gmail.com>'
__all__ = [
    'ProxyMaker',
    'ProxyChecker',
    ]