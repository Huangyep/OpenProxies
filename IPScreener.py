import requests
import config


def my_process(proxies):
    useful_proxies = []
    for proxy in proxies:
        try:
            r = requests.get(url=config.URL,headers=config.HEADERS,proxies=proxy,timeout=config.TIMEOUT)
            useful_proxies.append(proxy)
        except:
            continue
    return useful_proxies


