def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    b=[]
    for a in range(1,11):
        b.append(a*price)
    return b    
print(main(2.25))