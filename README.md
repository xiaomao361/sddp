sentry ding ding plugin
===

进入sentry目录

1. vim requirements.txt

添加下面内容

```
sddp=0.2.4
```

2. 构建并重启sentry

`sudo docker-compose build`

`sudo docker-compose down`

`sudo docker-compose up -d`

**更新测试了部分内容，适应sentry 20.8.0 版本，9.0版本请使用 sddp==0.1.7 **
