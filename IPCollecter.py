import requests
import re,json,os,random
import config


def save_ips(isCover=False):
    """保存所有代理IP的数据"""
    url = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"# github上的开源IP
    r = requests.get(url)
    wb = r.text

    # 处理数据
    proxies = []
    pattern = re.compile(r'{.*?}')
    data = pattern.findall(wb, re.S)
    for d in data:
        dict_obj = json.loads(d)
        if dict_obj["anonymity"] == "high_anonymous":  # 这里只保存了高匿代理
            temp = {}
            temp["type"] = dict_obj["type"]
            temp["host"] = dict_obj["host"]
            temp["port"] = dict_obj["port"]
            proxies.append(temp)

    # 把代理IP保存下来，不要频繁访问该网站
    path = config.PATH + config.SAVE_NAME
    if isCover == False: # 防止覆盖原有的文件
        if os.path.exists(path):
            print(path,"文件已存在，注意防止覆盖无关文件")
            return
    try:
        # 如果config.SAVE_PATH路径不存在，自动创建
        if os.path.exists(config.PATH) == False:
            try:
                os.makedirs(config.PATH)
                print(config.PATH,"build succeed")
            except:
                print(config.PATH, "build error")
        f = open(path, "w")
        f.write(json.dumps(proxies)) # 以json格式保存数据，方便解析
        f.close()
        print(path,'save succeed')
    except Exception as e:
        raise e


def get_ips(total=1):
    """读取已经保存的IP，随机抽出total数量的IP"""
    path = config.PATH + config.SAVE_NAME
    if os.path.exists(path) == False:
        print(path,"文件不存在")
        return
    f = open(path,'r')
    data = json.load(f)
    f.close()
    http_list = []
    https_list = []
    for i in range(len(data)):
        if data[i]['type'] == 'http':
            http_list.append('http://' + data[i]['host'] + ':' + str(data[i]['port']))
        if data[i]['type'] == 'https':
            https_list.append('https://' + data[i]['host'] + ':' + str(data[i]['port']))
    proxies = []
    for j in range(total):
        http = random.choice(http_list)
        https = random.choice(https_list)
        proxy = {'http':http,'https':https}  # 返回的每一个代理
        proxies.append(proxy)
    return proxies