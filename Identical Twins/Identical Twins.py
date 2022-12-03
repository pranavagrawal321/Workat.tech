class Solution:
	def getIdenticalTwinsCount(self, arr: List[int]) -> int:
		# add your logic here
		c = 0
		for i in range(len(arr)):
			for j in range(i+1, len(arr)):
				if arr[i] == arr[j]:
					c += 1
		return c
