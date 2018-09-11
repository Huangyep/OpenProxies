# 用来对保存IP的文件进行操作，对IP进行管理
import json

def get_useful_ips(path):
    """获取所有经过筛选的IP"""
    f = open(path, 'r')
    d = json.load(f)
    f.close()
    return d

def delete_ip_by_index(path,index):
    """删除某个代理，剔除失效的代理，也防止同个代理进行频繁的操作"""
    f = open(path,'r')
    d = json.load(f)
    f.close()
    info = d[index]
    d.pop(index)
    new_d = json.dumps(d)
    f = open(path,'w')
    f.write(new_d)
    f.close()
    print(info,"remove succeed")

def add_ip(path,ip):
    """写入单个代理"""
    f = open(path, 'r')
    d = json.load(f)
    f.close()
    d.append(ip)
    new_d = json.dumps(d)
    f = open(path, 'w')
    f.write(new_d)
    f.close()
    print(ip, "write succeed")

def search_index(path,ip):
    """搜索代理在path文件中的index"""
    ips = get_useful_ips(path)
    for i in range(len(ips)):
        if ips[i]['http'] == ip['http'] and ips[i]['https'] == ip['https']:
            return i
