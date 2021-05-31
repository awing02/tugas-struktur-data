from random import randrange

def my_choice(data):
    a = randrange(0,len(data))
    return data[a]


print(my_choice([5,6,7,8]))