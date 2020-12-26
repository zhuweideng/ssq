import numpy as np
import time
from ssq_data import *



def new_run():

    ssqdata=get_exl_data_by_period(random_order=False,use_resnet=True,times=10)

    print("sss")
    # print(ssqdata)
    ticks = time.time();
    result2txt = str(ssqdata)  # data是前面运行出的数据，先将其转为字符串才能写入

    with open(str(ticks)+'结果存放.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        # file_handle.write()


        file_handle.write("{}/n".format(result2txt))  # 此时不需在第2行中的转为字符串
    # np.savetxt('new.txt',ssqdata);





new_run()