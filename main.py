a = 4
B = 2
#C = B - 1
#R = C + B
#if a < 0 :
    #print("ValueError")
    
#if a > -1:
    #print("Fibonacci(0) = 0")
    #B += 1
    #a -= 1
#if a > 0:
    #print("Fibonacci(1) = 1")
    #B += 1
    #a -= 1
while a > 2:
    C = B - 2
    H = B - 1
    R = H + C
    print(f"Fibonacci({B}) = {R}")
    a -= 1
    B += 1
    
