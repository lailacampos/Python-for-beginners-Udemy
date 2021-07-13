a,b,c = [float(x) for x in input("Enter three numbers separated by comma: ").split(sep=',', maxsplit=2)]
print(a,b,c)

average = (a+b+c)/3

print("Average of three numbers is %.2f" % average)