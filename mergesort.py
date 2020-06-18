class Solution:
    def mergesort(self, nums, left, right):
      # Base case, subarray has 1 number
      if left == right:
        return

      mid = left + (right-left)/2
      self.mergesort(nums, left, mid)
      self.mergesort(nums, mid+1, right)

      left_start = left
      left_end = mid

      right_start = mid+1
      right_end = right

      self.merge(nums, left_start, left_end, right_start, right_end)

    def merge(self, nums, left_start, left_end, right_start, right_end):
      arr = []
      i,j = left_start, right_start

      while i <= left_end and j <= right_end:
        if nums[i] <= nums[j]:
          arr.append(nums[i])
          i += 1
        else:
          arr.append(nums[j])
          j += 1

      while i <= left_end:
        arr.append(nums[i])
        i += 1

      while j <= right_end:
        arr.append(nums[j])
        j += 1

      for i in range(len(arr)):
        nums[left_start + i] = arr[i]
