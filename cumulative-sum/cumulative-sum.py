class Solution:
	def getCumulativeSum(self, l: List[int]) -> List[int]:
		# add your logic here
		for i in range(1, len(l)):
			l[i] += l[i-1]
		return l
