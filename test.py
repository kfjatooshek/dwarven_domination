def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(be_awesome))

def adder(x):
    def egger(y):
        return x+y
    return egger

x = adder(1)
x = x(5)
print(x)

