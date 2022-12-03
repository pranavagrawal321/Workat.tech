class Solution:
	def getSquareSortedArray(self, arr: List[int]) -> List[int]:
		# add your logic here
		return sorted(map(lambda x: x**2, arr))
