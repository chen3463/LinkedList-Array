'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)): 
            left[i] = nums[i-1] * left[i-1]
            
        for j in range(len(nums)-2, -1, -1):
            right[j] = nums[j+1] * right[j+1] 
            
        for k in range(len(nums)):
            res[k] = left[k] * right[k]
        return res
