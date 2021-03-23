#Pythoneers -- Kano Kitaguchi and Anita Liang
#IntroCS pd06 sec10
#L4 -- Controlling the Flow
#2021-03-19

#Type in the funciton name like <functionName>() to get the test cases for it
ask = input("Enter function to test : ")

#takes the target number plus two others, and returns a statement saying which number was closer to the target
def closer_num(target, num1, num2):
    one = abs(target - num1)
    two = abs(target - num2)
    if one>two:
        print(num2, " is closer to ", target)
    elif one<two:
        print(num1, " is closer to ", target)
    elif target==num1==num2:
        print("They're all equal!")
    else:
        print("Neither number is closer to ", target)
        
# Test Cases for closer_num()
if ask=="closer_num()":
    closer_num(8, 20, 10)
    print("...should return 10 is closer to 8")
    closer_num(8, 20, 2)
    print("...should return 2 is closer to 8")
    closer_num(8, -2, 30)
    print("...should return -2 is closer to 8")
    closer_num(8,-2,-2)
    print("...should return Neither number is closer to 8")
    closer_num(8,8,8)
    print("...should return They're all equal")


#Takes percentage grade and converts it into a letter grade, and returns that along with a comment
def grade_conv(g):
    if g<=100 and g>=0:
        if g<=100 and g>89.5:
            print("A")
        elif g<89.5 and g>=79.5:
            print("B")
        elif g<79.5 and g>=69.5:
            print("C")
        elif g<69.5 and g>=64.5:
            print("D")
        elif g<64.5 and g>=0:
            print("F")
    else:
        print("YOUR INPUTTED GRADE IS INVALID")
        
# Test Cases for grade_conv()
if ask=="grade_conv()":
    grade_conv(64.56)
    print('...should return D')
    grade_conv(86.3)
    print('...should return B')
    grade_conv(70)
    print('...should return C')
    grade_conv(-12)
    print('...should return YOUR INPUTTED GRADE IS INVALID')

#Takes a letter from A-F as an input, and returns a comment based on it.
def pass_judgement(letter_grade):
    config_grade = letter_grade.upper()
    if config_grade=='A':
        print("... you're doing good")
    elif config_grade=='B':
        print("... you're doing ok")
    elif config_grade=='C':
        print("... you could be doing better")
    elif config_grade=='D':
        print("... you're borderline failing. Get it together")
    elif config_grade=='F':
        print("... well you've hit rock bottom. At least you can only go up from here")
    else:
        print("INVALID GRADE\n Try checking for unneccesary spaces\n Make sure your input is a letter")
        
# Test Cases for pass_judgement()
if ask=="pass_judgement()":
    pass_judgement('b')
    print("...should return you're doing ok")
    pass_judgement('D')
    print("...should return you're borderline failing. Get it together")
    pass_judgement('100')
    print("...should return INVALID GRADE try checking for unneccesary spaces make sure your input is a letter")


# Use recursion to calculate factorial
def fact_r(n):
    if type(n)=='int':
        if n == 1:  
            return n  
        else:  
            return n*fact_r(n-1)
    else:
        print("please enter a positive whole number")
    
# Test Cases for fact_r()
if ask=="fact_r()":
    print(fact_r(7))
    print("...should return 5040")
    print(fact_r(10))
    print("...should return 3628800")
    print(fact_r(2.56))
    print("...should return please enter a positive whole number")
    
    
#Use iteration to calculate factorial
def fact_w(n):
    if type(n)=='int':
        i = 1
        while n>=1:
              i = i*n
              n = n-1
        return i
    else:
        print("please enter a positive whole number")

# Test Cases for fact_w()
if ask=="fact_w()":
    print(fact_w(7))
    print("...should return 5040")
    print(fact_w(-2.5))
    print("...should return please enter a positive whole number")
    print(fact_w(3))
    print("...should return 6")
    