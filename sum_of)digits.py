def sumdigit(string):
    total=0
    for a in string:
        #checking if character is digit and adding it
        if a.isdigit():
            total+=int(a)
    return total
userinput=input("enetr any string with digits:")
#function calling
result=sumdigit(userinput)
#printing the sumof all digits
print("the sum of all digits in the string  ",userinput )
print("is:",result)
