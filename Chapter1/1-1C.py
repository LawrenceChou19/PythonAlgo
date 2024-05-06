cnt=0
level=0

def add(cnt,level):
    print('before cnt = ',cnt)
    print('before level',level)
    if level >5:
        return cnt
    cnt += level
    print('level',level)
    print('cnt += level = ',cnt)

    print(f'End of the recursive {level}')
    return add(cnt,level+1)

cnt2 = 0
cnt2= add(cnt2,1)
print(f'cnt2 : {cnt2}')