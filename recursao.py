#recursive is a function that call itself

#recursive function infinite loop
def regressive(i):
    print(i)
    regressive(i-1)

#recursive function with base case to interrupt
def regressive2(i):
    print(i)
    if i <= 1: # base case
        return 
    else: 
        regressive2(i-1)

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)
print(fat(4))


#call stack (pilha)
# all stack have two operations: push and pop
# all calls to a function go on the call stack  
# the call stack may can get very large and take up a lot of memory

def soma(arr):
    if arr == []:
        return 0
    else:
        return arr.pop(0)+soma(arr)

lista = [2,4,6]
print(soma(lista))



def myLen(arr):
    if len(arr) == 0:
        return 0
    return 1+myLen((arr[1:]))

print(myLen(lista))