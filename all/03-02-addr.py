# Input: memory
#   The memory description given by teacher
#
# Type the hex number of the virtual address on screen
#
# Output: answer
#   The answer for each input in a fixed format
#
# Author: zhoujie15
#
# Time: 2015-03-18

fin = open('memory', 'rb')
fout = open('answer', 'wb')
memory = []
for line in fin:
    k = line.find(':')
    line = line[k+2:]
    arr = line.strip('\r\n').split(' ')
    for item in arr:
        if item != '':
            memory.append(int(item, 16))

pdbr = 0x220

while True:
    num = raw_input()
    if num == '':
        break
    va = int(num, 16)
    fout.write('Virtual Address ' + num + ':\n')

    of1 = (va & 0x7c00) >> 10
    of2 = (va & 0x3e0) >> 5
    of3 = va & 0x1f

    fout.write('  --> pde index:' + str(hex(of1)))

    pde = memory[pdbr + of1]
    valid = (pde & 0x80) >> 7
    pde = pde & 0x7f
    fout.write('  pde contents:(valid ' + str(valid) + ', pfn ' + str(hex(pde)) +')\n')
    if valid == 0:
        fout.write('      --> Fault (page directory entry not valid)\n')
        continue

    ad = (pde << 5) + of2



    pte = memory[ad]
    valid = (pte & 0x80) >> 7
    pte = pte & 0x7f

    fout.write('    --> pte index:' + str(hex(of2)) + '  pte content:(valid ' + str(valid) + ', pfn ' + str(hex(pte)) + ')\n')
    if valid == 0:
        fout.write('      --> Fault (page table entry not valid)\n')
        continue

    pa = (pte << 5) + of3

    fout.write('      --> Translate to Physical Address ' + str(hex(pa)) + ' --> Value: ' + str(hex(memory[pa])) + '\n')

