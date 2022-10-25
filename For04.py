def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    b=[]
    for a in range(A,B+1):
        b.append(a)
    return b
print(main(2,7))    