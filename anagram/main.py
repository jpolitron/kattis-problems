def isAnagram(s: str, t: str) -> bool:
	if len(s) == len(t):
		s = list(s)
		s.sort()
		t = list(t)
		t.sort()
		if s == t:
			return True
		else:
			return False
	return False
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("listen", "silent"))
