## Anaconda安装源

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

几个推荐的源

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

> about link
>
> 1. [Anaconda安装、使用-ubuntu](anaconda-%E5%AE%89%E8%A3%85%26%E4%BD%BF%E7%94%A8-ubuntu.md)
