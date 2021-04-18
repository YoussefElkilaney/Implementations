'''
This is an implementation of Min-Heap
This code is not commented and probably not a clean code, so excuse me
There're many 'print' debugging lines, I've used them and 
decided to let them as is, so feel free to uncomment and
see intermedite outputs.

This code is my solution of a problem from HackRank practice
https://www.hackerrank.com/challenges/qheap1/problem
'''

class Heap():
    def __init__(self):
        self.items = []
        self.indices = {}
        self.idx = 0

    def _siftUp(self, idx):
        if idx == 0: return
        parent = (idx-1)//2
#         print(idx, self.items, self.indices)
        while parent >= 0 and self.items[idx] < self.items[parent]:
            self.swap(idx, parent)
            idx = parent
            if idx == 0: return
            parent = (idx-1)//2
#             print(idx, self.items, self.indices)
    
    def _siftDown(self, idx):
        left, right = idx*2+1, idx*2+2
        while left < self.idx:
            swapped = left
            if right < self.idx and self.items[right] < self.items[swapped]:
                swapped = right
            if self.items[swapped] < self.items[idx]:
#                 print(swapped, idx)
                self.swap(swapped, idx)
            idx = swapped
            left, right = idx*2+1, idx*2+2
    
    def swap(self, idx, parent):
        self.indices[self.items[idx]], self.indices[self.items[parent]] = parent, idx
        self.items[idx], self.items[parent] = self.items[parent], self.items[idx]
    
    def add(self, v):
        self.items.append(v)
        self.indices[v] = self.idx
        self._siftUp(self.idx)
#         print('1', self.items, sorted(self.indices, key=lambda x:self.indices[x]))
        self.idx += 1
    
    def remove(self, v):
#         print('\n', self.indices[v], self.items[-1])
        self.items[self.indices[v]], self.indices[self.items[-1]] = self.items[-1], self.indices[v]
        self.items = self.items[:-1]
        self.idx -= 1
#         print('remove', v, 'with idx', self.indices[v], '#', self.idx)
#         print(self.items)
        if self.indices[v] < self.idx:
            self._siftDown(self.indices[v])
        self.indices.pop(v)
#         print('2', self.items, sorted(self.indices, key=lambda x:self.indices[x]))
    
    def front(self):
        return self.items[0]
    
myHeap = Heap()

with open('f.txt', 'r') as f:
    Q = int(f.readline())
    i = 0
#     print(i, Q)
    while i < Q:
        i += 1
        l = f.readline().split()
#         print(l)
        if len(l) == 1:
            print(myHeap.front())
        else:
            t, v = list(map(int, l))
            if t == 1:
#                 print('adding', v, end =' ')
                myHeap.add(v)
#                 print('added')
            else:
#                 print('removing', v, end=' ')
                myHeap.remove(v)
#                 print('removed')


# Q = int(input())
# i = 0
# while i < Q:
#     i += 1
#     l = input().split()
#     if len(l) == 1:
#         print(myHeap.front())
#     else:
#         t, v = list(map(int, l))
#         if t == 1:
#             myHeap.add(v)
#         else:
#             myHeap.remove(v)
