## 向校园网服务器快速上传文件

> 正常情况能上60-80MB/s

1. 上传文件至[奶牛快传](https://cowtransfer.com)
2. [直链解析](https://api.kit9.cn/api/nainiu/nainiu.php)分享链接
3. 复制得到的"downloadlink"
4. 服务器上wget这个downloadlink，建议链接用引号括起来，避免链接识别问题