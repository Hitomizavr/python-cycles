n = int(input("Число N = " ));
zero = 0
for i in range(n):
    if int(input()) == 0:
        zero = zero + 1;

print("Количество введенных нулей:", zero);