2020-11-30 20:43:51.416256: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-11-30 20:43:51.440481: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 3793045000 Hz
2020-11-30 20:43:51.441184: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55dcf4cc9830 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-11-30 20:43:51.441206: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
2020-11-30 20:43:51.443268: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
2020-11-30 20:43:51.524789: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:983] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-11-30 20:43:51.525225: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55dcf4d51420 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
2020-11-30 20:43:51.525247: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): GeForce RTX 3080, Compute Capability 8.6
2020-11-30 20:43:51.525395: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:983] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2020-11-30 20:43:51.526005: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Found device 0 with properties: 
name: GeForce RTX 3080 major: 8 minor: 6 memoryClockRate(GHz): 1.785
pciBusID: 0000:09:00.0
2020-11-30 20:43:51.526080: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcudart.so.10.0'; dlerror: libcudart.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526124: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcublas.so.10.0'; dlerror: libcublas.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526164: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcufft.so.10.0'; dlerror: libcufft.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526204: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcurand.so.10.0'; dlerror: libcurand.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526242: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcusolver.so.10.0'; dlerror: libcusolver.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526280: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcusparse.so.10.0'; dlerror: libcusparse.so.10.0: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526319: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libcudnn.so.7'; dlerror: libcudnn.so.7: cannot open shared object file: No such file or directory
2020-11-30 20:43:51.526329: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1662] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2020-11-30 20:43:51.526347: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1180] Device interconnect StreamExecutor with strength 1 edge matrix:
2020-11-30 20:43:51.526355: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1186]      0 
2020-11-30 20:43:51.526362: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1199] 0:   N 
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 2063529865334432322
, name: "/device:XLA_CPU:0"
device_type: "XLA_CPU"
memory_limit: 17179869184
locality {
}
incarnation: 8206699023878515142
physical_device_desc: "device: XLA_CPU device"
, name: "/device:XLA_GPU:0"
device_type: "XLA_GPU"
memory_limit: 17179869184
locality {
}
incarnation: 11033687429676096514
physical_device_desc: "device: XLA_GPU device"
]

[nvidia cuda 10 下载](https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal)


tensorflow_gpu 1.15 python 3.5-3.7  cuDNN 7.4  CUDA 10