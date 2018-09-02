### 文件说明：
* main.py : 程序入口，进行初步筛选代理
* config.py : 保存所有的配置，包含代理文件保存地址，进行筛选的代理个数，requests请求的参数等等。
* IPScreener.py : 用GET的请求对代理进行初步筛选
* IPCollecter.py : 用爬虫爬取github上的代理资源，保存到本地
* IPHelper.py : 用于对初步筛选后的IP进行管理，IPHelper中的方法用于进一步筛选

### 代理来源、第三方库：
* 代理来源：[github开源的代理](https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list)
* 第三方库： requests大法好

### 使用方法：
* 设置好config,直接运行main.py即可。获得为经过初步筛选的代理

### 代理筛选过程：
1. 从代理源获取所有的代理
2. 初步筛选：用一定数量的代理向网站发送GET请求，挑选出请求成功的代理
3. 多次筛选：初步筛选的代理运用到实际项目中，由于开源的代理不稳定，用python的try-except来使用代理。即try用代理a发送请求，如果代理a挂掉，执行except来换代理b,这样可以避免程序运行到一半报错停止。  
在except中便可以统计代理挂掉的次数，运行结束后打印统计结果。配合IPHelper中的方法来管理useful_ips文件。

### emmmm
* 由于是免费代理，折腾了半天应该能获得一些较为高速的代理。但是用了代理IP也别频繁访问网站，在发送请求时考虑到网站的压力，控制好访问的速度~~~