def fibonacci(i):
    b = 1
    t1 = 0
    t2 = 1
    if i < 0:
        raise ValueError("n tem que ser maior do que zero")
    if i == 0:
        return 0
    if i == 1:
        return 1
    while b < i:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        b += 1
    if b == i:
        return(t3)
if __name__== "__main__":
    print("Digite a posição do Fibonacci: ")
    i = int(input(">>>"))
    fibonacci(i)