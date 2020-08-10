# Returns a new string where for every char in the original string, there are two chars.
def double_char(string):
    new_str = ""

    for i in range(len(string)):
        new_str += 2*string[i:i+1]
    return new_str


print(double_char("The"))
print(double_char("AAABB"))
print(double_char("Hi-There"))
print(double_char("Hello World"))
print(double_char("Hii everyoneeee"))
