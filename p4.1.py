print("Name: Niya Joshy")
print("Admission No:A24MCA049")
print("Experiment No:4")

inputcolor1=input("Enter colour separated by commas ")
list1=inputcolor1.split(",")
if len(list1[0])>1:
    print("The first colour is ", list1[0])
    print("The last colour is ", list1[-1])
else:
    print("No colours entered")
inputcolor2=input("Enter second coloured list separated by commas ")
list2=inputcolor2.split(",")

unique=[color for color in list1 if color not in list2]
print("The unique list is ",unique)

intlist=list(range(1,len(list1)+1))
print("integer valued list from first list ",intlist)

oddlist=[num for num in intlist if num % 2 != 0]
print("Removed odd numbers from list ",oddlist)