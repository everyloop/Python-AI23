def main():
    print("Start of main()")
    func_b()
    func_a()
    func_b()
    print("End of main()")

def func_a():
    print("Start of func_a()")

    func_b()

    print("End of func_a()")

def func_b():
    print("Start of func_b()")
    
    func_a()

    print("End of func_b()")

def print_hello(n):
    for i in range(n):
        print("hello")

def print_hello_recursive(n):
    print("hello")
    if n > 1: print_hello_recursive(n-1)
    return

print_hello_recursive(4)

#main()
