print("Digite o Valor desejavel do Fibonacc: ")
int(input(">>"))
b = 1
t1 = 0
t2 = 1
if a < 0:
    raise ValueError("n tem que ser maior do que zero")

if a == 0:
    print(0)
if a == 1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)
    b += 1
while b < a:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    b += 1
    if b == a:
        printf"(Fibonacci({a}) = {t3})"

