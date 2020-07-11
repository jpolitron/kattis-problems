def firstBadVersion(last_version: int, isBadVersion: int) -> int:
    start = 1
    end = last_version
    while start+1 < end:
        mid = start + (end - start) /2
        if isBadVersion ==  mid:
            end = mid
        else:
            start = mid
    if isBadVersion == start:
    	return int(start)
    return int(end)
print(firstBadVersion(9,5))
print(firstBadVersion(5,4))
