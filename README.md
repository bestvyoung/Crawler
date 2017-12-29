<!DOCTYPE html>
<html>
<head>
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


<article>
        <h1 class="csdn_top">mongo管理</h1>
        <div class="article_bar clearfix">
            <div class="artical_tag">
                <span class="original">
                原创                </span>
                <span class="time">2015年04月27日 16:19:43</span>
            </div>

            <ul class="article_tags clearfix csdn-tracking-statistics tracking-click" data-mod="popu_377">
                <li class="tit">标签：</li>

<!--          [startarticletags]-->
                                                            <li><a href="http://so.csdn.net/so/search/s.do?q=mongodb&amp;t=blog" target="_blank">mongodb</a> <span style="display: none;">/</span></li>
                                    <!--          [endarticletags]-->
            </ul>
            <ul class="right_bar">
                <li><button class="btn-noborder"><i class="icon iconfont icon-read"></i><span class="txt">7525</span></button></li>
                <li class="edit" style="display: none;">
                    <a class="btn-noborder" href="http://write.blog.csdn.net/postedit/45312079">
                        <i class="icon iconfont icon-bianji"></i><span class="txt">编辑</span>
                    </a>
                </li>
                <li class="del" style="display: none;">
                    <a class="btn-noborder" onclick="javascript:deleteArticle(fileName);return false;">
                        <i class="icon iconfont icon-shanchu"></i><span class="txt">删除</span>
                    </a>
                </li>
            </ul>
        </div>
        <div id="article_content" class="article_content csdn-tracking-statistics tracking-click" data-mod="popu_519" data-dsm="post" style="overflow: hidden;">
                            <div class="markdown_views">
                        <h1 id="mongo管理"><a name="t0"></a>mongo管理</h1>

<p>基于mongo3.0，和2.x的版本有些地方会不大一样。</p>

<h2 id="安装"><a name="t1"></a>安装</h2>



<h3 id="源安装ubuntu"><a name="t2"></a>源安装(ubuntu)</h3>



<pre class="prettyprint"><code class="hljs lasso has-numbering">echo <span class="hljs-string">"deb http://repo.mongodb.org/apt/ubuntu "</span>$(lsb_release <span class="hljs-attribute">-sc</span>)<span class="hljs-string">"/mongodb-org/3.0 multiverse"</span> <span class="hljs-subst">|</span> sudo tee /etc/apt/sources<span class="hljs-built_in">.</span><span class="hljs-built_in">list</span><span class="hljs-built_in">.</span>d/mongodb<span class="hljs-attribute">-org</span><span class="hljs-subst">-</span><span class="hljs-number">3.0</span><span class="hljs-built_in">.</span><span class="hljs-built_in">list</span>

apt<span class="hljs-attribute">-key</span> adv <span class="hljs-subst">--</span>keyserver keyserver<span class="hljs-built_in">.</span>ubuntu<span class="hljs-built_in">.</span>com <span class="hljs-subst">--</span>recv <span class="hljs-number">7</span>F0CEB10

apt<span class="hljs-attribute">-get</span> update

apt<span class="hljs-attribute">-get</span> install <span class="hljs-attribute">-y</span> mongodb<span class="hljs-attribute">-org</span></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>



<h3 id="mac下登陆mongo"><a name="t3"></a>mac下登陆mongo</h3>

<p>mac 下面默认环境变量会导致登陆不上，报如下错误:</p>

<p>root@iZ28ywqw7nhZ:~# mongo <br>
Failed global initialization: BadValue Invalid or no user locale set. Please ensure LANG and/or LC_* environment variables are set correctly.</p>

<p>设置下环境变量就好了:</p>



<pre class="prettyprint"><code class="hljs bash has-numbering"><span class="hljs-keyword">export</span> LC_ALL=C
mongo </code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>



<h2 id="启动停止"><a name="t4"></a>启动停止</h2>



<h3 id="启动"><a name="t5"></a>启动</h3>

<p>脚本的方法:</p>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">/etc/init<span class="hljs-preprocessor">.d</span>/mongod start
/etc/init<span class="hljs-preprocessor">.d</span>/mongod stop</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>

<p>命令行:</p>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">从配置文件启动:
nohup mongod -f /etc/mongod<span class="hljs-preprocessor">.conf</span> &amp;
停止:
mongo
    use admin
    db<span class="hljs-preprocessor">.shutdownServer</span>()</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li></ul></pre>



<h3 id="停止"><a name="t6"></a>停止</h3>

<p>脚本:</p>

<p>service mongod stop</p>

<p>命令行:</p>

<p>use admin <br>
db.shutdownServer()</p>

<p>如果以上都无效的话用</p>

<p>killall -15 mongod</p>

<p>注意不用用kill -9 ,-9会导致数据库损坏。</p>



<h2 id="mongodb修复"><a name="t7"></a>mongodb修复</h2>

<p>很简单，启动时加上–repair参数 <br>
mongod –dbpath /data/db –repair <br>
非正常重启或者kill -9 均可导致mongodb数据库损坏。</p>



<h2 id="php和python驱动的安装"><a name="t8"></a>php和python驱动的安装</h2>



<h3 id="安装php驱动"><a name="t9"></a>安装php驱动</h3>



<pre class="prettyprint"><code class="hljs cmake has-numbering">pecl <span class="hljs-keyword">install</span> mongo</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>



<h3 id="安装python驱动"><a name="t10"></a>安装python驱动</h3>



<pre class="prettyprint"><code class="hljs coffeescript has-numbering">
apt-get install python-pip

pip install pymongo

root<span class="hljs-property">@iZ28ywqw7nhZ</span>:~<span class="hljs-comment"># python</span>
Python <span class="hljs-number">2.7</span><span class="hljs-number">.3</span> (<span class="hljs-reserved">default</span>, Dec <span class="hljs-number">18</span> <span class="hljs-number">2014</span>, <span class="hljs-number">19</span>:<span class="hljs-number">10</span>:<span class="hljs-number">20</span>)
[GCC <span class="hljs-number">4.6</span><span class="hljs-number">.3</span>] <span class="hljs-literal">on</span> linux2
Type <span class="hljs-string">"help"</span>, <span class="hljs-string">"copyright"</span>, <span class="hljs-string">"credits"</span> <span class="hljs-keyword">or</span> <span class="hljs-string">"license"</span> <span class="hljs-keyword">for</span> more information.
<span class="hljs-reserved">import</span> pymongo
能正确<span class="hljs-reserved">import</span> 就说明pymongo已经安装成功
</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>



<h2 id="mongo索引"><a name="t11"></a>mongo索引</h2>

<p>mongo索引和其他数据库类似的，数据结构上面用的是b树。</p>



<h3 id="创建索引ensureinde"><a name="t12"></a>创建索引ensureInde</h3>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">db<span class="hljs-preprocessor">.inventory</span><span class="hljs-preprocessor">.ensureIndex</span>({<span class="hljs-string">"item"</span>:<span class="hljs-number">1</span>})
{
    <span class="hljs-string">"createdCollectionAutomatically"</span> : false,
    <span class="hljs-string">"numIndexesBefore"</span> : <span class="hljs-number">1</span>,
    <span class="hljs-string">"numIndexesAfter"</span> : <span class="hljs-number">2</span>,
    <span class="hljs-string">"ok"</span> : <span class="hljs-number">1</span>
}</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>



<h3 id="查看索引"><a name="t13"></a>查看索引</h3>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">db<span class="hljs-preprocessor">.inventory</span><span class="hljs-preprocessor">.getIndexes</span>()
[
    {
        <span class="hljs-string">"v"</span> : <span class="hljs-number">1</span>,
        <span class="hljs-string">"key"</span> : {
            <span class="hljs-string">"_id"</span> : <span class="hljs-number">1</span>
        },
        <span class="hljs-string">"name"</span> : <span class="hljs-string">"_id_"</span>,
        <span class="hljs-string">"ns"</span> : <span class="hljs-string">"test.inventory"</span>
    },
    {
        <span class="hljs-string">"v"</span> : <span class="hljs-number">1</span>,
        <span class="hljs-string">"key"</span> : {
            <span class="hljs-string">"item"</span> : <span class="hljs-number">1</span>
        },
        <span class="hljs-string">"name"</span> : <span class="hljs-string">"item_1"</span>,
        <span class="hljs-string">"ns"</span> : <span class="hljs-string">"test.inventory"</span>
    }
]</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li></ul></pre>



<h3 id="删除索引"><a name="t14"></a>删除索引</h3>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">db<span class="hljs-preprocessor">.inventory</span><span class="hljs-preprocessor">.dropIndex</span>({<span class="hljs-string">"item"</span>:<span class="hljs-number">1</span>})
{ <span class="hljs-string">"nIndexesWas"</span> : <span class="hljs-number">2</span>, <span class="hljs-string">"ok"</span> : <span class="hljs-number">1</span> }</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li></ul></pre>



<h3 id="唯一索引"><a name="t15"></a>唯一索引</h3>



<pre class="prettyprint"><code class="hljs bash has-numbering">db.test.ensureIndex({<span class="hljs-string">"item"</span>:<span class="hljs-number">1</span>},{<span class="hljs-string">"unique"</span>:<span class="hljs-literal">true</span>})
{
    <span class="hljs-string">"createdCollectionAutomatically"</span> : <span class="hljs-literal">true</span>,
    <span class="hljs-string">"numIndexesBefore"</span> : <span class="hljs-number">1</span>,
    <span class="hljs-string">"numIndexesAfter"</span> : <span class="hljs-number">2</span>,
    <span class="hljs-string">"ok"</span> : <span class="hljs-number">1</span>
}</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li></ul></pre>



<h3 id="explain查询执行计划"><a name="t16"></a>explain查询执行计划</h3>



<pre class="prettyprint"><code class="hljs bash has-numbering">db.inventory.find().<span class="hljs-function"><span class="hljs-title">explain</span></span>()
{
    <span class="hljs-string">"queryPlanner"</span> : {
        <span class="hljs-string">"plannerVersion"</span> : <span class="hljs-number">1</span>,
        <span class="hljs-string">"namespace"</span> : <span class="hljs-string">"test.inventory"</span>,
        <span class="hljs-string">"indexFilterSet"</span> : <span class="hljs-literal">false</span>,
        <span class="hljs-string">"parsedQuery"</span> : {
            <span class="hljs-string">"<span class="hljs-variable">$and</span>"</span> : [ ]
        },
        <span class="hljs-string">"winningPlan"</span> : {
            <span class="hljs-string">"stage"</span> : <span class="hljs-string">"COLLSCAN"</span>,
            <span class="hljs-string">"filter"</span> : {
                <span class="hljs-string">"<span class="hljs-variable">$and</span>"</span> : [ ]
            },
            <span class="hljs-string">"direction"</span> : <span class="hljs-string">"forward"</span>
        },
        <span class="hljs-string">"rejectedPlans"</span> : [ ]
    },
    <span class="hljs-string">"serverInfo"</span> : {
        <span class="hljs-string">"host"</span> : <span class="hljs-string">"iZ28ywqw7nhZ"</span>,
        <span class="hljs-string">"port"</span> : <span class="hljs-number">27017</span>,
        <span class="hljs-string">"version"</span> : <span class="hljs-string">"3.0.2"</span>,
        <span class="hljs-string">"gitVersion"</span> : <span class="hljs-string">"6201872043ecbbc0a4cc169b5482dcf385fc464f"</span>
    },
    <span class="hljs-string">"ok"</span> : <span class="hljs-number">1</span>
}
</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li></ul></pre>

<p>stage 是COLLSCAN 说明没有走索引，走索引的话会显示 IXSCAN</p>



<h2 id="mongo备份恢复"><a name="t17"></a>mongo备份恢复</h2>



<h3 id="备份mongodump"><a name="t18"></a>备份mongodump</h3>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">root@iZ28ywqw7nhZ:~/backup<span class="hljs-preprocessor"># mongodump </span>
<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.095</span>+<span class="hljs-number">0800</span>    writing admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.indexes</span> to dump/admin/system<span class="hljs-preprocessor">.indexes</span><span class="hljs-preprocessor">.bson</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.096</span>+<span class="hljs-number">0800</span>    writing admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.users</span> to dump/admin/system<span class="hljs-preprocessor">.users</span><span class="hljs-preprocessor">.bson</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.113</span>+<span class="hljs-number">0800</span>    writing admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.users</span> metadata to dump/admin/system<span class="hljs-preprocessor">.users</span><span class="hljs-preprocessor">.metadata</span><span class="hljs-preprocessor">.json</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.115</span>+<span class="hljs-number">0800</span>    done dumping admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.users</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.115</span>+<span class="hljs-number">0800</span>    writing admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.version</span> to dump/admin/system<span class="hljs-preprocessor">.version</span><span class="hljs-preprocessor">.bson</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.116</span>+<span class="hljs-number">0800</span>    writing admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.version</span> metadata to dump/admin/system<span class="hljs-preprocessor">.version</span><span class="hljs-preprocessor">.metadata</span><span class="hljs-preprocessor">.json</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.117</span>+<span class="hljs-number">0800</span>    done dumping admin<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.version</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.117</span>+<span class="hljs-number">0800</span>    writing test<span class="hljs-preprocessor">.inventory</span> to dump/test/inventory<span class="hljs-preprocessor">.bson</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.118</span>+<span class="hljs-number">0800</span>    writing test<span class="hljs-preprocessor">.inventory</span> metadata to dump/test/inventory<span class="hljs-preprocessor">.metadata</span><span class="hljs-preprocessor">.json</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.119</span>+<span class="hljs-number">0800</span>    done dumping test<span class="hljs-preprocessor">.inventory</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">26</span>T21:<span class="hljs-number">31</span>:<span class="hljs-number">34.119</span>+<span class="hljs-number">0800</span>    writing test<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.indexes</span> to dump/test/system<span class="hljs-preprocessor">.indexes</span><span class="hljs-preprocessor">.bson</span>
</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li></ul></pre>



<h3 id="恢复mongorestore-drop"><a name="t19"></a>恢复mongorestore –drop</h3>



<pre class="prettyprint"><code class="hljs livecodeserver has-numbering">root@iZ28ywqw7nhZ:~/backup<span class="hljs-comment"># mongorestore --drop</span>
<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.391</span>+<span class="hljs-number">0800</span>    <span class="hljs-keyword">using</span> default <span class="hljs-string">'dump'</span> <span class="hljs-built_in">directory</span>

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.394</span>+<span class="hljs-number">0800</span>    building <span class="hljs-operator">a</span> list <span class="hljs-operator">of</span> dbs <span class="hljs-operator">and</span> collections <span class="hljs-built_in">to</span> restore <span class="hljs-built_in">from</span> dump dir

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.397</span>+<span class="hljs-number">0800</span>    reading metadata <span class="hljs-built_in">file</span> <span class="hljs-built_in">from</span> dump/test/inventory.metadata.json

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.397</span>+<span class="hljs-number">0800</span>    restoring test.inventory <span class="hljs-built_in">from</span> <span class="hljs-built_in">file</span> dump/test/inventory.bson

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.398</span>+<span class="hljs-number">0800</span>    restoring indexes <span class="hljs-keyword">for</span> collection test.inventory <span class="hljs-built_in">from</span> metadata

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.398</span>+<span class="hljs-number">0800</span>    finished restoring test.inventory

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.399</span>+<span class="hljs-number">0800</span>    restoring users <span class="hljs-built_in">from</span> dump/admin/<span class="hljs-keyword">system</span>.users.bson

<span class="hljs-number">2015</span>-<span class="hljs-number">04</span>-<span class="hljs-number">27</span>T09:<span class="hljs-number">03</span>:<span class="hljs-number">22.402</span>+<span class="hljs-number">0800</span>    done
</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li></ul></pre>



<h3 id="恢复单库"><a name="t20"></a>恢复单库</h3>

<p>cd ~/testmongobackup</p>

<p>mongorestore -d blog –drop</p>



<h3 id="恢复单集合"><a name="t21"></a>恢复单集合</h3>

<p>cd ~/testmongobackup</p>

<p>mongorestore -d blog -c posts –drop</p>



<h3 id="备份大库"><a name="t22"></a>备份大库</h3>



<h2 id="导入导出"><a name="t23"></a>导入导出</h2>



<h3 id="导入-mongoimport"><a name="t24"></a>导入 mongoimport</h3>

<p>目前支持三种格式</p>

<ul>
<li>CSV</li>
<li>TSV</li>
<li>JSON</li>
</ul>

<p>比如:</p>

<p>$mongoimport -d blog -c tagcloud –type csv –headerline &lt; csvimportfile.csv</p>



<h3 id="导出-mongoexport"><a name="t25"></a>导出 mongoexport</h3>

<p>也是支持3种格式，和import一致。</p>

<p>mongoexport -d blog -c posts -q {} -f _id,Title,Message,Author –csv &gt;blogposts.csv</p>



<h2 id="认证"><a name="t26"></a>认证</h2>



<h3 id="添加一个admin用户"><a name="t27"></a>添加一个admin用户</h3>



<pre class="prettyprint"><code class="hljs avrasm has-numbering">use admin
db<span class="hljs-preprocessor">.createUser</span>({user : <span class="hljs-string">"admin"</span>, pwd: <span class="hljs-string">"pass"</span>, roles: [ <span class="hljs-string">"readWrite"</span>, <span class="hljs-string">"dbAdmin"</span> ] })
db<span class="hljs-preprocessor">.system</span><span class="hljs-preprocessor">.users</span><span class="hljs-preprocessor">.find</span>()</code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>



<h4 id="常见的权限有">常见的权限有</h4>

<ul>
<li>read</li>
<li>readWrite</li>
<li>dbAdmin</li>
<li>dbOwner</li>
<li>userAdmin</li>
<li>backup</li>
<li>restore</li>
<li>readAnyDatabase</li>
<li>readWriteAnyDatabase</li>
<li>userAdminAnyDatabase</li>
<li>dbAdminAnyDatabase</li>
<li>root （最高权限）</li>
<li>…</li>
</ul>

<p>具体含义请见 <a href="http://docs.mongodb.org/v3.0/reference/built-in-roles/" target="_blank">http://docs.mongodb.org/v3.0/reference/built-in-roles/</a></p>



<h3 id="开启认证"><a name="t28"></a>开启认证</h3>

<p>在mongo配置文件中加入，之后重启生效:</p>



<pre class="prettyprint"><code class="hljs ini has-numbering"><span class="hljs-setting">auth=<span class="hljs-value"><span class="hljs-keyword">true</span></span></span></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>service mongodb restart</p>                            </div>
                <link rel="stylesheet" href="http://csdnimg.cn/release/phoenix/production/markdown_views-d4dade9c33.css">
                    </div>
    </article>