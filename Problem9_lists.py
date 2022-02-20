#lists and mutability
a=[1,2]
b=[3,4]


def foo(lst1):
    lst1.append(1 + lst1[1])
    print(lst1)

def baz(lst2):
    print("starting of baz")
    lst2.append(2 + lst2[1])
    lst2 = []
    print(lst2)
    print("endinig og baz")

def bar(lst1, lst2):
    print("starting of bar")
    foo(lst2)
    print(lst1)
    print(lst2)
    baz(lst1)
    print(lst1)
    print(lst2)
    lst1, lst2 = lst2, lst1
    print(lst1)
    print(lst2)
    print("ending of bar")

bar(a,b)