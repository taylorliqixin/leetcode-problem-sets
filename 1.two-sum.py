#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.92%)
# Likes:    17414
# Dislikes: 624
# Total Accepted:    3.4M
# Total Submissions: 7.5M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums:
                if i == j:
                    continue
                elif target == i + j:
                    return [nums.index(i), nums.index(j)]
                else:
                    continue
        
# @lc code=end

