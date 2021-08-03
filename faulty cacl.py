print('welcome')
a,b = list(map(int,(input("enter your numbers ").split())))
operand = input("enter your operation ").strip()
if operand == '+':
    res = a+b
    print("your answer: ",res)
elif operand == '-':
    res = a-b
    print("your answer: ",res)

elif operand == '*':
    res= a*b
    if a ==(45 or 98) and b ==(45 or 98):
        print(135)
    else:
        print("your answer: ",res)

elif operand == '/':
    print("your answer: ",res)
