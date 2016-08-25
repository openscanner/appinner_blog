Title: 对比各应用商店下应用的权限差别
Date: 2016-8-25 14:30
Modified: 2016-8-25 14:30
lang: cn
Category: statistics
Tags: statistics, platform, permission
Slug: permissions-on-stores
Summary: 利用 [AppInner](https://www.appinner.com) 简单统计下各应用商店下app权限的差别.

## 00 序言

大家到应用商店下载应用，都会看到app请求的权限列表，用户在安装之前也会弹出请求权限的提示。

> App要实现其功能，是需要请求各种权限的，但是也有些app借助这种便利，去申请了它并不需要的权限，
> 甚至利用一些申请到的敏感权限去收集用户隐私，窃取其他app的运行数据等等。

> 比如，我们就看到过明明是同样的app，在不同的应用商店中权限要求会不一样。

## 01 分析方法

### 分析哪些权限？

> 安卓应用的权限要求多达数百种，单单官方的权限列表就高达一百种以上，除此之外还有一些app自定义了各种稀奇古怪的权限要求
> （这个容我有时间也会做一个详细的分析），因此对这上百种权限要求进行分类统计会比较耗时耗力，

我们决定有选择性的挑一些特别敏感的权限进行分析。

### 如何进行分析？

最为科学合理的分析方法应该是，逐个比对相同类型的app的权限要求，然后对这些权限要求进行分类统计，
以此为基础再对各个不同的应用商店进行对比。

但是这样我们面临两个问题:

- 一个就是各应用商店内的app总数并不相同，
- 另一个就是不同的应用商店，其app的分类标准也不一样。

我们最终选取了一个更加简便的方法:

> 以单个应用商店为对象，统计其对应的权限数量，然后对应用的总数求平均数，这个平均值作为本文的主要比较对象。
> 以上方法相对简单，考虑到数百万的应用样本数量，这种比较方法还是有一定的分析价值的。 

## 03 分析范围

Android应用商店，我们选取了最有代表性的googleplay，这个也是谷歌的官方应用商店，目前应用的数量110多万，
另外我们选取了国内的腾讯、豌豆荚、360、mi和安智等10个有代表性的应用商店，应用样本数量30多万。

权限的分析我们根据谷歌官方提供的敏感权限列表选择了

- android.permission.ACCESS_FINE_LOCATION 访问精确的位置(如GPS)；
- android.permission.READ_CONTACTS 读取用户联系人数据
- android.permission.CAMERA 调用摄像头
- android.permission.READ_SMS 读取短信息

## 04 分析结果

- 样本总数

  > [version:all](https://www.appinner.com/main/search?q=version:all&page=1)

  > 将该搜索保存成myprofile后，可以绘图查看

  ![store.count]({filename}/images/permissions_stores_count.png)

- 调用了四种权限中任意一种的样本数量统计

  > [permission:android.permission.ACCESS_FINE_LOCATION or permission:android.permission.READ_CONTACTS or permission:android.permission.CAMERA or permission:android.permission.READ_SMS](https://www.appinner.com/main/search?q=(permission:android.permission.ACCESS_FINE_LOCATION)%20or%20%20(permission:android.permission.READ_CONTACTS)%20%20or%20(permission:android.permission.CAMERA)%20or%20(permission:android.permission.READ_SMS)&page=1)

  ![or.count]({filename}/images/permissions_or_count.png)

- 调用了四种权限中所有权限的样本数量统计

  > [permission:android.permission.ACCESS_FINE_LOCATION permission:android.permission.READ_CONTACTS  permission:android.permission.CAMERA  permission:android.permission.READ_SMS](https://www.appinner.com/main/search?q=(permission:android.permission.ACCESS_FINE_LOCATION)%20%20%20(permission:android.permission.READ_CONTACTS)%20%20(permission:android.permission.CAMERA)%20%20(permission:android.permission.READ_SMS)&page=1)

  ![and.count]({filename}/images/permissions_and_count.png)

- 应用商店中使用了以上四种敏感权限的app占比

| 商店名称   | 样本总数 | 一种敏感权限 |   比例 | 四种敏感权限 |  比例 |
|----|----|----|----|-----|----|
| Googleplay |  1124145 |       247660 | 22.03% |         1625 | 0.14% |
| Anzhi      |   113849 |        39744 | 34.91% |         1593 | 1.40% |
| 360        |    55693 |        14736 | 26.46% |          748 | 1.34% |
| Wandoujia  |    32068 |        10912 | 34.03% |          517 | 1.61% |
| Pc6        |    26653 |         6618 | 24.83% |          486 | 1.82% |
| Pp         |    19433 |         6497 | 33.43% |          477 | 2.45% |
| Mi         |    14495 |         4909 | 33.87% |          386 | 2.66% |
| Huawei     |    11542 |         4735 | 41.02% |          376 | 3.26% |
| Lenovo     |    10329 |         3872 | 37.49% |          279 | 2.70% |
| Iqiyi      |     9700 |         3522 | 36.31% |          215 | 2.22% |


## 05 结论

从上面的分析结果来看，googleplay上app的敏感权限比例还是比较低的，不愧是android的官方商店。

以上分析会随着总样本数量的增加而更加精确，欢迎使用[AppInner](https://www.appinner.com)查看最新的搜索结果。

