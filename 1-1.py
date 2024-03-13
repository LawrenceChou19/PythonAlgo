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
    
print('Single for loop design calculator series')
sum = 0
termi = 1 
x = 1.4
for i in range(0,6):
    print('Sum    is :',sum)
    print('termi  is :',termi)
    sum += termi
    print('Sum+   is :',sum)
    termi = termi * x/2
    print('termi* is :',termi)
    separate_section()
    