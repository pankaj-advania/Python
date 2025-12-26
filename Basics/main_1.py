# # # # # print("Hello World!")
# # # # # print("Hello World")
# # # # # print("Mehak Napa")
# # # # # print (7)
# # # # # print(7.7)
# # # # # print(True)
# # # # # print("Hello", 1, 4.5,True)
# # # # # print("Hello",1,4.5,True, sep='/')
# # # # # print("Hello",1,3.5,end='-')
# # # # # print("Duggu")


# # # # # # Intenger
# # # # # print(8)
# # # # # # 1*10^308
# # # # # print(1e308)


# # # # #  # Decimal/ Float
# # # # # print (8.55)
# # # # # print (1.7e309)


# # # # # # Boolean 
# # # # # print(True)
# # # # # print(False)


# # # # # # String
# # # # # print("Pankaj")


# # # # # # Comlex
# # # # # print(5+6j)

# # # # # # list -> c-> Array
# # # # # print([1,2,3,4,5])

# # # # # # Tuple 
# # # # # print({1,2,3,4,5})

# # # # # # # Dictionary
# # # # # # print({"Name" : "Pankaj","Age" : 21,"Address" : "Jallopur"})


# # # # # # # Type 
# # # # # # type (4)
# # # # # # type (True)
# # # # # # type ("Pankaj")
# # # # # # print(type)


# # # # # # Variables
# # # # # # Static Vs Dynamic Typing
# # # # # # Static Vs Dynamic Blinding
# # # # # # Styish declaration techniques


# # # # # # name = "Pankaj"
# # # # # # print(name)
# # # # # # a = 5
# # # # # # b = 7

# # # # # print(a+ b)
# # # # # # Dynamoc Typing 
# # # # # # a = 4

# # # # # # #Static Typing 
# # # # # # int a = 4


# # # # # # Dynamic Blinding
# # # # # # a = 5 
# # # # # # print(a)
# # # # # # a = "Pankaj"
# # # # # # print(a)


# # # # # # Static Binding
# # # # # # int a =5
# # # # # # a = 1
# # # # # # b = 2
# # # # # # c = 3
# # # # # # print(a,b,c)
# # # # # # a,b,c = 1,2,3
# # # # # # print(a,b,c)

# # # # # # a=b=c = 5
# # # # # # print(a,b,c)

# # # # # # Comment

# # # # # # # Keywords & Indentifiers 
# # # # # # # Keywords
# # # # # # # Identifiers
# # # # # # # you can't start with a digit
# # # # # # name1 = "Pankaj"
# # # # # # print(name1)

# # # # # # # you can use special chars -> _
# # # # # # _ = "Pankaj"
# # # # # # print(_)

# # # # # # # identiers can not be keywords 
# # # # fnum = int(input("Enter your number"))
# # # # snum = int(input ("Enter your number"))
# # # # print(fnum, snum)
# # # # result = (fnum + snum)
# # # # print(result)
# # # # Literals 
# # # a = 0b1010 # binary literals
# # # b = 100 # Decimal literals 
# # # c = 0o310 # octal Literals 
# # # d = 0x12c # Hexadecimal Literals

# # # # Float Litrals 
# # # float_1 = 10.5 
# # # float_2 = 1.5e2
# # # float_3 =1.5e-3

# # # # Complex Literal
# # # x = 3.14j
# # # print (a,b,c,d)
# # # print(float_1,float_2,float_3)
# # # print(x, x.imag, x.real)

# # # string = "this is Pyhton"
# # # string = " this is Python "
# # # char = "c"
# # # mutiline_str = """this is a multiline string with more than oneline code ."""
# # # uncode = "\U0001F600\U0001F606\U0001F923"
# # # raw_str = r"raw \n string"
# # # print(string)
# # # print(char)
# # # print(raw_str)

# # # a = T3333




# # # Arthmetic Operators

# # print(5+5) 

# # print(9-5)

# # print(4*4)

# # print(2/2)

# # print(5//2)

# # print(5**3)

# # print(4%2)




# # # Relational Operators

# # print(4<5)
# # print(4>=4)
# # print(4<=4)
# # print(4==4)
# # print(4!=4)


# # # Logical Operators

# # print(1 and 0)
# # print(1 or 0)
# # print( not 1)


# # # Bitwise Operators

# # # bitwise and 
# # # print(2 & 3)

# # # bitwise or 
# # # print(2 |3)

# # # bitwise xor
# # # print(2 ^ 3)

# # # print(~3)
# # # print(4 >> 2)
# # # print(5 << 2)



# # # Assignment Operators
# # # =
# # # a = 2
# # a = 2

# # # a = a % 2
# # a *= 2


# # # a++ ++a
# # print(a)

# # # Membership Operator
# # # in /not in
# # print("p" in "pankaj")
# # print("D" not in "dehli") 
# # number = int(input("Enter your 3 digit no.:"))
# # a = number % 10
# # number = number // 10 

# # b = number % 10
# # number = number // 10
# # c = number % 10
# # number = number // 10
# # # print(a+b+c)

# # help("modules")


# # Loop in Python 
# # * Need for Python 
# # * while loop
# # * for loop

# # number = int(input("Enter the number :"))
# # i = 1
# # while i<11 :
# #  print(number * i)
# #  i+=1


# # guessing game
# # generate a random integer between 1 and 10
# import random
# jackport = random.randint(1,10)

# guess = int(input("guess karo : "))
# counter = 1
# while guess != jackport :
#     if guess < jackport :
#         print("galat ! guess higher")
#     else :
#         print("galat ! guess lower ")
    
#     guess = int(input("guess karo "))
#     counter += 1

# else :
#     print("correct guess")
#     print("attempts", counter)


# For Loops

# for i in range (10,0,-1) :
#     print(i)
# for i in "pankaj" :
#     print(i)
 
curr_pop = 10000

# for i in range (10,0,-1) :
#     print (i,curr_pop)
#     curr_pop = curr_pop - .1 * curr_pop

print(.1 * 10000)c
