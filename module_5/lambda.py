def func(a, b): 
    return a * b

print((lambda x,y: x*y)(2,3))

# Higher order functions 
# = Functions that take other functions as arguments and/or return functions as their return values

# Example: map
def my_map(myfunc, myiterable):
    results = []
    for item in myiterable:
        result = myfunc(item)
        results.append(result)
    return results

myiterable = [1,2,3,4,5]

times_three = my_map(lambda x: x*3, myiterable)
print(times_three)