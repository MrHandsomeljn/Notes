## C语言-EasyX、EGE

EasyX可以作为简易图形库使用，但需要安装Visual Studio。Easy Graphic Engine可以大部分替代EasyX，且支持使用MinGW的开发环境。

主要参考了这篇 [配置教程](https://blog.csdn.net/qq272508839/article/details/104287255) ，搭建了vscode可用的EGE简易图形库

我的步骤：

> 1. 保证vscode可以正常编译运行C语言
> 2. 进入 [easy graphic engine](https://xege.org/) 官网下载EGE，建议下载版本为 [ege19.01_all](http://xege.org/download/ege19.01_all.7z)
> 3. 解压，把```include```文件夹和```lib/mingw64/lib/libgraphics.a```复制到 ```mingw64\x86_64-w64-mingw32``` 文件夹下对应目录（目录参考软件32/64位环境而异）
> 4. 打开工作目录下的```./.vscode/c_cpp_properties.json```，替换入以下内容
>
> *注意：所有mingw64路径换成你自己的，工作区源文件和exe也换成你自己的*
>
> ```json
> {
>     "configurations": [
>         {
>             "name": "Win32",
>             "includePath": [
>               "${workspaceFolder}/**",
>               "C:\\Program Files\\mingw64\\include\\**",
>               "C:\\Program Files\\mingw64\\x86_64-w64-mingw32\\include\\**"
>             ],
>             "defines": [
>               "_DEBUG",
>               "UNICODE",
>               "_UNICODE"
>             ],
>             "compilerPath": "C:\\Program Files\\mingw64\\bin\\gcc.exe",
>             "cStandard": "c11",
>             "cppStandard": "c++17",
>             "intelliSenseMode": "gcc-x64"
>         }
>     ],
>     "version": 4
> }
> ```
>
> 5. 打开tasks.json，替换入以下内容
>
> *注意：所有mingw64路径换成你自己的，工作区源文件和exe也换成你自己的*
>
> ```json
> {
>     "version": "2.0.0",
>     "tasks": [
>         {
>             "type": "shell",
>             "label": "build",
>             //找到自己mingw安装目录下的bin文件夹，一共有俩bin文件夹，找有g++.exe的那个
>             "command": "C:\\Program Files\\mingw64\\bin\\g++.exe",
>             "args": [
>                 "-g", "${file}",
>                 "-o", "${fileDirname}/../bin/${fileBasenameNoExtension}.exe",
> 
>                 "-lgraphics64",    //32位的可能要把64去掉，具体自己尝试
>                 "-luuid",
>                 "-lmsimg32",
>                 "-lgdi32",
>                 "-limm32",
>                 "-lole32",
>                 "-loleaut32"
>             ],
>             "options": {
>                 "cwd": "C:\\Program Files\\mingw64\\bin"
>             },
>             "problemMatcher": [
>                 "$gcc"
>             ],
>             "group": {
>                 "kind": "build",
>                 "isDefault": true
>             }
>         }
>     ]
> }
> ```
>
> 6. include进<graphics.h>，快乐地运行EGE啦！

问题：

> 1. 编译时出现了很多很多行include error或者之类的的报错
>
>    > 看看下载的版本是不是19.01
>
> 2. 没有c_cpp_properties.json，或者没有tasks.json
>
>    > 建议看vscode+minGW编译C语言相关的blog