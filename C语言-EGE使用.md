## C语言-EGE的使用

参考：[EGE基础：图像操作篇](https://blog.csdn.net/qq_39151563/article/details/104342530)

### 基础

- 图像对象
  - EGE表示图像使用的是```PIMAGE```，也就是```IMAGE```的指针

- 窗口

  - initgraph(width, height)或initgraph(width, height, index)，其中index含义如下：

    ```C
    INIT_DEFAULT	//普通窗口
    INIT_NOBORDER	//为无边框窗口
    INIT_CHILD		//为子窗口（需要使用attachHWND指定要依附的父窗口，此函数不另说明）
    INIT_TOPMOST	//使窗口总在最前
    INIT_RENDERMANUAL//手动更新标志，即调用delay_fps/delay_ms等会等待操作的函数时，会更新窗口，否则保持窗口内容，这是为了减少绘制，减少界面闪烁
    INIT_WITHLOGO	//使initgraph的时候显示开场动画logo，无index时默认开启
    INIT_NOFORCEEXIT//使关闭窗口的时候不强制退出程序，但窗口会消失，需要配合is_run函数
    INIT_UNICODE	//设置窗口为Unicode窗口，使用Unicode字符集
    INIT_ANIMATION	//是 INIT_DEFAULT, INIT_RENDERMANUAL和 INIT_NOFORCEEXIT 三个的组合，用于动画编写
    ```

### 文件

#### 读取

```c
#include <graphics.h>

int main()
{
	initgraph(640, 480, 0);
	
    //创建图片对象。newimage()必须在initgraph()之后
	PIMAGE pimg = newimage();//空图像；可传入宽高
	
    //读取，返回值为0时成功
    getimage(pimg, "pic.png");
	
    //free，防止内存泄漏
    delimage(pimg);
    
    //带透明通道
    getimage_withalpha(pimg, "pic.png");
	
    //绘制图像，(0, 0)是图片绘制区域的左上角，会改变pimg尺寸	
	putimage(0, 0, pimg);
	
	getch();
	closegraph();
	return 0;
}
```

> **不要多次getimage而不delimage，防止内存泄漏**

#### 保存

```c
saveimage(pimg, "a.bmp");	//保存为bmp
savepng(pimg, "a.png");		//保存为png
```

