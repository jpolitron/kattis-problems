def merge_overlapping_intervals(intervals):
    s = sorted(intervals, key=lambda t: t[0])
    m = 0
    for  t in s:
        if t[0] > s[m][1]:
            m += 1
            s[m] = t
        else:
            s[m] = s[m][0], t[1]
    return s[:m+1]

print(merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]]))
#expected out put [1,6],[8,10],[15,18]
