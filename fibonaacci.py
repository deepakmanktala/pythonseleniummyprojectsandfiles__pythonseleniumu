a, b = 0, 1

for i in range (0, 10000):
    print(a)
    a, b = b,a+b
    if a % b != 0 :
        print('you got it')
