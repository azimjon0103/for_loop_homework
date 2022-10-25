def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    i=0
    ans=0
    a=list(range(A,B))
    while i<len(a):
        if a[i]!=0:
            ans+=a[i]
        i+=1    
    return ans
print(main(0,5))    