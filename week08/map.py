'''
容器序列：list, tuple, collections.deque
扁平序列：str
可变序列：list, dict, collections.deque
不可变序列：str, tuple
'''
#map
def cal(x):
    return x * 2

def maplike(func, list):
    new_list = []
    for i in list:
        new_list.append(func(i))
    return new_list.__iter__()

list1 = [1, 2, 3, 4, 5]
list2 = maplike(cal, list1)
print(list2)
