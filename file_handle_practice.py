a = 'First string added'
with open('check.txt', 'a') as f:
    f.write(a + '\n')
    f.write('the second one \n')
b = open('check.txt','r')
print(b.read())
b.close()
ss = 'second'
flag = False
with open('check.txt', 'r+')as s:
    for line in s:
        if ss in line:
            flag = True
    if flag == False:
        s.write('New Addition\n')
    s.write('New\n')