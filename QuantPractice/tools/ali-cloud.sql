阿里云提供的Python版本单一，如需要其他版本的Python，可按照如下步骤来更换。
https://developer.aliyun.com/article/933318
不要删原有的2.7的，新装一个就行了

centOS下升级python版本，详细步骤
1、在aws云服务器，申请一台小vm机器，自带2.7.6 版本的python，现在我要升级至3.9.13版本
wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz
或：
curl -o https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz

2、下载完成后到下载目录下，解压
tar -xzvf Python-3.9.13.tgz

3、进入解压缩后的文件夹
cd Python-3.9.13　　

4、在编译前先在/usr/local建一个文件夹python3（作为python的安装路径，以免覆盖老的版本）
mkdir /usr/local/python3 （此处新建文件夹用mkdir，如果是新建文件则用touch）

　　
5、开始编译安装（ 笔者安装的是最小centos系统，所以使用编译命令前，必须安装编译套件gcc，
读者如果安装的是界面centos系统，或者使用过编译工具则可跳过安装gcc，直接进行下边的编译步骤）

安装gcc
https://developer.aliyun.com/article/41508?spm=5176.21213303.J_qCOwPWspKEuWcmp8qiZNQ.1.6fd12f3daVbfvG&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@41508._.ID_community@@%E6%96%87%E7%AB%A0@@41508-RL_centos%20%E5%AE%89%E8%A3%85gcc-LOC_llm-OR_ser-V_3-RE_new2-P0_0
https://developer.aliyun.com/article/1072951?spm=5176.21213303.J_qCOwPWspKEuWcmp8qiZNQ.12.6fd12f3daVbfvG&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1072951._.ID_community@@%E6%96%87%E7%AB%A0@@1072951-RL_centos%20%E5%AE%89%E8%A3%85gcc-LOC_llm-OR_ser-V_3-RE_new2-P0_2

./configure --prefix=/usr/local/python3

make

make install

6、此时没有覆盖老版本，再将原来/usr/bin/python链接改为别的名字（笔者保留了两个版本的，
一个python，一个python3，所以第6步笔者略过，把第7步的链接后名字改为python3，读者可按正常步骤，实现的效果相同）
mv /usr/bin/python /usr/bin/python_old2
　　
7、再建立新版本python的链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python
　　
8、这个时候输入
python -V

　
10、就会显示出python的新版本信息

python -V
Python 3.9.13

PS：如果不建立新安装路径python3，而是直接默认安装，则安装后的新python应该会覆盖linux下自带的老版本，也有可能不覆盖，具体看安装过程了，
这个大家可以自己试验下，当然如果还想保留原来的版本，那么这种方法最好不过了。