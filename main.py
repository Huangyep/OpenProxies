from multiprocessing import Pool
import time,json
import IPCollecter,IPScreener
import config


if __name__ == "__main__":
    s = time.time()
    # 保存所有的IP
    IPCollecter.save_ips(isCover=True)
    # 多进程筛选较快的IP
    data = []
    pool = Pool(config.POOL)
    result = []
    for i in range(config.TOTAL):
        proxies = IPCollecter.get_ips(total=config.EACH_POOL_TOTAL)
        useful_proxies = pool.apply_async(IPScreener.my_process,args=(proxies,))  # 接收多进程return的数据
        result.append(useful_proxies)
    pool.close()
    pool.join()
    # 将较快的最后保存在data数组中，写入文件
    for r in result:
        for proxy in r.get():
            data.append(proxy)
    path = config.PATH + config.NAME
    f = open(path,"w")
    f.write(json.dumps(data))
    f.close()
    print("useful ips save succeed")
    e = time.time()
    print("总时间",e-s)