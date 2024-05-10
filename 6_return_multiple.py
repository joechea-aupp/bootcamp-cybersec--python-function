def return_multiple(a, b, c):
    total = a + b + c
    return total, c

total_sum = return_multiple(2, 3, 4)
print( total_sum )

total_computed, last_num = return_multiple(2, 3, 4)
print( total_computed, last_num )
