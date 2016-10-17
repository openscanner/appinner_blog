Title: 针对线上仓库android外部包引用情况的分析
Date: 2016-10-17 14:30
Modified: 2016-10-17 14:30
lang: cn
Category: statistics
Tags: statistics
Slug: external-packages
Summary: 利用 [AppInner](https://www.appinner.com)后台数据统计分析android外部包引用情况

- [数据源](#sec-1)
- [数据分析](#sec-2)
- [引用次数在前100位的包列表](#sec-3)
- [引用次数在前100位的组织列表](#sec-4)


# 数据源<a id="sec-1"></a>

本次分析使用了appinner线上的1,361,737条数据．其中应用商店app所占比例见下图：
![img]({filename}/images/stores_distribution.png?raw=true)

这里主要使用了googleplay的数据源，其它应用商店的数据质量不如googleplay，仅使用了一小部分

# 数据分析<a id="sec-2"></a>

在这些app中，一共发现了 **722,361** 个外部java包(app主包外的java包)，这些包总共被引用了 **28,279,239** 次．

| 引用次数的范围  | 被引用包的数量 | 引用包占总引用的百分比 |
|--------------- |------- |------------ |
|                 |         |              |
| 100,000次以上   | 25      | 0.0034608734 |
| 50,000-100,000次 | 49      | 0.0067833117 |
| 10,000-50,000次 | 371     | 0.051359363  |
| 5,000-10,000次  | 494     | 0.06838686   |
| 1,000-5,000次   | 1,438   | 0.19906944   |
| 500-1,000次     | 1,368   | 0.18937899   |
| 100-500次       | 7,310   | 1.0119594    |
| 10-100次        | 59,167  | 8.19078      |
| 1-10次          | 652,139 | 90.278824    |

可以看到：

-   98%的包被引用的次数都在100次以内
-   99%的包被引用次数在500次以内
-   只有不到1%的包被引用次数在500次以上．

引用次数排名靠前的包的分布图：

![img]({filename}/images/top-packages.png?raw=true)

我们使用包的前两个单词做为组织名，从 **722,361** 个外部java包中得到了 **149,204** 个组织名

| 引用次数的范围       | 被引用组织的数量 | 引用组织占总引用的百分比 |
|-------------------- |-------- |------------ |
| 1,000,000-5,000,000次 | 3        | 0.00201067   |
| 500,000-1,000,000次  | 5        | 0.0033511166 |
| 100,000-500,000次    | 33       | 0.022117369  |
| 50,000-100,000次     | 31       | 0.020776924  |
| 10,000-50,000次      | 158      | 0.10589528   |
| 5,000-10,000次       | 171      | 0.11460819   |
| 1,000-5,000次        | 825      | 0.5529342    |
| 500-1,000次          | 740      | 0.49596524   |
| 100-500次            | 4,232    | 2.836385     |
| 10-100次             | 27,930   | 18.719338    |
| 1-10次               | 115,076  | 77.12662     |

可以看到：

-   95.8%的组织被引用的次数都在100次以内
-   98.6%的组织被引用次数在500次以内
-   只有大概1%的组织被引用次数在500次以上．

引用次数排名靠前的组织的分布图：

![img]({filename}/images/top-org-packages.png?raw=true)

# 引用次数在前100位的包列表<a id="sec-3"></a>

| 序号 | 引用次数 | 包名                                            | 引用次数百分比 |
|--- |------- |----------------------------------------------- |---------- |
| 1   | 671,718 | [com.google.ads](https://www.appinner.com/main/search?q=class:com.google.ads){:target="_blank"}                                  | 2.3753043  |
| 2   | 617,017 | [com.google.android.gms](https://www.appinner.com/main/search?q=class:com.google.android.gms){:target="_blank"}                          | 2.1818726  |
| 3   | 320,436 | [com.tencent.mm.sdk](https://www.appinner.com/main/search?q=class:com.tencent.mm.sdk){:target="_blank"}                              | 1.1331139  |
| 4   | 308,041 | [com.tencent.wxop.stat](https://www.appinner.com/main/search?q=class:com.tencent.wxop.stat){:target="_blank"}                           | 1.0892831  |
| 5   | 242,044 | [com.tencent.stat](https://www.appinner.com/main/search?q=class:com.tencent.stat){:target="_blank"}                                | 0.855907   |
| 6   | 240,073 | [com.tencent.tauth](https://www.appinner.com/main/search?q=class:com.tencent.tauth){:target="_blank"}                               | 0.8489372  |
| 7   | 237,953 | [com.tencent.open](https://www.appinner.com/main/search?q=class:com.tencent.open){:target="_blank"}                                | 0.84144056 |
| 8   | 234,715 | [com.tencent.connect](https://www.appinner.com/main/search?q=class:com.tencent.connect){:target="_blank"}                             | 0.8299905  |
| 9   | 230,818 | [com.tencent.qqconnect.dataprovider.datatype](https://www.appinner.com/main/search?q=class:com.tencent.qqconnect.dataprovider.datatype){:target="_blank"}     | 0.81621004 |
| 10  | 230,502 | [com.tencent.map](https://www.appinner.com/main/search?q=class:com.tencent.map){:target="_blank"}                                 | 0.8150926  |
| 11  | 208,949 | [com.baidu.lbsapi.auth](https://www.appinner.com/main/search?q=class:com.baidu.lbsapi.auth){:target="_blank"}                           | 0.7388777  |
| 12  | 208,714 | [com.baidu.mapapi](https://www.appinner.com/main/search?q=class:com.baidu.mapapi){:target="_blank"}                                | 0.7380467  |
| 13  | 207,815 | [com.baidu.platform.comapi](https://www.appinner.com/main/search?q=class:com.baidu.platform.comapi){:target="_blank"}                       | 0.7348677  |
| 14  | 207,770 | [com.baidu.vi](https://www.appinner.com/main/search?q=class:com.baidu.vi){:target="_blank"}                                    | 0.73470855 |
| 15  | 207,680 | [com.baidu.platform.comjni](https://www.appinner.com/main/search?q=class:com.baidu.platform.comjni){:target="_blank"}                       | 0.7343903  |
| 16  | 207,627 | [com.baidu.android.bbalbs.common](https://www.appinner.com/main/search?q=class:com.baidu.android.bbalbs.common){:target="_blank"}                 | 0.7342029  |
| 17  | 200,488 | [com.umeng.analytics](https://www.appinner.com/main/search?q=class:com.umeng.analytics){:target="_blank"}                             | 0.7089582  |
| 18  | 167,941 | [com.google.gson](https://www.appinner.com/main/search?q=class:com.google.gson){:target="_blank"}                                 | 0.59386677 |
| 19  | 161,461 | [com.android.vending.billing](https://www.appinner.com/main/search?q=class:com.android.vending.billing){:target="_blank"}                     | 0.5709524  |
| 20  | 158,348 | [u.aly](https://www.appinner.com/main/search?q=class:u.aly){:target="_blank"}                                           | 0.55994434 |
| 21  | 153,258 | [com.facebook.internal](https://www.appinner.com/main/search?q=class:com.facebook.internal){:target="_blank"}                           | 0.5419453  |
| 22  | 132,284 | [com.facebook.android](https://www.appinner.com/main/search?q=class:com.facebook.android){:target="_blank"}                            | 0.4677778  |
| 23  | 119,116 | [com.facebook.widget](https://www.appinner.com/main/search?q=class:com.facebook.widget){:target="_blank"}                             | 0.4212136  |
| 24  | 118,334 | [com.facebook.model](https://www.appinner.com/main/search?q=class:com.facebook.model){:target="_blank"}                              | 0.4184483  |
| 25  | 111,189 | [com.unity3d.player](https://www.appinner.com/main/search?q=class:com.unity3d.player){:target="_blank"}                              | 0.39318243 |
| 26  | 98,769  | [com.ut.device](https://www.appinner.com/main/search?q=class:com.ut.device){:target="_blank"}                                   | 0.34926328 |
| 27  | 89,452  | [org.apache.cordova](https://www.appinner.com/main/search?q=class:org.apache.cordova){:target="_blank"}                              | 0.31631684 |
| 28  | 86,431  | [com.nineoldandroids.util](https://www.appinner.com/main/search?q=class:com.nineoldandroids.util){:target="_blank"}                        | 0.3056341  |
| 29  | 86,034  | [com.squareup.okhttp](https://www.appinner.com/main/search?q=class:com.squareup.okhttp){:target="_blank"}                             | 0.30423024 |
| 30  | 85,416  | [com.nostra13.universalimageloader.core](https://www.appinner.com/main/search?q=class:com.nostra13.universalimageloader.core){:target="_blank"}          | 0.3020449  |
| 31  | 85,295  | [com.google.zxing](https://www.appinner.com/main/search?q=class:com.google.zxing){:target="_blank"}                                | 0.30161703 |
| 32  | 84,219  | [com.nineoldandroids.animation](https://www.appinner.com/main/search?q=class:com.nineoldandroids.animation){:target="_blank"}                   | 0.2978121  |
| 33  | 84,156  | [com.nostra13.universalimageloader.utils](https://www.appinner.com/main/search?q=class:com.nostra13.universalimageloader.utils){:target="_blank"}         | 0.29758933 |
| 34  | 84,145  | [com.nostra13.universalimageloader.cache.disc](https://www.appinner.com/main/search?q=class:com.nostra13.universalimageloader.cache.disc){:target="_blank"}    | 0.29755044 |
| 35  | 84,144  | [com.nostra13.universalimageloader.cache.memory](https://www.appinner.com/main/search?q=class:com.nostra13.universalimageloader.cache.memory){:target="_blank"}  | 0.2975469  |
| 36  | 84,124  | [com.flurry.android](https://www.appinner.com/main/search?q=class:com.flurry.android){:target="_blank"}                              | 0.29747617 |
| 37  | 83,956  | [com.nineoldandroids.view](https://www.appinner.com/main/search?q=class:com.nineoldandroids.view){:target="_blank"}                        | 0.2968821  |
| 38  | 82,324  | [com.sina.weibo.sdk](https://www.appinner.com/main/search?q=class:com.sina.weibo.sdk){:target="_blank"}                              | 0.29111108 |
| 39  | 82,058  | [com.google.android.gcm](https://www.appinner.com/main/search?q=class:com.google.android.gcm){:target="_blank"}                          | 0.29017046 |
| 40  | 81,882  | [com.umeng.message](https://www.appinner.com/main/search?q=class:com.umeng.message){:target="_blank"}                               | 0.2895481  |
| 41  | 80,831  | [com.google.analytics.tracking.android](https://www.appinner.com/main/search?q=class:com.google.analytics.tracking.android){:target="_blank"}           | 0.28583157 |
| 42  | 80,829  | [com.umeng.common.message](https://www.appinner.com/main/search?q=class:com.umeng.common.message){:target="_blank"}                        | 0.2858245  |
| 43  | 80,584  | [com.inmobi](https://www.appinner.com/main/search?q=class:com.inmobi){:target="_blank"}                                      | 0.28495815 |
| 44  | 77,079  | [org.apache.http.entity.mime](https://www.appinner.com/main/search?q=class:org.apache.http.entity.mime){:target="_blank"}                     | 0.2725639  |
| 45  | 75,342  | [com.squareup.picasso](https://www.appinner.com/main/search?q=class:com.squareup.picasso){:target="_blank"}                            | 0.2664216  |
| 46  | 66,865  | [com.igexin](https://www.appinner.com/main/search?q=class:com.igexin){:target="_blank"}                                      | 0.23644553 |
| 47  | 66,023  | [com.google.android.gms.common](https://www.appinner.com/main/search?q=class:com.google.android.gms.common){:target="_blank"}                   | 0.23346809 |
| 48  | 65,542  | [com.google.android.gms.internal](https://www.appinner.com/main/search?q=class:com.google.android.gms.internal){:target="_blank"}                 | 0.23176719 |
| 49  | 63,489  | [com.chartboost.sdk](https://www.appinner.com/main/search?q=class:com.chartboost.sdk){:target="_blank"}                              | 0.22450745 |
| 50  | 63,350  | [com.actionbarsherlock.internal](https://www.appinner.com/main/search?q=class:com.actionbarsherlock.internal){:target="_blank"}                  | 0.22401592 |
| 51  | 63,310  | [com.actionbarsherlock.widget](https://www.appinner.com/main/search?q=class:com.actionbarsherlock.widget){:target="_blank"}                    | 0.22387448 |
| 52  | 63,255  | [com.actionbarsherlock.app](https://www.appinner.com/main/search?q=class:com.actionbarsherlock.app){:target="_blank"}                       | 0.22367999 |
| 53  | 62,783  | [com.google.android.gms.maps](https://www.appinner.com/main/search?q=class:com.google.android.gms.maps){:target="_blank"}                     | 0.22201091 |
| 54  | 62,692  | [com.actionbarsherlock.view](https://www.appinner.com/main/search?q=class:com.actionbarsherlock.view){:target="_blank"}                      | 0.22168912 |
| 55  | 61,004  | [com.google.android.gms.games](https://www.appinner.com/main/search?q=class:com.google.android.gms.games){:target="_blank"}                    | 0.21572009 |
| 56  | 59,734  | [com.google.android.gms.location](https://www.appinner.com/main/search?q=class:com.google.android.gms.location){:target="_blank"}                 | 0.21122916 |
| 57  | 58,594  | [com.google.android.gms.auth](https://www.appinner.com/main/search?q=class:com.google.android.gms.auth){:target="_blank"}                     | 0.20719794 |
| 58  | 58,372  | [com.google.android.gms.plus](https://www.appinner.com/main/search?q=class:com.google.android.gms.plus){:target="_blank"}                     | 0.2064129  |
| 59  | 57,961  | [com.google.android.gms.dynamic](https://www.appinner.com/main/search?q=class:com.google.android.gms.dynamic){:target="_blank"}                  | 0.20495954 |
| 60  | 56,708  | [com.google.android.gms.gcm](https://www.appinner.com/main/search?q=class:com.google.android.gms.gcm){:target="_blank"}                      | 0.20052873 |
| 61  | 56,690  | [com.flurry.sdk](https://www.appinner.com/main/search?q=class:com.flurry.sdk){:target="_blank"}                                  | 0.20046509 |
| 62  | 56,542  | [com.google.android.gms.wallet](https://www.appinner.com/main/search?q=class:com.google.android.gms.wallet){:target="_blank"}                   | 0.19994173 |
| 63  | 55,199  | [com.google.android.gms.panorama](https://www.appinner.com/main/search?q=class:com.google.android.gms.panorama){:target="_blank"}                 | 0.19519265 |
| 64  | 55,193  | [com.google.android.gms.ads](https://www.appinner.com/main/search?q=class:com.google.android.gms.ads){:target="_blank"}                      | 0.19517145 |
| 65  | 52,063  | [com.android.volley](https://www.appinner.com/main/search?q=class:com.android.volley){:target="_blank"}                              | 0.18410325 |
| 66  | 51,978  | [com.google.android.gms.drive](https://www.appinner.com/main/search?q=class:com.google.android.gms.drive){:target="_blank"}                    | 0.18380268 |
| 67  | 51,676  | [org.apache.commons.io](https://www.appinner.com/main/search?q=class:org.apache.commons.io){:target="_blank"}                           | 0.18273476 |
| 68  | 51,641  | [com.google.android.gms.appstate](https://www.appinner.com/main/search?q=class:com.google.android.gms.appstate){:target="_blank"}                 | 0.18261099 |
| 69  | 51,280  | [com.google.android.gms.cast](https://www.appinner.com/main/search?q=class:com.google.android.gms.cast){:target="_blank"}                     | 0.18133444 |
| 70  | 51,032  | [com.startapp.android.publish](https://www.appinner.com/main/search?q=class:com.startapp.android.publish){:target="_blank"}                    | 0.18045748 |
| 71  | 50,810  | [org.jsoup.nodes](https://www.appinner.com/main/search?q=class:org.jsoup.nodes){:target="_blank"}                                 | 0.17967244 |
| 72  | 50,575  | [com.google.android.vending.licensing](https://www.appinner.com/main/search?q=class:com.google.android.vending.licensing){:target="_blank"}            | 0.17884144 |
| 73  | 50,445  | [org.jsoup.helper](https://www.appinner.com/main/search?q=class:org.jsoup.helper){:target="_blank"}                                | 0.17838174 |
| 74  | 50,437  | [org.jsoup.parser](https://www.appinner.com/main/search?q=class:org.jsoup.parser){:target="_blank"}                                | 0.17835345 |
| 75  | 47,056  | [com.google.tagmanager](https://www.appinner.com/main/search?q=class:com.google.tagmanager){:target="_blank"}                           | 0.16639768 |
| 76  | 47,015  | [com.google.android.gms.identity.intents](https://www.appinner.com/main/search?q=class:com.google.android.gms.identity.intents){:target="_blank"}         | 0.1662527  |
| 77  | 45,822  | [org.apache.commons.codec](https://www.appinner.com/main/search?q=class:org.apache.commons.codec){:target="_blank"}                        | 0.16203407 |
| 78  | 45,284  | [com.google.analytics.midtier.proto.containertag](https://www.appinner.com/main/search?q=class:com.google.analytics.midtier.proto.containertag){:target="_blank"} | 0.1601316  |
| 79  | 45,278  | [com.google.analytics.containertag.proto](https://www.appinner.com/main/search?q=class:com.google.analytics.containertag.proto){:target="_blank"}         | 0.16011039 |
| 80  | 45,210  | [org.cocos2dx.lib](https://www.appinner.com/main/search?q=class:org.cocos2dx.lib){:target="_blank"}                                | 0.15986993 |
| 81  | 45,046  | [com.google.analytics.containertag.common](https://www.appinner.com/main/search?q=class:com.google.analytics.containertag.common){:target="_blank"}        | 0.15929    |
| 82  | 44,119  | [com.tencent.android.tpush](https://www.appinner.com/main/search?q=class:com.tencent.android.tpush){:target="_blank"}                       | 0.15601197 |
| 83  | 44,106  | [com.google.android.gms.tagmanager](https://www.appinner.com/main/search?q=class:com.google.android.gms.tagmanager){:target="_blank"}               | 0.155966   |
| 84  | 44,009  | [com.alipay.android.app](https://www.appinner.com/main/search?q=class:com.alipay.android.app){:target="_blank"}                          | 0.15562299 |
| 85  | 43,406  | [com.google.android.gms.analytics](https://www.appinner.com/main/search?q=class:com.google.android.gms.analytics){:target="_blank"}                | 0.15349069 |
| 86  | 43,068  | [com.facebook.ads](https://www.appinner.com/main/search?q=class:com.facebook.ads){:target="_blank"}                                | 0.15229547 |
| 87  | 40,428  | [com.loopj.android.http](https://www.appinner.com/main/search?q=class:com.loopj.android.http){:target="_blank"}                          | 0.14296    |
| 88  | 39,955  | [org.slf4j.helpers](https://www.appinner.com/main/search?q=class:org.slf4j.helpers){:target="_blank"}                               | 0.14128739 |
| 89  | 39,573  | [twitter4j.internal.http](https://www.appinner.com/main/search?q=class:twitter4j.internal.http){:target="_blank"}                         | 0.13993658 |
| 90  | 39,460  | [twitter4j.internal.async](https://www.appinner.com/main/search?q=class:twitter4j.internal.async){:target="_blank"}                        | 0.13953699 |
| 91  | 39,441  | [twitter4j.internal.logging](https://www.appinner.com/main/search?q=class:twitter4j.internal.logging){:target="_blank"}                      | 0.1394698  |
| 92  | 38,894  | [com.google.android.gms.wearable](https://www.appinner.com/main/search?q=class:com.google.android.gms.wearable){:target="_blank"}                 | 0.13753553 |
| 93  | 38,529  | [com.sina.sso](https://www.appinner.com/main/search?q=class:com.sina.sso){:target="_blank"}                                    | 0.13624482 |
| 94  | 38,416  | [org.jsoup.select](https://www.appinner.com/main/search?q=class:org.jsoup.select){:target="_blank"}                                | 0.13584523 |
| 95  | 37,566  | [twitter4j.internal.util](https://www.appinner.com/main/search?q=class:twitter4j.internal.util){:target="_blank"}                         | 0.1328395  |
| 96  | 37,437  | [org.apache.http](https://www.appinner.com/main/search?q=class:org.apache.http){:target="_blank"}                                 | 0.13238333 |
| 97  | 37,426  | [com.facebook.login](https://www.appinner.com/main/search?q=class:com.facebook.login){:target="_blank"}                              | 0.13234444 |
| 98  | 37,421  | [com.crashlytics.android](https://www.appinner.com/main/search?q=class:com.crashlytics.android){:target="_blank"}                         | 0.13232675 |
| 99  | 37,360  | [org.jsoup.examples](https://www.appinner.com/main/search?q=class:org.jsoup.examples){:target="_blank"}                              | 0.13211105 |
| 100 | 37,135  | [twitter4j.internal.json](https://www.appinner.com/main/search?q=class:twitter4j.internal.json){:target="_blank"}                         | 0.13131541 |

# 引用次数在前100位的组织列表<a id="sec-4"></a>

| 序号 | 引用次数  | 组织名                | 引用次数百分比 |
|--- |--------- |--------------------- |---------- |
| 1   | 3,981,769 | [com.google](https://www.appinner.com/main/search?q=class:com.google){:target="_blank"}            | 14.080184  |
| 2   | 2,335,994 | [com.tencent](https://www.appinner.com/main/search?q=class:com.tencent){:target="_blank"}           | 8.260455   |
| 3   | 1,491,627 | [com.baidu](https://www.appinner.com/main/search?q=class:com.baidu){:target="_blank"}             | 5.2746363  |
| 4   | 925,287   | [com.facebook](https://www.appinner.com/main/search?q=class:com.facebook){:target="_blank"}          | 3.2719658  |
| 5   | 713,405   | [org.apache](https://www.appinner.com/main/search?q=class:org.apache){:target="_blank"}            | 2.5227163  |
| 6   | 697,470   | [com.umeng](https://www.appinner.com/main/search?q=class:com.umeng){:target="_blank"}             | 2.4663675  |
| 7   | 605,386   | [com.biznessapps](https://www.appinner.com/main/search?q=class:com.biznessapps){:target="_blank"}       | 2.1407435  |
| 8   | 596,607   | [com.qbiki](https://www.appinner.com/main/search?q=class:com.qbiki){:target="_blank"}             | 2.1096995  |
| 9   | 349,048   | [com.nostra13](https://www.appinner.com/main/search?q=class:com.nostra13){:target="_blank"}          | 1.2342906  |
| 10  | 330,225   | [com.android](https://www.appinner.com/main/search?q=class:com.android){:target="_blank"}           | 1.1677294  |
| 11  | 264,270   | [org.jsoup](https://www.appinner.com/main/search?q=class:org.jsoup){:target="_blank"}             | 0.93450177 |
| 12  | 255,935   | [com.nineoldandroids](https://www.appinner.com/main/search?q=class:com.nineoldandroids){:target="_blank"}   | 0.90502787 |
| 13  | 254,302   | [com.actionbarsherlock](https://www.appinner.com/main/search?q=class:com.actionbarsherlock){:target="_blank"} | 0.8992533  |
| 14  | 230,520   | [mono.android](https://www.appinner.com/main/search?q=class:mono.android){:target="_blank"}          | 0.8151563  |
| 15  | 230,110   | [twitter4j.internal](https://www.appinner.com/main/search?q=class:twitter4j.internal){:target="_blank"}    | 0.81370646 |
| 16  | 220,681   | [com.j256](https://www.appinner.com/main/search?q=class:com.j256){:target="_blank"}              | 0.780364   |
| 17  | 215,903   | [org.kobjects](https://www.appinner.com/main/search?q=class:org.kobjects){:target="_blank"}          | 0.7634682  |
| 18  | 192,289   | [com.inmobi](https://www.appinner.com/main/search?q=class:com.inmobi){:target="_blank"}            | 0.67996526 |
| 19  | 191,689   | [com.alipay](https://www.appinner.com/main/search?q=class:com.alipay){:target="_blank"}            | 0.6778435  |
| 20  | 191,286   | [com.squareup](https://www.appinner.com/main/search?q=class:com.squareup){:target="_blank"}          | 0.6764185  |
| 21  | 174,677   | [com.mopub](https://www.appinner.com/main/search?q=class:com.mopub){:target="_blank"}             | 0.61768634 |
| 22  | 171,207   | [com.parse](https://www.appinner.com/main/search?q=class:com.parse){:target="_blank"}             | 0.6054158  |
| 23  | 170,863   | [com.flurry](https://www.appinner.com/main/search?q=class:com.flurry){:target="_blank"}            | 0.6041994  |
| 24  | 162,141   | [com.androidnative](https://www.appinner.com/main/search?q=class:com.androidnative){:target="_blank"}     | 0.573357   |
| 25  | 160,082   | [cn.sharesdk](https://www.appinner.com/main/search?q=class:cn.sharesdk){:target="_blank"}           | 0.56607605 |
| 26  | 158,348   | [u.aly](https://www.appinner.com/main/search?q=class:u.aly){:target="_blank"}                 | 0.55994434 |
| 27  | 156,548   | [org.acra](https://www.appinner.com/main/search?q=class:org.acra){:target="_blank"}              | 0.5535792  |
| 28  | 154,183   | [com.unity3d](https://www.appinner.com/main/search?q=class:com.unity3d){:target="_blank"}           | 0.5452162  |
| 29  | 154,033   | [com.heyzap](https://www.appinner.com/main/search?q=class:com.heyzap){:target="_blank"}            | 0.5446858  |
| 30  | 149,857   | [com.unionpay](https://www.appinner.com/main/search?q=class:com.unionpay){:target="_blank"}          | 0.5299188  |
| 31  | 146,153   | [com.adobe](https://www.appinner.com/main/search?q=class:com.adobe){:target="_blank"}             | 0.51682085 |
| 32  | 144,892   | [com.amap](https://www.appinner.com/main/search?q=class:com.amap){:target="_blank"}              | 0.5123617  |
| 33  | 143,014   | [com.sina](https://www.appinner.com/main/search?q=class:com.sina){:target="_blank"}              | 0.5057208  |
| 34  | 127,819   | [gnu.kawa](https://www.appinner.com/main/search?q=class:gnu.kawa){:target="_blank"}              | 0.45198882 |
| 35  | 126,801   | [com.revmob](https://www.appinner.com/main/search?q=class:com.revmob){:target="_blank"}            | 0.448389   |
| 36  | 117,426   | [org.chromium](https://www.appinner.com/main/search?q=class:org.chromium){:target="_blank"}          | 0.41523746 |
| 37  | 115,574   | [com.applovin](https://www.appinner.com/main/search?q=class:com.applovin){:target="_blank"}          | 0.4086885  |
| 38  | 111,408   | [oauth.signpost](https://www.appinner.com/main/search?q=class:oauth.signpost){:target="_blank"}        | 0.39395684 |
| 39  | 105,237   | [com.amazonaws](https://www.appinner.com/main/search?q=class:com.amazonaws){:target="_blank"}         | 0.3721352  |
| 40  | 100,882   | [com.ut](https://www.appinner.com/main/search?q=class:com.ut){:target="_blank"}                | 0.3567352  |
| 41  | 100,674   | [org.slf4j](https://www.appinner.com/main/search?q=class:org.slf4j){:target="_blank"}             | 0.35599968 |
| 42  | 93,972    | [com.amazon](https://www.appinner.com/main/search?q=class:com.amazon){:target="_blank"}            | 0.3323003  |
| 43  | 93,494    | [io.rong](https://www.appinner.com/main/search?q=class:io.rong){:target="_blank"}               | 0.33061    |
| 44  | 92,539    | [com.seattleclouds](https://www.appinner.com/main/search?q=class:com.seattleclouds){:target="_blank"}     | 0.327233   |
| 45  | 89,542    | [org.cocos2d](https://www.appinner.com/main/search?q=class:org.cocos2d){:target="_blank"}           | 0.3166351  |
| 46  | 77,527    | [org.andengine](https://www.appinner.com/main/search?q=class:org.andengine){:target="_blank"}         | 0.2741481  |
| 47  | 77,003    | [org.kxml2](https://www.appinner.com/main/search?q=class:org.kxml2){:target="_blank"}             | 0.27229515 |
| 48  | 74,111    | [com.urbanairship](https://www.appinner.com/main/search?q=class:com.urbanairship){:target="_blank"}      | 0.26206857 |
| 49  | 73,341    | [com.igexin](https://www.appinner.com/main/search?q=class:com.igexin){:target="_blank"}            | 0.2593457  |
| 50  | 73,174    | [uk.co](https://www.appinner.com/main/search?q=class:uk.co){:target="_blank"}                 | 0.25875518 |
| 51  | 69,394    | [com.sun](https://www.appinner.com/main/search?q=class:com.sun){:target="_blank"}               | 0.2453885  |
| 52  | 68,925    | [com.ta](https://www.appinner.com/main/search?q=class:com.ta){:target="_blank"}                | 0.24373003 |
| 53  | 68,602    | [com.androidquery](https://www.appinner.com/main/search?q=class:com.androidquery){:target="_blank"}      | 0.24258785 |
| 54  | 68,113    | [com.github](https://www.appinner.com/main/search?q=class:com.github){:target="_blank"}            | 0.24085866 |
| 55  | 67,810    | [org.jaxen](https://www.appinner.com/main/search?q=class:org.jaxen){:target="_blank"}             | 0.2397872  |
| 56  | 66,937    | [com.chartboost](https://www.appinner.com/main/search?q=class:com.chartboost){:target="_blank"}        | 0.23670013 |
| 57  | 66,516    | [com.appyet](https://www.appinner.com/main/search?q=class:com.appyet){:target="_blank"}            | 0.23521142 |
| 58  | 65,839    | [com.fasterxml](https://www.appinner.com/main/search?q=class:com.fasterxml){:target="_blank"}         | 0.23281743 |
| 59  | 65,626    | [org.scribe](https://www.appinner.com/main/search?q=class:org.scribe){:target="_blank"}            | 0.23206423 |
| 60  | 65,544    | [com.pollfish](https://www.appinner.com/main/search?q=class:com.pollfish){:target="_blank"}          | 0.23177426 |
| 61  | 60,856    | [org.cocos2dx](https://www.appinner.com/main/search?q=class:org.cocos2dx){:target="_blank"}          | 0.21519673 |
| 62  | 59,477    | [com.mobcent](https://www.appinner.com/main/search?q=class:com.mobcent){:target="_blank"}           | 0.21032037 |
| 63  | 57,500    | [com.appmk](https://www.appinner.com/main/search?q=class:com.appmk){:target="_blank"}             | 0.20332937 |
| 64  | 57,462    | [mf.org](https://www.appinner.com/main/search?q=class:mf.org){:target="_blank"}                | 0.20319499 |
| 65  | 55,508    | [com.example](https://www.appinner.com/main/search?q=class:com.example){:target="_blank"}           | 0.19628534 |
| 66  | 55,088    | [com.startapp](https://www.appinner.com/main/search?q=class:com.startapp){:target="_blank"}          | 0.19480014 |
| 67  | 53,960    | [mono.com](https://www.appinner.com/main/search?q=class:mono.com){:target="_blank"}              | 0.19081135 |
| 68  | 53,433    | [org.ksoap2](https://www.appinner.com/main/search?q=class:org.ksoap2){:target="_blank"}            | 0.1889478  |
| 69  | 51,025    | [com.immersion](https://www.appinner.com/main/search?q=class:com.immersion){:target="_blank"}         | 0.1804327  |
| 70  | 50,280    | [pdftron.pdf](https://www.appinner.com/main/search?q=class:pdftron.pdf){:target="_blank"}           | 0.17779827 |
| 71  | 50,211    | [org.bouncycastle](https://www.appinner.com/main/search?q=class:org.bouncycastle){:target="_blank"}      | 0.17755428 |
| 72  | 50,183    | [com.taobao](https://www.appinner.com/main/search?q=class:com.taobao){:target="_blank"}            | 0.17745526 |
| 73  | 48,738    | [org.dom4j](https://www.appinner.com/main/search?q=class:org.dom4j){:target="_blank"}             | 0.1723455  |
| 74  | 46,813    | [com.dns](https://www.appinner.com/main/search?q=class:com.dns){:target="_blank"}               | 0.1655384  |
| 75  | 46,746    | [com.xiaomi](https://www.appinner.com/main/search?q=class:com.xiaomi){:target="_blank"}            | 0.16530147 |
| 76  | 46,229    | [org.anddev](https://www.appinner.com/main/search?q=class:org.anddev){:target="_blank"}            | 0.16347328 |
| 77  | 46,142    | [com.loopj](https://www.appinner.com/main/search?q=class:com.loopj){:target="_blank"}             | 0.16316563 |
| 78  | 42,839    | [com.qq](https://www.appinner.com/main/search?q=class:com.qq){:target="_blank"}                | 0.15148568 |
| 79  | 42,160    | [com.vungle](https://www.appinner.com/main/search?q=class:com.vungle){:target="_blank"}            | 0.14908463 |
| 80  | 41,980    | [org.springframework](https://www.appinner.com/main/search?q=class:org.springframework){:target="_blank"}   | 0.14844813 |
| 81  | 41,942    | [jp.co](https://www.appinner.com/main/search?q=class:jp.co){:target="_blank"}                 | 0.14831375 |
| 82  | 41,766    | [com.googlecode](https://www.appinner.com/main/search?q=class:com.googlecode){:target="_blank"}        | 0.14769139 |
| 83  | 40,874    | [net.sourceforge](https://www.appinner.com/main/search?q=class:net.sourceforge){:target="_blank"}       | 0.14453712 |
| 84  | 40,861    | [javax.annotation](https://www.appinner.com/main/search?q=class:javax.annotation){:target="_blank"}      | 0.14449115 |
| 85  | 40,790    | [org.zywx](https://www.appinner.com/main/search?q=class:org.zywx){:target="_blank"}              | 0.14424008 |
| 86  | 40,291    | [com.alibaba](https://www.appinner.com/main/search?q=class:com.alibaba){:target="_blank"}           | 0.14247555 |
| 87  | 38,918    | [com.badlogic](https://www.appinner.com/main/search?q=class:com.badlogic){:target="_blank"}          | 0.13762039 |
| 88  | 38,791    | [nl.siegmann](https://www.appinner.com/main/search?q=class:nl.siegmann){:target="_blank"}           | 0.1371713  |
| 89  | 38,774    | [com.tapjoy](https://www.appinner.com/main/search?q=class:com.tapjoy){:target="_blank"}            | 0.13711119 |
| 90  | 38,649    | [com.jirbo](https://www.appinner.com/main/search?q=class:com.jirbo){:target="_blank"}             | 0.13666916 |
| 91  | 37,846    | [com.crashlytics](https://www.appinner.com/main/search?q=class:com.crashlytics){:target="_blank"}       | 0.13382963 |
| 92  | 36,476    | [com.autonavi](https://www.appinner.com/main/search?q=class:com.autonavi){:target="_blank"}          | 0.12898508 |
| 93  | 36,425    | [com.qihoo](https://www.appinner.com/main/search?q=class:com.qihoo){:target="_blank"}             | 0.12880473 |
| 94  | 36,241    | [kankan.wheel](https://www.appinner.com/main/search?q=class:kankan.wheel){:target="_blank"}          | 0.12815409 |
| 95  | 35,624    | [org.java\_websocket](https://www.appinner.com/main/search?q=class:org.java\_websocket){:target="_blank"}   | 0.12597227 |
| 96  | 35,571    | [okhttp3.internal](https://www.appinner.com/main/search?q=class:okhttp3.internal){:target="_blank"}      | 0.12578485 |
| 97  | 35,552    | [org.nexage](https://www.appinner.com/main/search?q=class:org.nexage){:target="_blank"}            | 0.12571767 |
| 98  | 34,837    | [org.achartengine](https://www.appinner.com/main/search?q=class:org.achartengine){:target="_blank"}      | 0.12318931 |
| 99  | 34,737    | [org.jdom2](https://www.appinner.com/main/search?q=class:org.jdom2){:target="_blank"}             | 0.12283569 |
| 100 | 33,805    | [org.android](https://www.appinner.com/main/search?q=class:org.android){:target="_blank"}           | 0.11953999 |
