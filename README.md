<!DOCTYPE html>
<html>
<head>
	<title>RENADME</title>
</head>
<body>
<div id="cnblogs_post_body" class="blogpost-body"><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; redis是当前比较热门的NOSQL系统之一，它是一个key-value存储系统。和Memcached类似，但很大程度补偿了memcached的不足，它支持存储的value类型相对更多，包括string、list、set、zset和hash。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作。在此基础上，redis支持各种不同方式的排序。Redis数据都是缓存在计算机内存中，并且会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redis官网地址：<a href="http://www.redis.io/">http://www.redis.io/</a></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 最新版本：2.8.3</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 在Linux下安装Redis非常简单，具体步骤如下（官网有说明）：</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 1、下载源码，解压缩后编译源码。</p>
<div class="cnblogs_code">
<pre>$ wget http:<span style="color: #008000;">//</span><span style="color: #008000;">download.redis.io/releases/redis-2.8.3.tar.gz</span>
$ tar xzf redis-<span style="color: #800080;">2.8</span>.<span style="color: #800080;">3</span><span style="color: #000000;">.tar.gz
$ cd redis</span>-<span style="color: #800080;">2.8</span>.<span style="color: #800080;">3</span><span style="color: #000000;">
$ make</span></pre>
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 2、编译完成后，在Src目录下，有四个可执行文件redis-server、redis-benchmark、redis-cli和redis.conf。然后拷贝到一个目录下。</p>
<div class="cnblogs_code">
<pre>mkdir /usr/<span style="color: #000000;">redis
cp redis</span>-server  /usr/<span style="color: #000000;">redis
cp redis</span>-benchmark /usr/<span style="color: #000000;">redis
cp redis</span>-cli  /usr/<span style="color: #000000;">redis
cp redis.conf  </span>/usr/<span style="color: #000000;">redis
cd </span>/usr/redis</pre>
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp; 3、启动Redis服务。</p>
<div class="cnblogs_code">
<pre>$ redis-server   redis.conf</pre>
</div>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4、然后用客户端测试一下是否启动成功。</p>
<div class="cnblogs_code">
<pre>$ redis-<span style="color: #000000;">cli
redis</span>&gt; <span style="color: #0000ff;">set</span><span style="color: #000000;"> foo bar
OK
redis</span>&gt; <span style="color: #0000ff;">get</span><span style="color: #000000;"> foo
</span><span style="color: #800000;">"</span><span style="color: #800000;">bar</span><span style="color: #800000;">"</span></pre>
</div>
<p><br>&nbsp;</p></div>
</body>
</html>
