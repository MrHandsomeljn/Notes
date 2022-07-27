## wsl莫名其妙连不上网

方法1

```powershell
wsl --shutdown
netsh winsock reset
netsh int ip reset all
netsh winhttp reset proxy
ipconfig /flushdns
wsl
```

方法2（未完待续）