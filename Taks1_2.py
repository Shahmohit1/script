#TASK 1
x=0
f = open('value.txt','r')
x=f.read()
f.close()

print("The given number is " + x)#x is still string 
#converting string to integer type 
x= int(x)
#storing x^2 in variable y
y=x*x
print("The square of the number is ",y)#here y is integer

# TASK 2
w= open('solution.txt','w')#storing file in varibale w 
#writing square of the given number 
#while converting the integer y to string type 
w.write("The square of the number is " + str(y))

