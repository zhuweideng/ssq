##学习资料

##### 神经网络中Batch Size的理解
https://blog.csdn.net/qq_34886403/article/details/82558399

##### TensorFlow 中 tf.app.flags.FLAGS 的用法介绍
https://blog.csdn.net/rosefun96/article/details/78923140

##### tf.placeholder函数说明
https://blog.csdn.net/kdongyi/article/details/82343712

##### tensorflow GPU 加速
https://blog.csdn.net/weixin_36670529/article/details/87214096


### 强制GPU 加速
```
将 with tf.Session() as sess: 替换为
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.9)
with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options,log_device_placement=True),graph=detection_graph) as sess:
    with tf.device("/gpu:0"):

```
https://www.cnblogs.com/wind-chaser/p/11348564.html

[Ubuntu 20.04安装CUDA 11](https://blog.csdn.net/qq_36999834/article/details/107589779)

[RTX3080+Ubuntu18.04+cuda11.1+cudnn8.0.4+TensorFlow1.15.4+PyTorch1.7.0环境配置](https://blog.csdn.net/qq_35635340/article/details/110138215)