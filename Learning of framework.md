# Reference links for existed framework learning

## scrapy官方中文文档
http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

## Scrapy之断点续爬
https://zhuanlan.zhihu.com/p/26810901

## 断点续传
找一个物理存储(Mysql, text, redis)记录断点前的状态, 再次爬取时可利用与记录比较的方法筛选出哪些是没有爬过的，然后进行爬取。主要是筛选url。<br>
另外可以学习redis模块建队列，也是增量爬虫常用的一种。And bloomfilter<br>
https://blog.csdn.net/zcc_0015/article/details/50608063<br>
BloomFilter: https://blog.csdn.net/zcc_0015/article/details/50608063<br>
Redis: https://blog.csdn.net/zcc_0015/article/details/50688145<br>
BloomFilter + Redis: https://blog.csdn.net/qq_18495465/article/details/78500472<br>

## 增量爬虫

## 按优先级队列，看似是利用scrapy本身的多线程优先级进行排队，最新状态的爬虫放在最优先的位置。可能用了算法来建立优先级。
https://www.jianshu.com/p/cf840e12193a

## scrapy的改编框架webmagic

## 用哈希函数优化爬虫的，有兴趣的同学可以再了解一下。

## scrapy本身含有断电，断网，暂停后续传的机制（只需一些配置和scrapy crawler projectname + ....特殊的命令行即可做到)
https://blog.csdn.net/JavaLixy/article/details/78135985

## 定时爬取
https://blog.csdn.net/qq_21768483/article/details/78725481

## scrapy 重写内置函数
https://www.cnblogs.com/wzjbg/p/6507565.html

## scrapy 配置
https://segmentfault.com/a/1190000009321902




