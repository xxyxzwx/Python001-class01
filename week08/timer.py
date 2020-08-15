import time

def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        print(time.time() - start)
    return inner

@timer
def foo2(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

foo2(1,2,3,4,5)