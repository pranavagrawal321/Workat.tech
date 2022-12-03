class Solution:
	def getEvenDigitNumbers(self, arr: List[int]) -> Optional[List[int]]:
		# add your logic here
		ans = []
		for i in arr:
			if len(str(i))%2 == 0:
				ans.append(i)
		return ans
