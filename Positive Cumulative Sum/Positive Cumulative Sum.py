class Solution:
	def getPositiveCumulativeSum(self, arr: List[int]) -> List[int]:
		# add your logic here
		ans = [arr[0]] if arr[0] > 0 else []
		for i in range(1, len(arr)):
			arr[i] += arr[i-1]
			if arr[i] > 0:
				ans.append(arr[i])
		return ans
