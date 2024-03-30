print("Hello World")

def main():
    print("Hello World")
main()

import myPythonFile   
myPythonFile.func()

def func():
    print("Hello World")
if __name__ == "__main__":
    print("interpreter")
    print(__name__)
else:
    print("import")
    print(__name__)

def main():
    print("Let's implement addition. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d + %d = %d" % (x, y, add(x, y)))    
    

# TODO: add() 함수 정의
def add(x,y):
    return x+y

if __name__ == "__main__":
    main()

def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    if y!=0:
        print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    else: divide(x,y)
    
def add(a, b):
    return a + b
    
    
# TODO: divide() 함수 정의
def divide(x,y):
    if y==0:
        print("Error: cannot divide by zero.")
    else: return x/y

if __name__ == "__main__":
    main()
