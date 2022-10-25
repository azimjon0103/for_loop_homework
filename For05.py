def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    b=[]
    for a in range(A,B+1):
        b.append(a)
    #a=list(range(A,B+1))
    return b[::-1]
print(main(5,9))