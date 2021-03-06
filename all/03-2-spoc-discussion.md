# lec6 SPOC思考题


NOTICE
- 有"w3l2"标记的题是助教要提交到学堂在线上的。
- 有"w3l2"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

（1） (w3l2) 请简要分析64bit CPU体系结构下的分页机制是如何实现的
```
  + 采分点：说明64bit CPU架构的分页机制的大致特点和页表执行过程
  - 答案没有涉及如下3点；（0分）
  - 正确描述了64bit CPU支持的物理内存大小限制（1分）
  - 正确描述了64bit CPU下的多级页表的级数和多级页表的结构或反置页表的结构（2分）
  - 除上述两点外，进一步描述了在多级页表或反置页表下的虚拟地址-->物理地址的映射过程（3分）
 ```
- [x]  
- 64bit的CPU的物理内存大小的限制是1.68*10^7T，CPU的多级页表的级数根据页表的大小以及页表项的大小进行判定，32bit的CPU一般两级页表，64bit的多级页表就需要三级页表或者更多级。在多级页表下，当得到当前的虚拟地址，CPU会从中得到每一级页表查询的偏置量。第一级页表的地址由PDBR和偏置相加得到，从中查询到第二级页表的起始地址，和第二个偏置相加得到第二级页表的表项，依次类推，最后一级页表中的内容移位后和偏移相加得到最终的物理地址。在64位系统中也通常会使用反置页表，每个物理页帧对应一个表项，当得到虚拟地址后，通过计算hash值找到页表中的表项，并和所有冲突项中的虚拟地址对比，如果相同则得到对应物理地址。
>  

## 小组思考题
---

（1）(spoc) 某系统使用请求分页存储管理，若页在内存中，满足一个内存请求需要150ns (10^-9s)。若缺页率是10%，为使有效访问时间达到0.5us(10^-6s),求不在内存的页面的平均访问时间。请给出计算步骤。 

- [x]  
- 根据公式 500= 0.9\*150 + 0.1\*x，解得平均访问时间为3650ns，即3.65ms。
> 500=0.9\*150+0.1\*x

（2）(spoc) 有一台假想的计算机，页大小（page size）为32 Bytes，支持32KB的虚拟地址空间（virtual address space）,有4KB的物理内存空间（physical memory），采用二级页表，一个页目录项（page directory entry ，PDE）大小为1 Byte,一个页表项（page-table entries
PTEs）大小为1 Byte，1个页目录表大小为32 Bytes，1个页表大小为32 Bytes。页目录基址寄存器（page directory base register，PDBR）保存了页目录表的物理地址（按页对齐）。

PTE格式（8 bit） :
```
  VALID | PFN6 ... PFN0
```
PDE格式（8 bit） :
```
  VALID | PT6 ... PT0
```
其
```
VALID==1表示，表示映射存在；VALID==0表示，表示映射不存在。
PFN6..0:页帧号
PT6..0:页表的物理基址>>5
```
在[物理内存模拟数据文件](./03-2-spoc-testdata.md)中，给出了4KB物理内存空间的值，请回答下列虚地址是否有合法对应的物理内存，请给出对应的pde index, pde contents, pte index, pte contents。
```
Virtual Address 6c74
Virtual Address 6b22
Virtual Address 03df
Virtual Address 69dc
Virtual Address 317a
Virtual Address 4546
Virtual Address 2c03
Virtual Address 7fd7
Virtual Address 390e
Virtual Address 748b
```

运行程序[addr.py](./03-02-addr.py)得到本题答案：
```
Virtual Address 6c74:
  --> pde index:0x1b  pde contents:(valid 1, pfn 0x20)
    --> pte index:0x3  pte content:(valid 1, pfn 0x61)
      --> Translate to Physical Address 0xc34 --> Value: 0x6
      
Virtual Address 6b22:
  --> pde index:0x1a  pde contents:(valid 1, pfn 0x52)
    --> pte index:0x19  pte content:(valid 1, pfn 0x47)
      --> Translate to Physical Address 0x8e2 --> Value: 0x1a
      
Virtual Address 03df:
  --> pde index:0x0  pde contents:(valid 1, pfn 0x5a)
    --> pte index:0x1e  pte content:(valid 1, pfn 0x5)
      --> Translate to Physical Address 0xbf --> Value: 0xf
      
Virtual Address 69dc:
  --> pde index:0x1a  pde contents:(valid 1, pfn 0x52)
    --> pte index:0xe  pte content:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
      
Virtual Address 317a:
  --> pde index:0xc  pde contents:(valid 1, pfn 0x18)
    --> pte index:0xb  pte content:(valid 1, pfn 0x35)
      --> Translate to Physical Address 0x6ba --> Value: 0x1e
      
Virtual Address 4546:
  --> pde index:0x11  pde contents:(valid 1, pfn 0x21)
    --> pte index:0xa  pte content:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
      
Virtual Address 2c03:
  --> pde index:0xb  pde contents:(valid 1, pfn 0x44)
    --> pte index:0x0  pte content:(valid 1, pfn 0x57)
      --> Translate to Physical Address 0xae3 --> Value: 0x16
      
Virtual Address 7fd7:
  --> pde index:0x1f  pde contents:(valid 1, pfn 0x12)
    --> pte index:0x1e  pte content:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
      
Virtual Address 390e:
  --> pde index:0xe  pde contents:(valid 0, pfn 0x7f)
      --> Fault (page directory entry not valid)
      
Virtual Address 748b:
  --> pde index:0x1d  pde contents:(valid 1, pfn 0x0)
    --> pte index:0x4  pte content:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
```


（3）请基于你对原理课二级页表的理解，并参考Lab2建页表的过程，设计一个应用程序（可基于python, ruby, C, C++，LISP等）可模拟实现(2)题中描述的抽象OS，可正确完成二级页表转换。


（4）假设你有一台支持[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)的机器，请问你如何设计操作系统支持这种类型计算机？请给出设计方案。

 (5)[X86的页面结构](http://os.cs.tsinghua.edu.cn/oscourse/OS2015/lecture06#head-1f58ea81c046bd27b196ea2c366d0a2063b304ab)
--- 

## 扩展思考题

阅读64bit IBM Powerpc CPU架构是如何实现[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)，给出分析报告。

--- 
