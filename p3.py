print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:3")

a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
if(a>b):
    if(a>c):
        print(a)
        n=a
    else:
        print(c)
        n=c
else:
    if(b>c):
        print(b)
        n=b
    else:
        print(c)
        n=c
print("Biggest Number is",n)
print("result=",n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))
area=3.14*n*n
perimeter=2*3.14*n
volume=(4/3)*3.14*n**3
print("Area of a circle with radius ",n,"is",area)
print("Perimeter of a circle with radius ",n,"is",perimeter)
print("Volume of a circle with ",n,"is",volume)