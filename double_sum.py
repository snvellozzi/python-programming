# Returns the sum of 2 ints and doubles the sum if the ints are the same
def double_sum(a, b):
    if a == b:
        return 2*(a+b)
    else:
        return a + b


print(double_sum(1, 3))
print(double_sum(2, 2))
print(double_sum(9, 8))
print(double_sum(4, 4))
print(double_sum(10, 10))
print(double_sum(5, 6))
