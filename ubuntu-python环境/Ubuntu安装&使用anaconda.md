## ubuntu安装/使用anaconda

anaconda安装：

- 有su权限
  - 没啥好说的
- 无su权限

  ```sh
  #1. 下载Anaconda3-xxxx.xx-Linux-x86_64.sh
  #2. 运行
  bash Anaconda3-xxxx.xx-Linux-x86_64.sh
  #3. 若发现conda: command not found
  vim ~/.bashrc
  #i输入模式
  export PATH="/xxx/anaconda3/bin:$PATH"
  #:wq保存并退出
  #刷新bashrc
  . ~/.bashrc
  ```

查看conda安装位置

```sh
conda info --envs
```

创建环境

```sh
conda create -n [环境名]
```

打开环境

```sh
conda activate [环境名]
```

环境迁移

```sh
#本地操作
conda activate [源环境]
conda env export > [新环境].yaml
#文件传送完成后，到另一台机器上
conda env create -f [新环境].yaml
#此时pip安装的包没有移植，需要单独操作
#本地操作
pip freeze > requirements.txt
#另一台机器上
pip install -r requirements.txt
```

或者直接打包环境文件夹，发送到服务器上解包

```sh
conda info --envs	#查看包位置
tar -cvf [] #打包
#传输打包好的文件
tar -xvf []	#解包
```

> about link
> 1. [Anaconda源相关](Anaconda源相关.md)