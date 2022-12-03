class Solution:
	def largestContiguousSum(self, arr: List[int]) -> int:
		# add your logic here
		max_so_far = 0
		max_final = -float('inf')
		for i in arr:
			max_so_far = max(i, max_so_far + i)
			max_final = max(max_final, max_so_far)
		return max_final
