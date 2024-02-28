名称
地域
创建时间
公网IP
iZ0jlhdmqu2usznfqs6lnvZ
华北6（乌兰察布）
2024年2月27日 12:41:00
39.101.76.35
USTC!


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
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python3


ln -s /usr/bin/python2 /usr/bin/python_old


mv /usr/bin/python /usr/bin/python_old2
　　
7、再建立新版本python的链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python

ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip

　
8、这个时候输入
python -V

注意配置环境变量
https://www.jianshu.com/p/6ec123426787
　
10、就会显示出python的新版本信息

python -V
Python 3.9.13

PS：如果不建立新安装路径python3，而是直接默认安装，则安装后的新python应该会覆盖linux下自带的老版本，也有可能不覆盖，具体看安装过程了，
这个大家可以自己试验下，当然如果还想保留原来的版本，那么这种方法最好不过了。


# 安装mysql8
https://developer.aliyun.com/article/1251149?spm=a2c6h.14164896.0.0.4b9147c5KHOorU&scm=20140722.S_community@@%E6%96%87%E7%AB%A0@@1251149._.ID_1251149-RL_%E9%98%BF%E9%87%8C%E4%BA%91%20centos%20%E5%AE%89%E8%A3%85mysql8-LOC_search~UND~community~UND~item-OR_ser-V_3-P0_1

https://developer.aliyun.com/article/913045?spm=5176.26934562.main.1.53616ae9reARYy
https://www.jb51.net/article/190714.htm

wget http://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm

The GPG keys listed for the “MySQL 8.0 Community Server“ repository are already installed but they a

解决方案
需要禁掉GPG验证检查

ls /etc/yum.repos.d/mysql-*

所以

[root@h1 ~]# rpm -ivh http://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
2.安装mysql

[root@localhost ~]# yum install -y mysql-server
或
[root@localhost ~]# yum install mysql-community-server
如果显示以下内容说明安装成功　　

Complete!
3.设置mysql

设置开机启动Mysql

[root@localhost ~]# systemctl enable mysqld.service
检查是否已经安装了开机自启动

[root@localhost ~]# systemctl list-unit-files | grep mysqld
如果显示以下内容说明已经完成自动启动安装

mysqld.service enabled
设置开启服务

[root@localhost ~]# systemctl start mysqld.service
这里需要稍微注释下：mysql8.0版本和以前版本的修改密码方式不一样　　　　　　　　　　　　　　　

4.登录修改mysql密码

查看mysql默认密码

[root@localhost ~]# grep 'temporary password' /var/log/mysqld.log
第一次登录mysql，输入账号和默认密码

[root@localhost ~]# mysql -uroot -p
修改当前密码

#MySQL8.0修改密码需要有大小写字母、数字、特殊字符组合
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Alicloud123456!';
5. 命令立即执行
mysql>flush privileges;

解决方案，登录MySQL，修改user表登录用户的host　　　　

#远程设置
mysql> use mysql;
mysql> update user set host='%' where user='root';
#授权用户名的权限，赋予任何主机访问数据的权限
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;


mysql登录用户密码设置好后,需要开发安全组端口，并且好像上面的不是mysql8.0版本，因为8.0版本的加密方式改变了，mysql8以后的加密规则为caching_sha2_password，所以我们需要将mysql用户登录的加密规则修改为mysql_native_password，且需要关闭防火墙的说，然后安全端口设置一个(注意，由于之前改了user，这里@"%")

mysql> ALTER USER 'root'@'%' IDENTIFIED BY 'Root!!2018' PASSWORD EXPIRE NEVER;
Query OK, 0 rows affected (0.03 sec)

mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'Root!!2018';
Query OK, 0 rows affected (0.01 sec)
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.00 sec)



rpm -e --nodeps mariadb-libs-5.5.68-1.el7.x86_64







https://www.jb51.net/article/102928.htm
1、yum方式安装的MySQL

$ yum remove mysql mysql-server mysql-libs compat-mysql51
$ rm -rf /var/lib/mysq
$ rm /etc/my.cnf
查看是否还有mysql软件：

$ rpm -qa|grep mysql
如果存在的话，继续删除即可，删除方式：yum remove + 【名字】。
2、rpm方式安装的mysql
a）查看系统中是否以rpm包安装的mysql：

[root@localhost opt]# rpm -qa | grep -i mysql
MySQL-server-5.6.17-1.el6.i686
MySQL-client-5.6.17-1.el6.i686
b)卸载mysql

[root@localhost local]# rpm -e MySQL-server-5.6.17-1.el6.i686
[root@localhost local]# rpm -e MySQL-client-5.6.17-1.el6.i686
rpm -e --nodeps mysql-community-client-plugins-8.0.36-1.el7.x86_64
rpm -e --nodeps mysql-community-icu-data-files-8.0.36-1.el7.x86_64
rpm -e --nodeps mysql-community-common-8.0.36-1.el7.x86_64
rpm -e --nodeps mysql-community-libs-8.0.36-1.el7.x86_64
rpm -e --nodeps mysql-community-server-8.0.36-1.el7.x86_64
rpm -e --nodeps mysql80-community-release-el7-3.noarch
rpm -e --nodeps mysql-community-client-8.0.36-1.el7.x86_64

c)删除mysql服务

[root@localhost local]# chkconfig --list | grep -i mysql
[root@localhost local]# chkconfig --del mysql
d)删除分散mysql文件夹

[root@localhost local]# whereis mysql #或者
find / -name mysql

mysql: /usr/lib/mysql /usr/share/mysql
清空相关mysql的所有目录以及文件

rm -rf /usr/lib/mysql
rm -rf /usr/share/mysql
rm -rf /usr/my.cnf
通过以上几步，mysql应该已经完全卸载干净了。













您好，如果您的ECS实例中的/var/log/mysqld.log文件被删除了，可以通过以下步骤进行恢复：

登录ECS实例，执行以下命令，获取并安装MySQL源安装包。
 wget 依次执行以下命令，配置安装是5.6版本MySQL的Yum源。

 yum -y install yum-utils
yum-config-manager --disable mysql80-community
yum-config-manager --enable mysql56-community
执行以下命令，安装MySQL Server。
 yum -y install mysql-community-server
编辑 /etc/my.cnf 文件，将文件内容替换成如下所示。
 [mysqld]
innodb_checksum_algorithm=crc32
innodb_data_file_path=ibdata1:200M:autoextend
innodb_log_files_in_group=2
innodb_log_file_size=524288000
innodb_undo_directory=/var/lib/mysql/
basedir=/usr datadir=/var/lib/mysql
innodb_undo_tablespaces=0
server-id=55555
log_bin=mysql-log
gtid_mode=on
enforce_gtid_consistency=on
log-slave-updates=1
relay_log=relay-log
sql_mode=''

binlog_format=row
skip-grant-tables=1
依次执行以下命令，配置Yum源。
 yum -y install 依次执行以下命令，查看并选择需要安装的软件。

 yum list | grep percona
yum -y install percona-xtrabackup.x86_64
执行以下命令，备份MySQL数据。
 mysqldump -u root -p --all-databases > /tmp/mysql-backup.sql
执行以下命令，删除MySQL数据。
 rm -rf /var/lib/mysql/*
执行以下命令，恢复MySQL数据。
 mysql -u root -p --batch --skip-column-names < /tmp/mysql-backup.sql
执行以下命令，重启MySQL服务。
systemctl restart mysqld
执行以下命令，检查MySQL服务状态。
systemctl status mysqld
执行以下命令，确认MySQL服务已经启动成功。
systemctl status mysqld
1。












原因： 链接数据库忘记用户密码， 配置文件/etc/my.cnf中增加skip-grant-table 跳过密码登录，进入服务器修改密码时，出现如下报错信息：

mysql> alter user root@'localhost' identified by '123';
ERROR 1290 (HY000): The MySQL server is running with the --skip-grant-tables option so it cannot execute this statement
解决方法：

1、重启数据库服务器

     ]# service mysql restart

2、链接数据库服务器

     ]# mysql

     mysql>  flush privileges;             刷新权限列表

     mysql> alter user root@'localhost' identified by '123';     更改用户密码
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/weixin_70661795/article/details/131663215

连接MySQL时报错：Public Key Retrieval is not allowed的解决方法
https://www.jianshu.com/p/928eb43d0073













https://www.cnblogs.com/wushujun/p/11691027.html

python模块安装问题：no matching distribution found for XXX 或者 Read timed out.
https://blog.csdn.net/zhang_han666/article/details/88286010





看了很多解决问题的博客，亲测通过更换国内安装源和设置超时时间可以解决。
在pip install XXX命令的后面加上
--default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple即可。



pip install robotframework-httplibrary   --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple