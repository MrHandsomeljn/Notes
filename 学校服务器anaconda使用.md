## 学校服务器anaconda使用

说明：适用于北京交通大学学校GPU服务器，服务器每周更新时会把用户文件夹清空，安装的软件也会清空，因而需要每周安装一次anaconda；校园网上传下载速度不是特别快，新create一个env也很慢，所以选用本地的anaconda安装包和env pack

#### 安装anaconda：

```sh
cd /opt/data/private/dachuang2022/diguang/
sh Anaconda3-2021.11-Linux-x86_64.sh
source ~/.bashrc
```

#### 安装env：

```sh
mkdir /root/anaconda3/envs/py36torch
cd /opt/data/private/dachuang2022/diguang/
tar -xzvf py36torch.tar.gz -C /root/anaconda3/envs/py36torch/
pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```

#### 必要时保存env，下次直接装

```sh
cd /opt/data/private/dachuang2022/diguang/
conda pack -n py36torch -o py36torch.tar.gz
```

