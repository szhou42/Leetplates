class Solution:    
    def quicksort(self, nums, left, right):
      if left < right:
        pivot_index = self.partition(nums, left, right)
        self.quicksort(nums, left, pivot_index-1)
        self.quicksort(nums, pivot_index+1, right)

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
