#lec 3 SPOC Discussion

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。
 2. BIOS是固化到主板上的程序，UEFI是在所有平台上一致的操作系统服务。
 1. 描述PXE的大致启动流程。
 2. PXE大致启动流程：设备发送DHCPDISCOVER给DHCP server和 ADS PXE service，DHCP server

    给设备提供IP地址，ADS PXE service忽略这条信息或者相应DHCPOFFER IP地址。设备发送

    DHCPREQUEST给DHCP server，DHCP server返回DHCPPACK。如果之前ADS PXE service有响应，

    设备发出DHCPREQUEST启动程序给ADS PXE service,ADS PXE service返回DHPACK启动程序路径

    ，TFTP获得STARTNBS启动镜像请求，TFTP发送STARTNBS启动镜像。SRARTNBS发送PXE开机指令

    请求给Controller service，Controller service返回/pxe/boot-vf，PXE启动。
## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
 2. NTLDR启动流程：访问引导驱动器上的文件系统，如果windows系统处于休眠状态，

    hiberfil.sys会加载到内存，系统从它离开的地方恢复，如果选择了一个不是基于NT的操作系

    统，NTLDR会加载在boot.ini的相关文件，并给它控制；如果选择了一个基于NT的操作系统，

    NTLDR会运行ntdetectc.com以获取计算机上的硬件信息，开始运行Ntoskrnl.exe，传递给他

    ntdetect.com返回的信息。
 1. 了解GRUB的启动流程。
 1. 比较NTLDR和GRUB的功能有差异。
 1. 了解u-boot的功能。

## 3.3 中断、异常和系统调用比较
 1. 举例说明Linux中有哪些中断，哪些异常？
 1. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)
 1. Linux系统调用指令有大约400个，主要功能分类有进程控制，文件系统控制，系统控制，内存管理，网络管理，socket控制，用户管理，进程间通信。
```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 1. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 1. ucore的系统调用有22个,SYS_exit,SYS_fork等，大致功能分类有进程管理(sys_exit, sys_fork, sys_wait, sys_exec,        sys_yield, sys_getpid, sys_pgdir, sys_lab6_set_priority, sys_sleep)，文件系统控制(sys_open, sys_close, sys_read, sys_write, sys_seek, sys_fstat, sys_fync, sys_dup, sys_putc)，系统控制(sys_gettime, sys_getcwd, sys_getdirentry), 进程间通信（sys_kill）。
 
 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 objdump：显示目标文件中的详细信息，nm：列出目标文件中的符号，file：检测文件类型，lab1_ex0实现了sys_write系统调用，在%eax,%ebx,%ecx,%edx寄存器中分别赋值$SYS_write（4）, $STDOUT（1）, $hello, $12(hello字符串长度)，通过int $0x80进行系统调用。

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 1. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)
 stace：跟踪进程执行时的系统调用和所接收的信号。

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。
 1. ucore的系统调用中返回结果的传递代码分析。
 1. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。
 1. 以ucore lab8的answer为例，尝试修改并运行代码，分析ucore应用的系统调用执行过程。
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
   1. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 
