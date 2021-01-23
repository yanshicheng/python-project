# websocket
## 简介
```bash
websocket
	web: 网站，可以让浏览器和服务端进行交互。
	socket： 让网络两端创建连接病进行收发数据
```

## 协议

```bash
http： 无状态短连接网络协议。
https： 无状态，加密的短连接网络协议。
websocket： 默认不断开连接。
```



# channels==2.3

## 安装

`pip install channels`

## 简介

 在 channels 内部已经写好了握手，加密，解密等环节。

- django
  - 默认不支持
  - 第三方： channels
- flask
  - 默认不支持
  - 第三方： geventwebsocket
- tornado
  - 默认支持





