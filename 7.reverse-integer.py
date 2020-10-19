#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.82%)
# Likes:    3841
# Dislikes: 5988
# Total Accepted:    1.3M
# Total Submissions: 4.9M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Note:
# Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
# 
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            n = len(x)
            tmp_list = []

            for i in range(n):
                tmp_list.append(x[n - i - 1])
            
            tmp_list = "-" + "".join(tmp_list)
            tmp_list = int(tmp_list)
        else:
            n = len(x)
            tmp_list = []

            for i in range(n):
                tmp_list.append(x[n - i - 1])
            
            tmp_list = "" + "".join(tmp_list)
            tmp_list = int(tmp_list)
        
        if tmp_list <= 2147483647 and tmp_list >= -2147483647:
            return tmp_list
        else:
            return 0
    
# @lc code=end

