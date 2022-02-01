#Krish Dhansinghani bje9jj

num = int (input("Pick a number between 1 and 10: "))
already_birthday = int (input("If you've already had a birthday this year, enter 1771. Otherwise, enter 1770: "))
year_born = int (input("Enter the year that you were born: "))

def add(x, y):
    return x + y
def mult(x, y):
    return x * y
def sub(x, y):
    return x - y
val1 = mult(num, 2)
val2 = add(val1, 5)
val3 = mult(val2, 50)
val4 = add(val3, 1770)

if already_birthday == 1770:
        val4 = add(val3, 1770)
if already_birthday == 1771:
        val4 = add(val3, 1771)

val5 = sub(val4, year_born)
age = val5 % 100

print("The magic number is " + '"' + str(val5) + '"' + ". " "That means you are " + str(age) + "!")