## 缺少组策略管理器

下载[gpedit-enabler.bat](./files/gpedit-enabler.bat)并运行

即可在win+R中运行gpedit.msc/secpol.msc等程序

附：.bat代码

```bat
@echo off 

pushd "%~dp0" 

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt 

dir /b %SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt 

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i" 

pause
```

