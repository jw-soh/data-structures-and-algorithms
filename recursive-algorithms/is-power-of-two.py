def isPowerOfTwo(n: int) -> bool:
    
    # given some integer n, e.g. n = 32
    # base case: n = 1
    # return true
    if (n == 1): return True
    
    # check if n is divisible by 2
    if (n % 2 == 0):
        return True and isPowerOfTwo(n // 2)
    else:
        return False # somewhere down the line n // 2 is not divisible by 2 and hence n is not a power of 2
            