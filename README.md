
[sentry-onpremise](https://github.com/getsentry/onpremise)使用的钉钉插件

进入sentry目录

1. vim requirements.txt

添加下面内容

```
sddp==0.2.6
```

2. 构建并重启sentry

`sudo docker-compose build`

`sudo docker-compose down`

`sudo docker-compose up -d`

~~更新测试了部分内容，适应sentry 20.8.0 版本，9.0版本请使用 sddp==0.1.7~~

*更新了插件版本到0.2.6，适应sentry21.2.0版本*

**更新了一个版本用以同时支持企业微信，但是只在23.3.1版本测试过，链接地址[csnp](https://github.com/xiaomao361/csnp)**

