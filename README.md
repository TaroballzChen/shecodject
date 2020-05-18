# shecodject (shellcode inject)
shecodject is a autoscript for shellcode injection by Python3 programing

Shecodject為shellcode inject的縮寫，是一個由python3編寫的工具，可將客製metasploit生成的raw檔直接使用pyinstaller封裝或是您也可使用本工具生成普通的raw檔再進行封裝。

使用ctypes模塊將shellcode注入到ram中，類似於客製shellcode的python自動化程序

近期(2020年04月)修改了封裝exe的模組，借用docker提供的pyinstaller鏡像完成封裝exe的工作，不再使用wine進行封裝。且不用擔心在Linux或是Mac系統下無法完成封裝exe

obf shellcode混淆模塊目前還在修復中

![image](https://i.imgur.com/Xa5FpYu.png)

# Basic Flow
* Method 1
	1. mpr 模塊產生普通raw檔
	2. exe 模塊封裝
		* 產生exe檔於output目錄下
	3. msf 模塊監聽
* Method 2
	1. msfvenom 產生raw檔
	2. scc 模塊引入raw檔
	3. exe 模塊封裝
		* 產生exe檔於output目錄下
	4. msf 模塊監聽

# Installation 

```
$ git clone https://github.com/TaroballzChen/Shecodject.git
$ cd Shecodject
$ cd setup
$ python3 setup.py
```

# Usage
```
$ python3 shecodeject.py
```
[![My video](http://i2.hdslb.com/bfs/archive/c3769df6013330e83c91b3954cc9306985f367da.jpg)](https://www.youtube.com/watch?v=0OFQ1fVopms)

# Reference
* https://github.com/TaroballzChen/shellcodeinject_regwrite_persistence/blob/master/reg_shellcode.py
* https://github.com/Mr-Un1k0d3r/DKMC
