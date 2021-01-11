import time

def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    # window默认编码gbk，所以我们需要转成utf-8,linux无视
    with open('log.ssq.txt', 'a+', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)