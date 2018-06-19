#function definition
def add(x,y):
    result = x+y
    print('Result of {} and {} is {}'.format(x,y,result))

add(10,20)

def mul(a,b):
    val = a*b
    return val

val = mul(10,20)
print(val)

def sub(x=5,y=5):
    res = x-y
    return res

res = sub(x=10)#override values
print(res)