class Solution:
	def containsElement(self, arr: List[int], e: int) -> bool:
		# add your logic here
		low = 0
		high = len(arr) - 1
		while low <= high:
			mid = (low + high) // 2
			if arr[mid] == e:
				return True
			elif arr[mid] < e:
				low = mid + 1
			else:
				high = mid - 1
		return False
