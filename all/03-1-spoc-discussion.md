# lec5 SPOC思考题


NOTICE
- 有"w3l1"标记的题是助教要提交到学堂在线上的。
- 有"w3l1"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

请简要分析最优匹配，最差匹配，最先匹配，buddy systemm分配算法的优势和劣势，并尝试提出一种更有效的连续内存分配算法 (w3l1)
- 最优匹配：优点：容易实现，高地址分区空间大；缺点：存在外部碎片，分配速度越来越慢
- 最先分配：优点：分配尺寸较小时，可以减少外部碎片大小；缺点：释放分区缓慢，产生的小碎片难以利用
- 最差匹配：优点：分配尺寸中等时，利用率较高；缺点：释放分区缓慢，可能使大空闲分区难分配
- buddy system：优点：访问迅速，分配整齐；缺点：存在内部碎片
- 可以用线段树实现类似buddy system的内存分配，提高查找、分配效率
```
  + 采分点：说明四种算法的优点和缺点
  - 答案没有涉及如下3点；（0分）
  - 正确描述了二种分配算法的优势和劣势（1分）
  - 正确描述了四种分配算法的优势和劣势（2分）
  - 除上述两点外，进一步描述了一种更有效的分配算法（3分）
 ```
- [x]  

>  

## 小组思考题

请参考ucore lab2代码，采用`struct pmm_manager` 根据你的`学号 mod 4`的结果值，选择四种（0:最优匹配，1:最差匹配，2:最先匹配，3:buddy systemm）分配算法中的一种或多种，在应用程序层面(可以 用python,ruby,C++，C，LISP等高语言)来实现，给出你的设思路，并给出测试用例。 (spoc)
- 我的学号是2012011403，采用的是buudy system，采用的语言是C，实现了二叉树数据结构，进行内存分配，实现以及测试代码如下：
```
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <string.h>

struct buddy2{
	unsigned size;
	unsigned longest[1];
};

#define LEFT_LEAF(index) ((index) * 2 + 1)
#define RIGHT_LEAF(index) ((index) * 2 + 2)
#define PARENT(index) (((index) + 1) / 2 - 1)
#define IS_POWER_OF_2(x) (!((x)&((x)-1)))
#define MAX(a, b) ((a)>(b) ? (a):(b))
#define ALLOC malloc
#define FREE free

static unsigned fixsize(unsigned size){
	size |= size >> 1;
	size |= size >> 2;
	size |= size >> 4;
	size |= size >> 8;
	size |= size >> 16;
	return size+1;
}

struct buddy2* buddy2_new(int size){
	struct 	buddy2* self;
	unsigned node_size;
	int i;

	if(size < 1 || !IS_POWER_OF_2(size)){
		return NULL;
	}

	self = (struct buddy2*)ALLOC(2*size*sizeof(unsigned));
	self -> size = size;
	node_size = size * 2;

	for (i = 0; i < 2*size-1; ++i){
		if(IS_POWER_OF_2(i+1)){
			node_size /= 2;		
		}
		self->longest[i] = node_size;
	}
	return self;
}

void buddy2_destroy(struct buddy2* self){
	FREE(self);
}

int buddy2_alloc(struct buddy2* self, int size){
	unsigned index = 0;
	unsigned node_size;
	unsigned offset = 0;
	
	if (self == NULL){
		return -1;	
	}
	if (size <= 0){
		size = 1;	
	}
	else if (!IS_POWER_OF_2(size)){
		size = fixsize(size);	
	}
	
	if(self->longest[index] < size){
		return -1;
	}

	for (node_size = self->size; node_size != size; node_size /= 2){
		if (self->longest[LEFT_LEAF(index)] >= size){
			index = LEFT_LEAF(index);
		}
		else{
			index = RIGHT_LEAF(index);		
		}
	}
	
	self->longest[index] = 0;
	offset = (index+1) * node_size - self->size;	

	while(index) {
		index = PARENT(index);
		self->longest[index] = MAX(self->longest[LEFT_LEAF(index)], self->longest[RIGHT_LEAF(index)]);
	}
	
	return offset;
}

void buddy2_free(struct buddy2* self, int offset){
	unsigned node_size, index = 0;
	unsigned left_longest, right_longest;
	
	assert(self && offset >= 0 && offset < self->size);

	node_size = 1;
	index = offset + self->size - 1;

	for (; self->longest[index] ; index = PARENT(index)){
		node_size *= 2;
		if (index == 0){
			return;	
		}
	}

	self->longest[index] = node_size;
	
	while (index){
		index = PARENT(index);
		node_size *= 2;
		
		left_longest = self->longest[LEFT_LEAF(index)];
		right_longest = self->longest[RIGHT_LEAF(index)];
		
		if (left_longest + right_longest == node_size){
			self->longest[index] = node_size;
		}		
		else{
			self->longest[index] = MAX(left_longest, right_longest);
		}
	}

}
	
int buddy2_size(struct buddy2* self, int offset){
	unsigned node_size, index = 0;
	
	assert(self && offset >= 0 && offset < self-> size);

	node_size = 1;
	
	for (index = offset+self->size-1; self->longest[index]; index = PARENT(index)){
		node_size *= 2;
	}

	return node_size;
}

void buddy2_dump(struct buddy2* self){
	char canvas[65];
	int i, j;
	unsigned node_size, offset;
	if (self == NULL){
		printf("buddy_dump: (struct buddy*)self == NULL");
		return;
	}
	
	if (self->size > 64){
		printf("buddy_dump: (struct buddy*)self is too big to dump");
		return;
	}

	memset(canvas, '_', sizeof(canvas));
	node_size = self->size * 2;

	for (i = 0; i < 2*self->size - 1; ++i){
		if (IS_POWER_OF_2(i+1)){
			node_size /= 2;
		}
		
		if (self->longest[i] == 0){
			if (i >= self->size - 1){
				canvas[i - self->size +1] ='*';			
			}
			else if (self->longest[LEFT_LEAF(i)] && self->longest[RIGHT_LEAF(i)]){
			offset = (i+1)*node_size - self->size;

			for (j = offset; j < offset + node_size; ++j){
				canvas[j] = '*';
			}		
		}

		}
	}
	canvas[self->size] = '\0';
	puts(canvas);
}

int main(){
	char cmd[80];
	int arg;

	struct buddy2* buddy = buddy2_new(32);
	buddy2_dump(buddy);
	
	printf("cmd: alloc, free, size;\n input: cmd, argument\n");
	
	for(;;){
		scanf("%s %d", cmd, &arg);
		if (strcmp(cmd, "alloc") == 0){
			printf("allocated@%d\n", buddy2_alloc(buddy, arg));
			buddy2_dump(buddy);	
		}else if(strcmp(cmd, "free") == 0){
			buddy2_free(buddy, arg);
			buddy2_dump(buddy);
		}else if(strcmp(cmd, "size") == 0){
			printf("size:%d\n", buddy2_size(buddy, arg));
			buddy2_dump(buddy);
		}else{
			buddy2_dump(buddy);
		}
	}
}


```
--- 

## 扩展思考题

阅读[slab分配算法](http://en.wikipedia.org/wiki/Slab_allocation)，尝试在应用程序中实现slab分配算法，给出设计方案和测试用例。

## “连续内存分配”与视频相关的课堂练习

### 5.1 计算机体系结构和内存层次
MMU的工作机理？

- [x]  

>  http://en.wikipedia.org/wiki/Memory_management_unit

L1和L2高速缓存有什么区别？

- [x]  

>  http://superuser.com/questions/196143/where-exactly-l1-l2-and-l3-caches-located-in-computer
>  Where exactly L1, L2 and L3 Caches located in computer?

>  http://en.wikipedia.org/wiki/CPU_cache
>  CPU cache

### 5.2 地址空间和地址生成
编译、链接和加载的过程了解？

- [x]  

>  

动态链接如何使用？

- [x]  

>  


### 5.3 连续内存分配
什么是内碎片、外碎片？

- [x]  

>  

为什么最先匹配会越用越慢？

- [x]  

>  

为什么最差匹配会的外碎片少？

- [x]  

>  

在几种算法中分区释放后的合并处理如何做？

- [x]  

>  

### 5.4 碎片整理
一个处于等待状态的进程被对换到外存（对换等待状态）后，等待事件出现了。操作系统需要如何响应？

- [x]  

>  

### 5.5 伙伴系统
伙伴系统的空闲块如何组织？

- [x]  

>  

伙伴系统的内存分配流程？

- [x]  

>  

伙伴系统的内存回收流程？

- [x]  

>  

struct list_entry是如何把数据元素组织成链表的？

- [x]  

>  


