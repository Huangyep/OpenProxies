
### 保存所有IP
PATH = "myFile/"    # 所有代理和经过筛选的代理IP的保存路径
SAVE_NAME = "all_ips.txt"   # 保存所有代理IP的文件名

### 筛选IP
NAME = "useful_ips.txt" # 保存经过筛选的IP的文件名

# 用多进程进行筛选
POOL = 4    # 进程的个数
EACH_POOL_TOTAL = 10  # 每个进程中取EACH_POOL个IP进行筛选
TOTAL = 10  # 多进程运行TOTAL个程序
# requests的请求参数
URL = "https://www.baidu.com/"    # 请求的url
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}   # 请求头,有cookie直接写在HEADERS里面
TIMEOUT = 1    # 请求时限，也可以用来筛选更快的IP


