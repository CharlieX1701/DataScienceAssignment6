'''
Zachary Sisco, Unit 6 Assignment
The purpose of this program is to utilize stacks to perform postfix aritmetic.

'''

def main(equ):

    #create input stack and postfix stack
    inStack = list()
    pfStack = list()

    #add input to input stack
    for i in equ:
        inStack.append(i)

    #search through input stack and use pfStack to complete arithmetic   
    for i in inStack:
        
        if i.isdigit():
            pfStack.append(i)
            
        else:
            num1 = pfStack.pop()
            num2 = pfStack.pop()
            result = str(eval(num2 + i + num1))
            pfStack.append(result)
            
    return float(pfStack.pop())
           

print(main('32+4*51-/'))
print(main('478*/21++'))
print(main('45+72-*'))

    

