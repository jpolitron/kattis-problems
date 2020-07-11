def isAnagram(s: str, t: str) -> bool:
	if len(s) == len(t):
		ss = set(s)
		tt = set(t)
		for i in s:
			if t.count(i) != s.count(i):
				return False
		return True
	return False
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("listen","silent"))
