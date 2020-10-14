# 利用神经网络和LSTM预测双色球(How To predict the China's Union Lotto with Neural Network and LSTM)

## 2019/6/18更新
利用最近几次的双色球结果和奖池情况做预测，训练和测试见`ssq4all_v4.py`和`ssq4all_test_v4.py`。
## 2018/9/16更新
添加了大乐透的训练测试文件。
## 2018/5/30更新
根据反馈，修复了一些错误，删除了两个文件。另外，有问题请直接开issue。
## 2018/3/29更新
尝试用CNN和LSTM做预测。CNN用于提取特征，采用的是resnet。目前最好的结果是五等奖（中4个红号）。
## 背景(Background)
------
这个项目是通过结合神经网络和Long Short-Term Memory(LSTM)完成双色球预测。关于双色球的介绍，在此处不在赘述（参见[网站](https://baike.baidu.com/item/中国福利彩票双色球/8676030?fr=aladdin&fromid=75279&fromtitle=%E5%8F%8C%E8%89%B2%E7%90%83)）。该项目以真实的双色球开奖结果作为输入（7个数值，其中前6个表示红号，最后一个表示蓝号），输出预测结果（输出仍为7个数值，其中前6个表示红号，最后一个表示蓝号）。目前该项目还处于开发中。<br><br>
其中，项目核心代码主要借鉴了这个[网站](https://github.com/jinfagang/tensorflow_poems) 。
截至目前，该项目充分训练后的预测结果中，正确预测的红号数目为0-2个（1个的居多，但鉴于这概率本身就偏高，因此不能算是取得很好的结果），正确预测的蓝号数目为0-1个（0个的居多），考虑到双色球的中奖条件（至少3红号正确或者至少蓝号正确），**不建议各位直接根据预测结果去买**。<br>
预测结果不好有以下几个原因：
1. 双色球本身是一个随机事件，而我却希望从中找到规律；
2. 数据集样本数量不够多且无法有效扩大数据集；
3. 可能我的模型还不够优秀。

如果您有什么好的建议或者有什么问题，请直接发我邮箱（yc_liang@qq.com）或者在issue留言也可以；<br>
如果您觉得这项目似乎还有点意思，记得STAR；<br>
当然，如果您真的中奖了，要求不高, STAR。<br>

## 项目依赖(Requirement)
-----

1.Tensorflow;<br>
2.pyexcel_xls;<br>
3.CUDA.(optional)<br>
该项目的代码可能还需要一些python包但我没列出来，请自行pip一下。<br><br>

-----
pip3 install tensorflow==1.15.4
pip3 install opencv-python
pip3 install pyexcel_xls
pip3 install tensorflow
pip3 install tensorflow
## 项目文件(File contents)
-----

1.` poems` : ` poems`文件夹包含3个模型文件，其中`model.py`是本项目所使用的模型文件;其中`resnet.py`定义的是resnet模型;<br>
2.`ssq.py `: 该文件用于训练双色球模型;<br>
3.`ssq.xls` : 该文件储存了历次双色球的开奖和中奖数据，需要利用宏进行数据更新;<br>
4.`ssq_data.py ` : 读取`ssq.xls`文件中的数据并变成所需要的形式.<br>
5.`ssq_test.py`: 以最近一次的双色球开奖结果作为输入，输出模型产生的预测结果;<br>
6.`ssq4all.py `: 该文件用于训练双色球模型（和`ssq.py `功能一样，但用的模型不一样）;<br>
7.`ssq4all_test.py`: 以最近一次的双色球开奖结果作为输入，输出模型产生的预测结果;<br>
6.`dlt.xls` : 该文件储存了历次双色球的开奖和中奖数据，需要利用宏进行数据更新;<br>
7.`dlt4all.py `: 该文件用于训练大乐透模型;<br>
8.`dlt4all_test.py`: 以最近一次的大乐透开奖结果作为输入，输出模型产生的预测结果;<br>

## 训练及测试(How To Use)
-----
设置好参数，运行ssq.py（建议在控制台运行，这样训练到一半可以直接通过按CTRL+C取消训练并保存结果；这样下次训练时可以从上一次的checkpoint继续训练）。训练后，项目目录下会生成一个model文件夹用于保存模型。然后运行ssq_test.py进行预测就可以了。<br>
该项目在W10, tensorflow 1.4/1.5正常运行。有无GPU均可运行。原则上讲，这项目的模型并不大，且数据量也不大，所以可以直接将所有训练数据作为一个batch进行训练，后续如果需要加深模型，可能要降低batch size。
