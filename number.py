#!/usr/bin/python3

# Numbers in python are integers and float-point numbers

int_numb = 1
float_numb = 1.4

#They converts automatically in follow situation

summa = int_numb + float_numb
print(summa)

#The same result
print(int_numb + float_numb)

#The third way to impress it
print("The sum of variables is: ", (int_numb + float_numb))

#The fourth way to impress it
print("The sum of variables is:  {}".format(int_numb + float_numb))

#The fifth way to impress it
print("The sum of variables is:  %.1f " % (int_numb + float_numb))

#Sum
print("Sum of 5 and 4 is %i" % (5 + 4))

#Multiplication
print("Multiply of 5 and 4 is %.2f" % (5 * 4))

#Division
print("Division of 20  and 4 is %.2f" % (20 / 4))

#Negative adding
print("Negative of 20  and 4 is %.2f" % (20 - 4))
