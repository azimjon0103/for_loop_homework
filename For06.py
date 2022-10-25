def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    b=0
    for a in range(A,B):
        b+=a  
    return b
print(main(0,5))    