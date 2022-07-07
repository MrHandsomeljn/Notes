## 小学期LoongArch-Linux交叉编译实验记录

#### 简介

实验主要参考：[foxsen/qemu-loongarch-runenv](https://github.com/foxsen/qemu-loongarch-runenv)

在Ubuntu20.04下进行，实验过程主要为

1. 安装Ubuntu20.04
2. 下载qemu-loongarch-runenv
3. 下载gcc [ToolChain](https://github.com/foxsen/qemu-loongarch-runenv/releases/download/toolchain/loongarch64-clfs-2021-12-18-cross-tools-gcc-full.tar.xz)
4. 下载Linux支持LoongArch的版本，使用以上gcc进行编译
5. 将编译完成的vmlinux挂载入QEMU，即可模拟在龙芯平台运行Linux
6. *更改Linux源代码，使加载过程可以显示编译者个人信息

#### 过程

```sh
#下载qemu
	cd ~/Codes
	git clone https://github.com/foxsen/qemu-loongarch-runenv.git
#测试qemu
	cd qemu-loongarch-runenv
	./qemu-system-loongarch64	#此时应出现qemu程序，最终出现qemu虚拟机的shell输入框，可模拟正常linux交互

#下载交叉编译工具
	cd /opt
	wget https://github.com/foxsen/qemu-loongarch-runenv/releases/download/toolchain/loongarch64-clfs-2021-12-18-cross-tools-gcc-full.tar.xz
	tar -xf loongarch64-clfs-2021-12-18-cross-tools-gcc-full.tar.xz
	
```



#### 报错及解决方法

##### 编译缺少文件类

1. 缺少libncursesw.so6

   使用Ubuntu18.04时会出现此问题，使用20.04则不会

2. 

3. 