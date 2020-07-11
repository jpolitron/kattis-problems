# NOTE: first step: A: identify the position of the largest pancake
#B: move it to the top

def pancakeSort(self, A: List[int]) -> List[int]:
    def flip(A,index):
        i,j = 0, index
        while i < j:
            A[i], A[j] = A[j],A[i]
            i += 1
            j -= 1

    res = []
    n = len(A)
    largest = n
    for i in range(n):
        indexLargest = A.index(largest)
        flip(A, indexLargest)
        res.append(indexLargest + 1)
        flip(A,largest - 1)
        res.append(largest)
        largest -= 1
    return res
