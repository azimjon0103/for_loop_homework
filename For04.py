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
    for A in range(B+1):
        b.append(A)
    return b[2:]
print(main(2,7))    