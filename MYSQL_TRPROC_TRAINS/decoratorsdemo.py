def outer():
    print("hello from Outer Function")
    def inner():
        print("Hello from inner function")
    inner()
d=outer()