for i in range(0,100):
    if i % 4 == 0:
        print(bin(i))
    else:
        print(str(i) + ": " + bin(i))