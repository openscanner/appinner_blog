Title: 利用AppInner统计在线App生成平台
Date: 2016-8-18 10:30
Modified: 2016-8-18 10:30
lang: cn
Category: statistics
Tags: statistics, No-Code, platform
Slug: No-Code-Apps-Platform
Summary: 利用 [AppInner](https://www.appinner.com) 简单统计下无需编码的在线App生成平台实际情况


## 00 缘起
上周我们更新版本,在搜索页面中添加了几个简单的TOP统计数据。在检索关键 [version:all](https://www.appinner.com/main/search?q=version:all&page=1) 时,发现 package(包名) 统计数据有点意思。包名 air.com 高居第一位, 简单查了下,发现这个是 [Adobe Air](www.adobe.com/products/air.html)平台使用的包名前缀, 看来 Air 的占有率还是蛮高的,以后有时间可以分析下。位于第三位的包名是: com.andromom, 查了下 [andromo.com](http://www.andromo.com/) 居然是做 App 在线生成的, 这个刷新了作者的认知, 所以决定利用 AppInner 调查下这种平台的流行程度。

> [version:all](https://www.appinner.com/main/search?q=version:all&page=1)  表示检索所有版本,默认情况下 [AppInner](https://www.appinner.com) 只检索最新版本的app数据。

## 01 Andromo 统计
那怎么统计呢?
> 鉴于 GooglePlay数据相对比较权威,因此限制只统计 GooglePlay, 对应搜索关键词 store:googleplay,后续检索中默认都会带此过滤。

作者是通过 package:com.andromo 包名发现 andromo, 所以自然的使用搜索关键词 [package:com.andromo store:googleplay](https://www.appinner.com/main/search?q=package:com.andromo store:googleplay&page=1), 结果如下图:

![com.andromo]({filename}/images/pacakge_com.andromo.png)



点击查看 App 的详情,发现它们的证书都是一样的:
```txt
owner: CN=Andromo App, OU=Development, O="Andromo.com L=Winnipeg", ST=MB, C=CA
cert_sha256: C262A97FE5596C49A9560F0964D0408881EE5A982ED4B9BDFDD7F731EE8DA408
serial_number: 1312389651
sig_alg_OID: 1.2.840.113549.1.1.5
version: 3
issuer: CN=Andromo App, OU=Development, O="Andromo.com L=Winnipeg", ST=MB, C=CA
sig_algorithm: SHA1withRSA
```

因此利用证书进行检索:  
[cert:'C262A97FE5596C49A9560F0964D0408881EE5A982ED4B9BDFDD7F731EE8DA408' store:googleplay](https://www.appinner.com/main/search?q=cert:%27C262A97FE5596C49A9560F0964D0408881EE5A982ED4B9BDFDD7F731EE8DA408%27%20store:googleplay&page=1)。

结果如下:

![com.andromo_cert]({filename}/images/package_com.andromo_cert.png)

对上面两个结果简单分析: 
1. 证书检索出来的 app 有 15699 个, 包名的结果只有 8415, 利用证书检索的结果更准确。
2. 同时将近一半利用 andromo 生成的app没有使用默认包名。
3. 左边栏统计数据中, 看起来前几位的开发者都至少开发了上百款App, 还真是高产。 

左边栏最上面有CreateReport功能, 我们来看一下结果。AppInner提供了对搜索结果创建报告的功能,点击后提示需要先创建Profile(登录后用户)。

![create_profile_andromo]({filename}/images/create_profile_andromo.png)

输入个名字,点击创建(Create), 然后在MyProfile看到一个新的Profile。

![myprofile_andromo]({filename}/images/myprofile_andromo.png)

点击创建报告(Create Report), 等待片刻, 提示创建成功, 然后就可以点击新生成的报告查看, 报告页有点长, 有兴趣的可以自己去建一个看看,我这里只截取2个看一下。如果数据和我这里的不一致是正常的,因为AppInner每天的数据都在快速增长。

第一个是类型分布,看起来音乐和娱乐类型加起来超过了1/3。

![AndromoApp_report_1]({filename}/images/AndromoApp_report_1.png)

第二个是下载量, 绝大部多数 App 都没什么人用, 但是也有30个超过了百万, 甚至还有2个超过了5百万。

![AndromoApp_report_2]({filename}/images/AndromoApp_report_2.png)

Andromo 在其主页上宣称其是: `The #1 Android App Maker Platform.`, 是真的吗? 


## 02 平台统计

作者统计了20个平台在GooglePlay上的App数量。直接列表如下:


|厂商 | 主页 | 搜索词 | 数量|
|----|------|------|-----|
|andromo| [http://andromo.com]() | [store:googleplay cert:C262A97FE5596C49A9560F0964D0408881EE5A982ED4B9BDFDD7F731EE8DA408](https://www.appinner.com/main/search?q=store:googleplay cert:C262A97FE5596C49A9560F0964D0408881EE5A982ED4B9BDFDD7F731EE8DA408) | 15699 |
|biznessapps|[https://www.biznessapps.com]()|[store:googleplay  cert:FDA9F9E77A33FFC6C51E1AEE76C894E173F23981A0BFA1621D706010B5D5BCC3](https://www.appinner.com/main/search?q=store:googleplay  cert:FDA9F9E77A33FFC6C51E1AEE76C894E173F23981A0BFA1621D706010B5D5BCC3)|13547
|como|[http://www.como.com/]()|[store:googleplay cert:AEDF00DFD06A4EC28CCD3E0F62AC323D1B057A2643D500CB26AC7D1AD68583B9](https://www.appinner.com/main/search?q=store:googleplay cert:AEDF00DFD06A4EC28CCD3E0F62AC323D1B057A2643D500CB26AC7D1AD68583B9)|5817
|mobincube|[http://www.mobincube.com/]()|[store:googleplay cert:A54E5071DD54EC05DB57390F33E384037D183505ECB20383D20FF32729A1FDF5](https://www.appinner.com/main/search?q=store:googleplay cert:A54E5071DD54EC05DB57390F33E384037D183505ECB20383D20FF32729A1FDF5) |3519
|gamesalad|[http://gamesalad.com/]()|[store:googleplay  activity:com.gamesalad.player.GSGameWrapperActivity](https://www.appinner.com/main/search?q=store:googleplay  activity:com.gamesalad.player.GSGameWrapperActivity) |3208
|goodbarber|[http://goodbarber.com]()|[store:googleplay cert:'CN=GoodBarber, OU=GoodBarber, O=GoodBarber, L=Ajaccio, ST=Corsica, C=FR'](https://www.appinner.com/main/search?q=store:googleplay%20cert:%27CN=GoodBarber,%20OU=GoodBarber,%20O=GoodBarber,%20L=Ajaccio,%20ST=Corsica,%20C=FR%27)|2654
|appmk|[http://www.appmk.com/]()|[store:googleplay cert:'CN="appmk OU =  O =  L =  ST =  C ="'](https://www.appinner.com/main/search?q=cert:%27CN="appmk%20OU%20=%20%20O%20=%20%20L%20=%20%20ST%20=%20%20C%20="%27%20store:googleplay) |2164
|shoutem|[http://shoutem.com]()|[store:googleplay cert:'3ED6FFBE447B6E39D7FF0DD7B732B885502C9817743D95C5FF4C4C19C7A83449'](https://www.appinner.com/main/search?q=store:googleplay cert:3ED6FFBE447B6E39D7FF0DD7B732B885502C9817743D95C5FF4C4C19C7A83449) |1078
|appmachine|[http://www.appmachine.com]()|[store:googleplay cert:'CN=AppMachine B.V., OU=AppMachine B.V., O=AppMachine B.V., L=Heerenveen, ST=Friesland, C=NL'](https://www.appinner.com/main/search?q=store:googleplay%20cert:%27CN=AppMachine%20B.V.,%20OU=AppMachine%20B.V.,%20O=AppMachine%20B.V.,%20L=Heerenveen,%20ST=Friesland,%20C=NL%27) |1072
|doubledutch|[http://doubledutch.me]()|[store:googleplay cert:19509AA81D9FFFF0BA768081F93F5144F7FFC17681A5E634D8FD38DC46811BD0](https://www.appinner.com/main/search?q=store:googleplay cert:19509AA81D9FFFF0BA768081F93F5144F7FFC17681A5E634D8FD38DC46811BD0) |775
|appyourself|[http://appyourself.net]()|[store:googleplay (package:net.ays OR cert:'58F7E8877F8B2293F2487F8CC950436702774CCBBF13E4B54E4B640E2EECFB5F')](https://www.appinner.com/main/search?q=store:googleplay (package:net.ays OR cert:58F7E8877F8B2293F2487F8CC950436702774CCBBF13E4B54E4B640E2EECFB5F))|585
|mindbodyonline|[https://www.mindbodyonline.com]()|[store:googleplay package:com.fitnessmobileapps](https://www.appinner.com/main/search?q=store:googleplay package:com.fitnessmobileapps)|505
|appsbuilder|[http://www.apps-builder.com]()|[store:googleplay cert:'3FE3C632E9056FE216FBD32AA8EFC7EAD07D6C7575F0173356B2CE562EC6FA62'](https://www.appinner.com/main/search?q=store:googleplay cert:3FE3C632E9056FE216FBD32AA8EFC7EAD07D6C7575F0173356B2CE562EC6FA62)|504
|buildfire|[http://buildfire.com]()|[store:googleplay cert:2F79244FDCAE40577158705DE6F54F70BA26EF38DFF0D93D1AA8BD29B23F1FAB](https://www.appinner.com/main/search?q=store:googleplay cert:2F79244FDCAE40577158705DE6F54F70BA26EF38DFF0D93D1AA8BD29B23F1FAB)|502
|appmakr|[http://www.appmakr.com]()|[store:googleplay package:com.appmakr](https://www.appinner.com/main/search?q=store:googleplay package:com.appmakr)|482
|attendify|https://attendify.com/|[store:googleplay  cert:F717C51513F8CAE219CC5EB18F45E96AE11C8695DB871EBF6BC7B767B1CF195E](https://www.appinner.com/main/search?q=store:googleplay  cert:F717C51513F8CAE219CC5EB18F45E96AE11C8695DB871EBF6BC7B767B1CF195E)|337
|mobileroadie|[http://www.mobileroadie.com]()|[store:googleplay cert:'4C60928082698D59DBCE664BC6519A553C8D705D3D80CB205CF9622551B28488'](https://www.appinner.com/main/search?q=store:googleplay cert:'4C60928082698D59DBCE664BC6519A553C8D705D3D80CB205CF9622551B28488') |318
|appypie|[http://www.appypie.com]()|[store:googleplay package:com.appypie](https://www.appinner.com/main/search?q=store:googleplay package:com.appypie)|304
|appery|[https://appery.io]()|[store:googleplay package:io.appery](https://www.appinner.com/main/search?q=store:googleplay package:io.appery)|182
|mobappcreator|[http://www.mobappcreator.com]()|[store:googleplay activity:com.defconsolutions.mobappcreator](https://www.appinner.com/main/search?q=store:googleplay activity:com.defconsolutions.mobappcreator) |116

> AppInner 的数据本身在增长,因此后续看到的数据肯定是变化了。

可以看到, 各平台的搜索词有差异,主要是3类:

1. 证书 : 14个平台都使用了唯一的证书或证书属性一致
2. 包名 : 4个平台的应用都以特定的包名开头
3. activity: 2个平台应用包含特定的activity

对上述数据绘制统计图:

![platform_1]({filename}/images/no_code_platform_1.png)
![platform_2]({filename}/images/no_code_platform_2.png)

看来这个市场也已经趋于集中, Andromo + biznessapps 在20个厂商中占有超过了 *50%*, 加上 como 已经超过 *60%*。

## 03 总结

以上利用 AppInner 对 Andromo 等在线生成App平台在GooglePlay中实际的情况进行了下简单的统计, 时间有限, 没有进一步深入分析。 比如 gamesalad 虽然看上去占有率不高,但是其在游戏领域绝对是第一。有兴趣或有需要的同学可以对相关数据更深入的分析。
