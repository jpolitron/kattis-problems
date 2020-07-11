def romanToInt(s: str) -> int:
	sum = 0
	roman = {'I': 1, 'V': 5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
	for i in range(len(s)):
		if i < len(s)-1 and roman[s[i+1]] > roman[s[i]]:
			sum -= roman[s[i]]
		else:
			sum += roman[s[i]]
	return sum
print(romanToInt('I'))
print(romanToInt('II'))
print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('V'))
print(romanToInt('VI'))
print(romanToInt('VII'))
print(romanToInt('VIII'))
print(romanToInt('IX'))
