from separate import separate_section
'Find the maximum number of consecutive occurrences of the number 0'
n =int(input('Please input the number'))
count = 0
max_count = 0
while n>10:
    d= n%10
    print('d is ', d)
    print('n is ', n)
    if d ==0:
        count +=1
        max_count=max(max_count,count)
    else:
        count= 0
    n = n//10
    print('n is ', n)
    print('count is ',count)
    print('max_count is ',max_count)