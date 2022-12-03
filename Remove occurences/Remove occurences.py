class Solution:
	def removeOccurences(self, Array: List[int], Number: int) -> int:
		# add your logic here
		i = 0
		while i < len(Array):
			if Array[i] == Number:
				Array.remove(Number)
			else:
				i += 1
		return len(Array)
