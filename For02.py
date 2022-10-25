def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    b=""
    for a in range(n): 
        b+=str(a)+","
    return '"'+b[:-1]+'"'
print(main(8))        
