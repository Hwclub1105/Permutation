def binary(num, place):
    ans = ''
    while True:
        ans += str(num % 2)
        if num == 1 or num == 0:
            break
        num = num // 2
    ans = ans[::-1]
    while len(ans) < place:
        ans = (ans[::-1]+'0')[::-1]
    return ans

def bitwise(exp,key):
    out = ''
    for i in range(len(exp)):
        if key[i] == '1':
            out += exp[i]
    return out

def powerset(expression):
    pattern = [binary(i,len(expression)) for i in range(2**len(expression))]
    power_set = [''.join(sorted(bitwise(expression, i))) for i in pattern]
    return power_set     
        

x = 'aabcde'
y = 'abcefga'

def string_permutation(x,y):
    x_powerset = powerset(x)
    y_powerset = powerset(y)
    list = []

    for i in x_powerset:
        if i in y_powerset:
            list.append(i)
    print(max(list,key=len))

string_permutation('happy','kspdya')




