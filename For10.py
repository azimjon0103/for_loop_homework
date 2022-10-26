def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer 
    """
    b=[]
    for a in range(list1):
        b.title(a)
    return b
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))    