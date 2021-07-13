#Pyhton checks the value of the object before allocating memory. If there's already an object with that same value, it simply points
#to the same memory location instead of reallocating the memory again.

a = 10
b = 10

print(id(a)) #Will print the memory location of the object
print(id(b))
print(a is b) #Returns 'true' if the following is true
print("a = ", a, ", b = ", b)

a = 15

print(id(a))
print(id(b))
print(a is b)
print("a = ", a, ", b = ", b)