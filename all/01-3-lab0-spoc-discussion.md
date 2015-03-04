# lab0 SPOC思考题

## 个人思考题

---

能否读懂ucore中的AT&T格式的X86-32汇编语言？请列出你不理解的汇编语言。
- [x]  
能读懂一部分，AT&T与Intel不同之处可能不太理解。
>  http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm

虽然学过计算机原理和x86汇编（根据THU-CS的课程设置），但对ucore中涉及的哪些硬件设计或功能细节不够了解？
- [x]  
寄存器的使用方法，不同机制的转换
>   


哪些困难（请分优先级）会阻碍你自主完成lab实验？
- [x]  
部分代码过于晦涩可能会影响。
>   

如何把一个在gdb中或执行过程中出现的物理/线性地址与你写的代码源码位置对应起来？
- [x]  
用gdb中的list指令。
>   

了解函数调用栈对lab实验有何帮助？
- [x]  
有利于理解内存分配问题
>   

你希望从lab中学到什么知识？
- [x]  
学到操作系统的实现细节，进一步提高自己的编程能力。
>   

---

## 小组讨论题

---

搭建好实验环境，请描述碰到的困难和解决的过程。
- [x]  
我采用的是虚拟机+老师给的虚拟硬盘配置的实验环境。由于以前一直使用虚拟机ubuntu系统，没有遇到明显的问题。
> 

熟悉基本的git命令行操作命令，从github上的[ucore git repo](http://www.github.com/chyyuu/ucore_lab)下载ucore lab实验
- [x]  
http://www.cnblogs.com/cspku/articles/Git_cmds.html
> 

尝试用qemu+gdb（or ECLIPSE-CDT）调试lab1
- [x]  
使用了ECLIPSE-CDT调试lab1
> 

对于如下的代码段，请说明”：“后面的数字是什么含义
```
/* Gate descriptors for interrupts and traps */
struct gatedesc {
    unsigned gd_off_15_0 : 16;        // low 16 bits of offset in segment
    unsigned gd_ss : 16;            // segment selector
    unsigned gd_args : 5;            // # args, 0 for interrupt/trap gates
    unsigned gd_rsv1 : 3;            // reserved(should be zero I guess)
    unsigned gd_type : 4;            // type(STS_{TG,IG32,TG32})
    unsigned gd_s : 1;                // must be 0 (system)
    unsigned gd_dpl : 2;            // descriptor(meaning new) privilege level
    unsigned gd_p : 1;                // Present
    unsigned gd_off_31_16 : 16;        // high bits of offset in segment
};
```
- [x]  
“：”后面的数字定义了位域的宽度，表示这个变量占用的位数。
> 

对于如下的代码段，
```
#define SETGATE(gate, istrap, sel, off, dpl) {            \
    (gate).gd_off_15_0 = (uint32_t)(off) & 0xffff;        \
    (gate).gd_ss = (sel);                                \
    (gate).gd_args = 0;                                    \
    (gate).gd_rsv1 = 0;                                    \
    (gate).gd_type = (istrap) ? STS_TG32 : STS_IG32;    \
    (gate).gd_s = 0;                                    \
    (gate).gd_dpl = (dpl);                                \
    (gate).gd_p = 1;                                    \
    (gate).gd_off_31_16 = (uint32_t)(off) >> 16;        \
}
```
如果在其他代码段中有如下语句，
```
unsigned intr;
intr=8;
SETGATE(intr, 0,1,2,3);
```
请问执行上述指令后， intr的值是多少？
- [x]  
65538
> 

请分析 [list.h](https://github.com/chyyuu/ucore_lab/blob/master/labcodes/lab2/libs/list.h)内容中大致的含义，并能include这个文件，利用其结构和功能编写一个数据结构链表操作的小C程序
- [x]  
- list.h实现了双向链表，其中的函数大概功能如下：
list_enrty:没有传统的数据域，包含链表结点；
list_init:初始化链表，指针都指向自己；
list_add_before:表尾插入；
list_add_after:表头插入；
list_add:等于list_add_after；
list_del:删除空闲链表结点，将结点指向自身，呈空链状态；
小C程序如下（链表没有数据域）：
> 
```
#include "list.h"
#include <cstdio>
int main() {
    list_entry *a = new list_entry();
    list_entry *b = new list_entry();
    list_entry *c = new list_entry();
    list_init(a);
    list_add(a, b);
    list_add_before(a, c);
    list_del(c);
    list_del_init(b);
    return 0;
}
```
> 

---

## 开放思考题

---

是否愿意挑战大实验（大实验内容来源于你的想法或老师列好的题目，需要与老师协商确定，需完成基本lab，但可不参加闭卷考试），如果有，可直接给老师email或课后面谈。
- [x]  

>  

---
