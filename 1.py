def add(x,y):
	return  x+y;
def sub(x,y):
	return x-y;

def mul(x,y):
	return x*y;

def div(x,y):
	return x/y;
def mod(x,y):
	return x%y;
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
choice=input("select opertion :")

if (choice =='1'):
	print("sum is ",add(a,b))

elif (choice =='2'):
	print("sub is ",sub(a,b))

elif (choice =='3'):
	print("mul is ",mul(a,b))

elif (choice =='4'):
	print("div is ",div(a,b))
else:
	print("modulus is",mod(a,b))
