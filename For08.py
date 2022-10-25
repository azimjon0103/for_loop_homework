def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    b=0

    for a in range(1, N+1):
        b+=(1/a)
    return b
print(main(4))    