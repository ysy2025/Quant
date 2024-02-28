Please make sure the libxml2 and libxslt development packages are installed.

https://blog.csdn.net/qq_42092076/article/details/130789827
sudo apt-get install libxml2-dev
sudo apt-get install libxslt-dev

https://developer.aliyun.com/article/1439083?spm=a2c6h.14164896.0.0.227547c5aeoyYu&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1439083._.ID_1439083-RL_libxml2%20and%20libxslt-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_0

安装pillow报错,兜兜转转发现是版本问题

https://pillow.readthedocs.io/en/latest/installation.html



其他一些问题记录
https://www.cnblogs.com/treemountain/p/12504582.html


https://www.jianshu.com/p/8f8cc499fee1
Python 脚本运行时Segmentation fault (core dumped)
问题如题描述，python 运行过程中直接导致python 解释器崩溃（不是异常，直接崩溃），下面简叙一下
运行：

ulimit -a
core file size (blocks, -c) 0
data seg size (kbytes, -d) unlimited
scheduling priority (-e) 0
file size (blocks, -f) unlimited
pending signals (-i) 62876
max locked memory (kbytes, -l) 64
max memory size (kbytes, -m) unlimited
open files (-n) 1024
pipe size (512 bytes, -p) 8
POSIX message queues (bytes, -q) 819200
real-time priority (-r) 0
stack size (kbytes, -s) 8192
cpu time (seconds, -t) unlimited
max user processes (-u) 62876
virtual memory (kbytes, -v) unlimited
file locks (-x) unlimited

stack size果然有限制，改成没有限制

ulimit -S -s unlimited
改完以后

stack size (kbytes, -s) unlimited

作者：sexy_cyber
链接：https://www.jianshu.com/p/8f8cc499fee1
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


Python3报错：ModuleNotFoundError: No module named '_bz2'
https://www.cnblogs.com/lemon-le/p/11558971.html

mv _bz2.cpython-36m-x86_64-linux-gnu.so _bz2.cpython-37m-x86_64-linux-gnu.so
cp _bz2.cpython-37m-x86_64-linux-gnu.so /usr/local/python3/lib/python3.7/lib-dynload/

>>> import akshare as ak
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/python3.8/lib/python3.8/site-packages/akshare/__init__.py", line 2685, in <module>
    import pandas as pd
  File "/usr/local/python3.8/lib/python3.8/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev  # pyright: ignore # noqa:F401
  File "/usr/local/python3.8/lib/python3.8/site-packages/pandas/compat/__init__.py", line 24, in <module>
    import pandas.compat.compressors
  File "/usr/local/python3.8/lib/python3.8/site-packages/pandas/compat/compressors.py", line 7, in <module>
    import bz2
  File "/usr/local/python3.8/lib/python3.8/bz2.py", line 19, in <module>
    from _bz2 import BZ2Compressor, BZ2Decompressor
ImportError: libbz2.so.1.0: cannot open shared object file: No such file or directory


1. 安装bzip2-devel
sudo yum install bzip2-devel

2. 缺少bz2的so文件
本机服务器原先安装由python3.6,在python安装目录的lib/python3.6/lib-dynload找到_bz2.cpython-36m-x86_64-linux-gnu.so，将复制到python3.9的lib/python3.6/lib-dynload路径中，并改名为_bz2.cpython-39-x86_64-linux-gnu.so

_bz2.cpython-36m-x86_64-linux-gnu.so文件和_bz2.cpython-39-x86_64-linux-gnu.so可在gitee下载
https://gitee.com/flow-laic/flow-laic.git
https://gitee.com/flow-laic/flow-laic/tree/master/

注意！！！python3.6的文件时36m,但是python3.9是39,不注意改为39m会导致文件不生效，问题无法解决。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/weixin_43876014/article/details/131221937



在centos中运行某些程序会报错如下图所示：

File "/usr/local/lib/python3.6.5/lib/python3.6/bz2.py", line 23, in
from _bz2 import BZ2Compressor, BZ2Decompressor
ModuleNotFoundError: No module named '_bz2'
该错误是缺失_bz2.cpython-36m-x86_64-linux-gnu.so这个os文件，处理步骤如下：

1）下载该文件，放到python3.6文件夹里…/python36/lib/python3.6/lib-dynload/目录下；

使用"chmod +x _bz2.cpython-36m-x86_64-linux-gnu.so"增加该文件的可执行权限

2）再次运行程序可能还会报错：ImportError: libbz2.so.1.0: cannot open shared object file: No such file or directory

1.首先需要使用sudo yum install -y bzip2* 确保系统已经安装了相关的库；

2.此时会发现在/usr/lib64目录下会发现其实有libbz2.so.1.0.6这样一个文件，我们只需要在该目录下使用命令

"sudo ln -s libbz2.so.1.0.6 libbz2.so.1.0"创建一个该文件的软连接。

至此问题得到解决
https://www.cnblogs.com/Afrafre/p/15624055.html

https://blog.csdn.net/suwei825/article/details/121101236




ModuleNotFoundError: No module named 'zlib'
https://blog.csdn.net/gongjianing/article/details/125350255


ImportError: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168
https://blog.csdn.net/weixin_63133658/article/details/134380096

./config --prefix=/usr/local/openssl
1.安装wget

yum install -y wget

2.编译安装 openssl

wget https://www.openssl.org/source/openssl-1.1.1n.tar.gz --no-check-certificate

tar zxf openssl-1.1.1n.tar.gz -C 指定目录

cd openssl-1.1.1n/

./config --prefix=/usr/local/openssl 设置安装目录 可以自定义 但是要记住，后面会用到

make -j && make install 编译并安装

/usr/local/openssl/lib 路径添加到系统动态库查找路径中，在 etc 目录下的 profile文件最后面添加下面这一行

export LD_LIBRARY_PATH=/usr/local/openssl/lib:$LD_LIBRARY_PATH
 source /etc/profile        使其生效
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/weixin_63133658/article/details/134380096


太感动了.总算安装好了
