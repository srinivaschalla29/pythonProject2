l=[5,6,56,45,435,54]
def demo_fun(n):
    if n>50:
        return True
    else:
        return False
data=list(filter(demo_fun,l))
print(data)