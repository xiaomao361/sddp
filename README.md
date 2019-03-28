sentry ding ding plugin
===

进入sentry目录

1. vim requirements.txt

添加下面内容

```
redis-py-cluster==1.3.4
sddp==0.1.7
```

2. 构建并重启sentry

`sudo docker-compose build`

`sudo docker-compose down`

`sudo docker-compose up -d`

