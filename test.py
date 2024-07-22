import pydoc
import inspect

def fibonacci(x: 'int', output: 'list' = []) -> 'list':
    if x == 0:
        return output
    else:
        if len(output) < 2:
            output.append(1)
            fibonacci(x-1, output)
        else:
            output.append(output[-1] + output[-2])
            fibonacci(x-1, output)
        return output


print(fibonacci("a"))
print(fibonacci.__annotations__)
#pydoc.help()
print(inspect.getfullargspec(fibonacci))
