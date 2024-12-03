'''
파일명: Ex10-2-method-set.py

'''
# 교집합 intersection()
s1 = {'apple' , 'banana', 'cherry'}
s2 = {'apple' , 'banana', 'orange'}

result = s1.intersection(s2)
print(result)
print(s1 & s2)


# 합집합 union()
s1 = {'apple' , 'banana', 'cherry'}
s2 = {'apple' , 'banana', 'orange'}
result = s1.union(s2)
print(result)

# 차집합 difference()
s1 = {'apple' , 'banana', 'cherry'}
s2 = {'apple' , 'banana', 'orange'}
result1 = s1.difference(s2)
result2 = s2.difference(s1)
print(result1)
print(result2)
print(s1- s2)
print(s2- s1)
