# 操作系统概述思考题

## 个人思考题

---

分析你所认识的操作系统（Windows、Linux、FreeBSD、Android、iOS）所具有的独特和共性的功能？
- [x]  
我认识的操作系统Windows和Linux，Windows，使用图形用户接口，具有易用性；linux系统开放，使用命令行接口。功能上的共性是都是协调用户和硬件的中间层，使用户可以方便的使用计算机中的资源。
>  

请总结你认为操作系统应该具有的特征有什么？并对其特征进行简要阐述。
- [x]  
操作系统都应该具有内核和接口（Shell或者GUI），应该是计算机的核心软件。内核应该具有并发、共享、虚拟、异步的特点。并发：操作系统中同时运行多个程序，需要OS的管理和调度；共享：多个应用同时和运行，宏观上要体现同时访问资源的情况，微观上要实现互斥访问；虚拟：用多道程序设计技术，让每个用户觉得有一个计算机专门为他提供服务；异步：程序的执行是走走停停的，向前推进的速度不可预知，但只要环境相同，OS需要保证程序运行的结果相同。
>   

请给出你觉得的更准确的操作系统的定义？
- [x]  
操作系统是管理计算机硬件资源的，并给用户提供访问硬件资源手段的，能比较好的解决资源访问冲突并且维持比较好的公平性的，程序与资源之间的中间层。
>   

你希望从操作系统课学到什么知识？
- [x]  
我往从操作系统课程中学到编写计算机操作系统的具体知识和技巧。
>   

---

## 小组讨论题

---

目前的台式PC机标准配置和价格？
- [x]  
目前PC机子的标配
CPU:Intel Core i5-Quad Core；
内存:4GB；
Processor Speed:3.20GHz-Turbo to 3.6；
显示器：20"LED Flat Panel 1600*900；
显卡：Intel HD 4600 Dual Monitor Capable；
硬盘：500GB ；
价格：$749 ￥4698
> 

你理解的命令行接口和GUI接口具有哪些共性和不同的特征？
- [x]  
GUI和Shell(CLI)比较
CLI比较难上手，对用户难度较大，GUI由于用图形化接口，比较直观，好上手；
CLI对文件和操作系统控制性更强，比如从一个地方把文件拷贝到另一个地方只需要一行，GUI提供大量的接口，但对比较高级的操作，不如CLI;
CLI只需要使用键盘，GUI需要使用鼠标+键盘，一般情况下，CLI比GUI更快；
CLI占用较少的系统资源，GUI占用较多的系统资源，因为需要加载很多如按钮之类的其他东西；
CLI可以很简单的用指令直接运行程序或者开始进程，GUI相比较CLI可获取的资源少一些；
CLI可以比较容易做到远程操作，部分GUI不支持远程操作；
CLI比较单一，简洁，GUI种类繁多，比较复杂；
CLI可以让手一直停留在键盘完成所有操作，GUI即使有快捷键也不可避免用到鼠标；
共同点都是为用户提供接口，使用计算机系统资源
> 

为什么现在的操作系统基本上用C语言来实现？
- [x]  
因为目前所有语言的开发环境里，C语言能做到编译成不依赖操作系统的形式二进制代码，C语言的各种脱离系统的库最丰富，最完整，C语言用来开发操作系统的工具最多。
语言运行所依赖的东西决定了C语言在现今是比较适合写操作系统的语言。
>  

为什么没有人用python，java来实现操作系统？
- [x]  
操作系统有一个很重要的功能是内存管理，Java,Python之类的不能直接操纵内存的语言要做内存管理是很困难的事情。不过有人确实用Java写过操作系统（JNode），链接： http://zh.wikipedia.org/wiki/JNode 。
不过他的内存管理部分使用的是汇编写的，相当一部分代码需要使用L2编译器编译，编译出来的是X86原生代码，不是JVM的bytecode，有点蛋疼。
>  

请评价用C++来实现操作系统的利弊？
- [x]  
可以把操作系统看做一个多层结构，C++适合比较高层的编写，不太适合比较底层的编写。C++需要运行时刻库来实现很多功能（比如异常处理），比较底层的时候可能无法用到运行时刻库，C在这时就显得比较合适。
不过比较高层的服务，比较抽象的系统服务，运行时刻库可以获取到的情况下，C++这类高级语言就更加合适，Windows中就有很多部分用C++编写。
>  

---

## 开放思考题

---

请评价微内核、单体内核、外核（exo-kernel）架构的操作系统的利弊？
- [x]  
单体内核架构是一个大处理器完全在一个地址空间中跑，内核是一个静态二进制文件。所有内核服务在内核地址空间中存在和执行，内核可以直接调用函数，这种类型的操作系统有：Linux，Unix。
微内核架构中，内核被分成多个独立进程，即服务，所有服务独立存在，并在不同的地址空间跑，不同服务之间通过IPC交流信息，服务实现功能通过发送请求，这样做的优点是一个服务失效了其余的仍可以有效的工作，这种类型的操作系统有：Windows NT。
单体内核架构出现的时间早于微内核架构，而且单体内核架构比较快不过比较大，单体内核的驱动放在内核空间，比较不安全，微内核架构中内核驱动放在用户空间，相对比较稳定。
微内核比较容易拓展，单体内核不太容易，微内核切换时比较慢。外核架构大大简化了微内核的信息传递，程序可以更加直接的跟硬件交流，内核简洁，只保证被请求的资源是空闲的。这样的外架结构中端到端的思想体现的很多。
>  

请评价用LISP,OCcaml, GO, D，RUST等实现操作系统的利弊？
- [x]  

>  

进程切换的可能实现思路？
- [x]  
在需要切换时，先保存上一个进程的状态，将保存有上个进程信息的数据结构（PCB），放到一个专门的地方，读取将要执行的这个进程的PCB，执行这个进程，根据优先级等信息选择将要运行的下个进程。
>  

计算机与终端间通过串口通信的可能实现思路？
- [x]  

>  

为什么微软的Windows没有在手机终端领域取得领先地位？
- [x]  
（这个问题是用来黑苹果的吧）WP设置繁复，手机上office编辑是个坑，更新慢，没有苹果传教传的好。
>  

你认为未来（10年内）的操作系统应该具有什么样的特征和功能？
- [x]  
未来的操作系统可以将部分功能放到服务器上实现，并能识别大量体感操作。
>  

---
