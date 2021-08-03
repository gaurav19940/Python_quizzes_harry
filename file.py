
with open('new.txt','a') as f:
    f.write('for')
    with open('new.txt','r+') as fs:
        print(fs.read())
