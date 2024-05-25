def add(a,b):
    ans = a+b
    print(str(a) +"+" +str(b)+"="+str(ans))

    
def sub():
    ans = a-b
    print(str(a) +"-"+str(b)+"="+str(ans))


def mul(a,b):
    ans = a*b
    print(str(a) +"*"+str(b)+"="+str(ans))

    
def div():
    ans = a/b
    print(str(a) +"/"+str(b)+"="+str(ans))


while True:
    
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Divivsion")
    print("4. Multiplication")
    print("5. Exit")

    choice = input('enter choice')

    if choice == 1:
        print("Addition")
        a = int(input("enter a"))
        b = int(input("enter b"))
        add(a,b)
    
    elif choice == 2:
        print("Subtraction")
        a = int(input("enter a"))
        b = int(input("enter b"))
        sub(a,b)

    if choice == 3:
        print("Multiplication")
        a = int(input("enter a"))
        b = int(input("enter b"))
        mul(a,b)
    
    elif choice == 4:
        print("Division")
        a = int(input("enter a"))
        b = int(input("enter b"))
        div(a,b)

    elif choice == 5:
        print('End')
        quit()
    
