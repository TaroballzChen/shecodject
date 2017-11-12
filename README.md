# shecodject (shellcode inject)
shecodject is a autoscript for shellcode injection by Python3 programing

shecoject是一個由python3編寫的工具，可將客製metasploit生成的raw檔直接使用pyinstaller封裝或是您也可使用本工具生成普通的raw檔再進行封裝。

使用ctypes模塊將shellcode注入到ram中

persistence的方法為利用python3的winreg模塊於註冊表中寫入開機執行本程序並自我複製到使用者客製的路徑

![image](https://i.imgur.com/Xa5FpYu.png)

且本工具亦提供shellcode混淆模塊將普通的reverse_tcp混淆(摘取自kgretzky作者)
# Basic Flow
* Example 1
	* msfvenom 產生raw檔
	* scc 引入raw檔
	* exe 模塊封裝
	* msf 模塊監聽
* Example 2
	* mpr 模塊產生普通raw檔
	* exe 模塊封裝
	* msf 模塊監聽
* Example 3
	* mpr 模塊產生普通reverse_tcp的raw檔
	* obf 模塊混淆
	* exe 模塊封裝
	* msf 模塊監聽	
	
# Requirements 
python2 (obf module) 

python3

# Installation 
```
$ git clone https://github.com/curtis992250/shecodject.git
$ python3 setup.py
```
# Usage
```
$ python3 shecodeject.py
```
# Reference
* https://github.com/curtis992250/shellcodeinject_regwrite_persistence/blob/master/reg_shellcode.py
* https://github.com/Mr-Un1k0d3r/DKMC
* https://www.youtube.com/watch?v=rjKEoBfdboo
* https://www.youtube.com/watch?v=w4BuXu344mU&t=638s
