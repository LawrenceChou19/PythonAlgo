def separate_section():
    print("-" * 80)
n = int(input('please input the number : '))
sum = 0 
for i in range(1,n+1):
    print('i   is : ',i)
    print('Sum is : ',sum)
    sum = sum + i
    print('Result : ',sum)
    separate_section()