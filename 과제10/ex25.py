keys = input().split() 
values = input().split()

x = dict(zip(keys, values))

del x['alpha']
del x['delta']

print(x)