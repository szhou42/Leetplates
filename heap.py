#!/usr/bin/python3

class MinHeap:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.heap = [0] * self.capacity
        
    # APIs
    def add(self, number):
        # Make sure heap has enough capacity for adding new numbers
        self.expand_heap()
        
        # Add number to the back of array, then fix heap ordering
        self.heap[self.size] = number
        self.heapify_up()
        self.size += 1

    def poll(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        min_number = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heapify_down()
        self.size -= 1
        return min_number
    
    def peak(self):
        if self.size == 0:
            raise Exception("Heap is empty")
        return self.heap[0]

    # helper methods
    def get_left_child_index(self, index):
        return 2 * index + 1
    
    def get_right_child_index(self, index):
        return 2 * index + 2
    
    def get_parent_index(self, index):
        return int((index-1) / 2)
    
    def heapify_up(self):
        # Make the last number in heap go up, swap with any parent that's bigger than it
        index = self.size - 1
        parent_index = self.get_parent_index(index)
        
        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = self.get_parent_index(index)
    
    def heapify_down(self):
        # Make the last number in heap go down, swap with any smaller child down the chain(until no child or no smaller child)
        index = 0
        left_child_index = self.get_left_child_index(index)
        while left_child_index < self.size:
            smaller_child_index = left_child_index
            right_child_index = self.get_right_child_index(index)
            if right_child_index < self.size:
                smaller_child_index = right_child_index if self.heap[right_child_index] < self.heap[left_child_index] else smaller_child_index
            
            # Is any child smaller than me? if no, exit
            if self.heap[smaller_child_index] >= self.heap[index]:
                break
            
            self.heap[smaller_child_index], self.heap[index] = self.heap[index], self.heap[smaller_child_index]
            index = smaller_child_index
            left_child_index = self.get_left_child_index(index)
            
    def expand_heap(self):
        if self.size == self.capacity:
            self.capacity *= 2
            self.heap = self.heap + [0]*(self.capacity-self.size)

# test code
h = MinHeap()
h.add(3)
h.add(1)
h.add(4)
h.poll()
print(h.peak())

"""
Practice Problems:
https://leetcode.com/problems/merge-k-sorted-lists
"""