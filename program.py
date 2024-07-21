# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#oprator programs
print(" Name : Krishna Singh Rathore   Reg_Num: 24MCA1016\n")
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
temp1 = a;
temp2 = b;
print("Arithmetic operators")

print("Addtion :" , a + b)
print("Subtraction :" , a - b)
print("Multiplication :" , a * b)
print("Division :" , a / b)
print("Modulus :" , a % b)
print("Exponentition :" , a ** b)
print("Floor Division :" , a // b , "\n")

print("Assignment operators")

a  = 10
print("assign :" , a )
a += b
print("Addtion assign :" , a)
a -= b
print("Subtraction assign :" , a)
a *= b
print("Multiplication  assign:" , a)
a /= b
print("Division assign:" , a)
a %= b
print("Modulus assign:" , a)
a **= b
print("Exponentition assign:" , a)
a //= b
print("Floor Division assign:" , a , "\n")

print("Comparison Operators")

print("Equal: ", a == b);
print("Not Equal: ", a != b);
print("Greater Than or Equal To: ", a >= b);
print("Less Than or Equal To: ", a <= b);
print("Less Than : ", a < b);
print("Greater Than : ", a > b , "\n");

print("Logical Operators")

print("AND: ", a < 5 and  b > 5);
print("OR: ", a < 5 or b < 4);
print("Not: ", not(a < 5 and b < 4) , "\n");

print("identity Operators")

List1 = ["Car", "Bike"]
List2 = ["Car", "Bike"]

print("Is: ", List1 is List2);
print("is not: ", List1 is not List2 , "\n");

print("Membership Operators")

List3 = ["Car", "Bike"]

print("Is: ", "Car" in List3);
print("is not: ", "Kr" not in List3 , "\n");

print("Bitwise operators\n");

print("And Bitwise Operators:" , temp1 & temp2);
print("OR Bitwise Operators:" , temp1 | temp2);
print("XOR Bitwise Operators:" , temp1 ^ temp2);
print("Zero Fill Left Shift Bitwise Operators:" , temp1 << temp2);
print("Signed Right Shift Bitwise Operators:" , temp1 >> temp2 , "\n");

print("Question NO 2 for finding Labour Cost and Total Charges\n");

Rate_per_hour = 45;
Cost_of_Materials = int(input("Enter the cost of Material: "));
Hour_Work = int(input("Enter Labour Hour Work: "));
Labour_Cost = Rate_per_hour * Hour_Work; 
Total_charges = Labour_Cost + Cost_of_Materials;

print("Labour Cost:" , Labour_Cost , "\nCost_of_Materials:" , Cost_of_Materials , "\nTotal_charges:" , Total_charges , "\n");

print("Question NO 3 for Finding Basic pay");

Basic_pay = int(input("Enter the Basic Pay: "));
DA = int(input("Enter Dearness Allowance:"));
HRA = int(input("Enter House Rent Allowance: "));
PF = int(input("Enter PF Amount: "));
print("Basic Pay: " , ((DA/100)*Basic_pay) + ((HRA/100)*Basic_pay) - ((PF/100)*Basic_pay));








