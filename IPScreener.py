# 手动筛选可用的代理
# 独立运行IPScreener,数据保存在path文件中
# 可设置的属性：path,total,each_pool_total,pool_num_set,timeout
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


