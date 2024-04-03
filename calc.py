#1
print("Hello World")

#2
def main():
    print("Hello World")
main()
#3
#main.py
import myPythonFile   
myPythonFile.func()
#myPythonFile.py
def func():
    print("Hello World")
if __name__ == "__main__":
    print("interpreter")
    print(__name__)
else:
    print("import")
    print(__name__)



#calc.py
#addition
def main():
    print("Let's implement addition. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d + %d = %d" % (x, y, add(x, y)))    
    
def add(x,y):
    return x+y

if __name__ == "__main__":
    main()
    
#subtraction
def main():
    print("Let's implement subtraction. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d - %d = %d" % (x, y, subtract(x, y)))    
    
def subtract(x,y):
    return x-y

if __name__ == "__main__":
    main()

#multiplication
def main():
    print("Let's implement multiplication. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d * %d = %d" % (x, y, multi(x, y)))    
    
def multi(x,y):
    return x*y

if __name__ == "__main__":
    main()

#divide
def divide(x,y):
    if y==0:
        print("Error: cannot divide by zero.")
    else: return x/y

if __name__ == "__main__":
    main()
