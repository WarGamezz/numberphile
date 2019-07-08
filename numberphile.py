# This is my introduction to programming. I have no previous programming experience.
# Created using multiple sources including: tutorialspoint.com; python-course.eu; w3schools.com; Corey Schafer's YouTube tutorial. I do not mean to infringe any copyright laws, this file was compiled to put all of the knowledge required in one place. If there's any issue with the copyrights, please message me and I will delete requested data immediately.
# Using Visual Studio Code on Windows machine, using better comments extension for better visuals
# Word wrap is set.
# Git https://github.com/WarGamezz/numberphile

# Number data types store numeric values. Number objects are created when you assign a value to them. For example:
number1 = 14

#! Numerical Types

#Python supports three different numerical types −

#int (signed integers) = 3
#float (floating point real values) = 3.14
#complex (complex numbers) - A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are real numbers and j is the imaginary unit.

#! Python Arithmetic Operators
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2 
# Division:       3 / 2     Divides left hand operand by right hand operand. (Regular division known from school)
# Floor Division: 3 // 2    The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
# Exponent:       3 ** 2    Performs exponential (power) calculation on operators
# Modulus:        3 % 2     Divides left hand operand by right hand operand and returns remainder

#! Python Comparisons Operators
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

#! Python Assignment Operators
# =                 //  Assigns values from right side operands to left side operand  //  c = a + b assigns value of a + b into c
# += Add AND        //  Adds right operand to the left operand and assign the result to left operand // c += a is equivalent to c = c + a
# -= Subtract AND   //  Subtracts right operand from the left operand and assign the result to left operand // c -= a is equivalent to c = c - a
# *= Multiply AND   //  Multiplies right operand with the left operand and assign the result to left operand // c *= a is equivalent to c = c * a
# /= Divide AND     //  Divides left operand with the right operand and assign the result to left operand // c /= a is equivalent to c = c / a
# %= Modulus AND    //  Takes modulus using two operands and assign the result to left operand // c %= a is equivalent to c = c % a
# **= Exponent AND  //  Performs exponential (power) calculation on operators and assign value to the left operand // c **= a is equivalent to c = c ** a
# /= Floor Division // It performs floor division on operators and assign value to the left operand // c //= a is equivalent to c = c // a

#! Python Bitwise Operators
#Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows

#a = 0011 1100 -  print(bin(60))
#b = 0000 1101 -  print(bin(13))

#Operators available
# & Binary AND              //  Operator copies a bit, to the result, if it exists in both operands // a&b = 0000 1100
# | Binary OR               //  It copies a bit, if it exists in either operand. // a|b = 0011 1101
# ^ Binary XOR              //  It copies the bit, if it is set in one operand but not both. // a^b = 0011 0001
# ~ Binary Ones Complement  // It is unary and has the effect of 'flipping' bits. // ~a = 1100 0011
# << Binary Left Shift      // The left operand's value is moved left by the number of bits specified by the right operand. // a << 2 = 1111 0000
# << Binary Right Shift     // The left operand's value is moved right by the number of bits specified by the right operand. // a >> 2 0000 1111

#! Python Logical Operators
#The following logical operators are supported by Python language. Assume variable a holds True and variable b holds False then:

#and Logical AND // If both the operands are true then condition becomes true. // (a and b) is False.
#or Logical OR // If any of the two operands are non-zero then condition becomes true. // (a or b) is True.
#not Logical NOT // Used to reverse the logical state of its operand. // Not(a and b) is True.

#! Python Membership Operators
# Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
#in // Evaluates to true if it finds a variable in the specified sequence and false otherwise. // x in y, here in results in a 1 if x is a member of sequence y.
#not in // Evaluates to true if it does not finds a variable in the specified sequence and false otherwise. // x not in y, here not in results in a 1 if x is not a member of sequence y.

#! Python Identity Operators
#is // Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. // x is y, here is results in 1 if id(x) equals id(y).
#is not // Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. // x is not y, here is not results in 1 if id(x) is not equal to id(y).