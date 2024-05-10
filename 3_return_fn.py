def sum_2(a, b):
    return a + b

def sum_3(a, b, c):
    return a + b + c

total_sum_2 = sum_2(2, 3)
total_sum_3 = sum_3(2, 3, 4)

total_sum = total_sum_2 + total_sum_3
print( total_sum )


# whatever come after return will not be executed
# inside the function
def sum_4(a, b, c, d):
    total = a + b + c
    return
    total += d

def sum_5(a, b, c, d, e):
    total = a + b + c
    print( total + d + e )


