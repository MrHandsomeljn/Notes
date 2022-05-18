## Anaconda源相关

查看现有安装源

```sh
conda config --show-sources
```

添加安装源

```sh
conda config --add channels [源]
```

删除某个安装源

```sh
conda config --remove channels [源]
```

切换回默认源

```sh
conda config --remove-key channels
```

设置搜索时显示通道地址

```sh
conda config --set show_channel_urls yes
```

安装时指定源

```sh
conda install -c [源] [包名]
```

推荐源

```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

