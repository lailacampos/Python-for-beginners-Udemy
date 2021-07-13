#Input function

# myString = input("Enter your name: ")
# print(myString)
#
# myInt = int(input("Enter a integer number: "))
# print(type(myInt))

lista = [x for x in input("Digite três números").split(sep=',', maxsplit=3)]
print(lista)