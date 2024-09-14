def fib(n):
    # base conditions
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive calls
    return fib(n-1) + fib(n-2)  

def main():
    print(fib(5))

if __name__ == "__main__":
    main()
    
# the function call stack is as follows 

# fib(5) is called from the main
# fib(5) calls -> fib(4) and fib(3) .............(ref.: line 8)
# fib(4) calls -> fib(3) and fib(2)
# fib(3) calls -> fib(2) and fib(1)
# fib(2) calls -> fib(1) and fib(0)

# here fib(1) and fib(0) returns 1 and 0 respectively -> base conditions of the function 
# hence fib(2) returns the value 1+0 = 1 .......... to fib(3)

#  in fib(3)
#           fib(2) returned value 1 
#           fib(1) returns value 1 -> (base case)
# hence fib(3) returns the value 1+1 = 2 .......... to fib(4)

#  in fib(4)
#           fib(3) returned value 2
#           fib(2) returns value 1 -> (computed earlier)
# hence fib(4) returns the value 2+1 = 3 .......... to fib(5)

#  in fib(5) 
#           fib(4) returned value 3
#           fib(3) returns value 2 -> (computed earlier)
# hence fib(5) returns the value 2+3 = 5 .......... to main function 

# and then we have the output of "5"  on the call of the function fib(5) 