noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
for i in range(1, 4):
    print()
    print('i = ', i)
    print()
    for j in range(i*2, 20, i):
        print('j = ',j)
print()

print(noprimes)

