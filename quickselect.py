class Solution:
    def find_kth_largest(self, nums, k):
        return self.quickselect(nums, 0, len(nums)-1, len(nums)-k+1)
    
    def quickselect(self, nums, left, right, k):
        index = self.partition(nums, left, right)
        # index-left+1 is where our chosen pivot lives, counting from 1,2,3...
        if index-left+1 == k:
            return nums[index]
        elif index-left+1 < k:
            # if kth smallest element is on the right, then only look in the right array, with new k excluding 
            # everything <= pivot, e.g if k=4 and we know left array has the smallest 3 numbers, then just 
            # look for the smallest 1 number in the right array
            return self.quickselect(nums, index+1, right, k-(index-left+1))
        else:
            return self.quickselect(nums, left, index-1, k)
        
    def partition(self, nums, left, right):
        pivot = nums[right]

        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, right)
        return i

    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
