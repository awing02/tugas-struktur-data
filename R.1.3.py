def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)


print(minmax([0,14,40,9,16,70,90,50,-2,40,4,-6,35,2,-2,-20]))