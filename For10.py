def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer 
    """
    b=[]
    i=0
    for a in list1:
        b.append(a.title())
    return b
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))    