def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    a=list(range(N))
    i=0
    ans=0
    while i<len(a):
        if a[i]%2==1:
            ans+=a[i]
        i+=1    
    return ans
print(main(12))    