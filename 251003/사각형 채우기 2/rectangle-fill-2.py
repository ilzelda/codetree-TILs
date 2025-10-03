N = int(input())

# Please write your code here.
mem = [ -1 for _ in range(N+1) ]

mem[1] = 1
mem[2] = 3

def recur(n):
    if n==1: return 1
    if n==2 : return 3
    
    a = recur(n-1) if mem[n-1] == -1 else mem[n-1]
    b = recur(n-2) if mem[n-2] == -1 else mem[n-2]

    mem[n-1] = a
    mem[n-2] = b


    return a + 2 * b

print(recur(N))