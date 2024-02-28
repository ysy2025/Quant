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