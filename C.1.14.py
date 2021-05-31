def odd_product_pair(data):
    data = set(data)
    for y in data:
        for x in data:
            if y == x :
                continue
        if y*x % 2 == 1:
            return True
    return False


print(odd_product_pair([6,8,10,15,17]))