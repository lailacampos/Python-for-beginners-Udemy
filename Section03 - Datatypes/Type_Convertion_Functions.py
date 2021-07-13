#Type convertion functions

a = 10
b = 12.0
c = '20.5'

#Converting to int type

d = int(b)
print(d) #Decimal points are gone

#Converting to a float type
e = float(c)
print(e)
print(type(e))

#Converting to a binary number
f = bin(a)
print(f) #Will print '0B' and the corresponding binary value for the converted number

#Converting to a hexadecimal number
g = hex(a)
print(g) #Will print '0x' and the corresponding hexadecimal value for the converted number

#Converting to an octal number
h = oct(a)
print(h) #Will print 'Oo' and the corresponding octal value for the converted number