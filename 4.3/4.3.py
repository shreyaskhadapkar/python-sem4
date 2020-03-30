import os
reclen=20
with open("cars.bin",'wb') as f1:
    n=int(input('How many entries?'))
    for i in range(n):
        car=input('enter car name:')
        ln=len(car)
        car=car+(reclen-ln)*' '
        car=car.encode()
        f1.write(car)

with open("cars.bin",'rb') as f:
    n=int(input('Enter record number?'))
    f.seek(reclen * (n-1))
    str=f.read(reclen)
print(str.decode())
 
size=os.path.getsize('cars.bin')
print('Size of file={} bytes'.format(size))
n=int(size/reclen)
print('No. of records={}'.format(n))
with open('cars.bin','r+b') as f:
    name=input('Enter car name :')
    name=name.encode()
    newname = input('enter new name:')
    ln = len(newname)
    newname = newname + (20 - n) * " "
    newname = newname.encode()
    position = 0
    found = False
    for i in range(n):
        f.seek(position)
        str = f.read(20)
    if name in str:
        print('Updated recordno:', (i + 1))
        f.seek(-20, 1)
        f.write(newname)
        position += reclen
 
    if not found:
        print('car not found')

size=os.path.getsize('cars.bin')
n=int(size/reclen)
f1=open('cars.bin','rb')
f2=open('file2.bin','wb')
car=input('Enter car name to delete:')
ln=len(car)
car=car+(reclen-ln)*" "
car=car.encode()
for i in range(n):
    str=f1.read(reclen)
    if(str!=car):
        f2.write(str)
print('Record deleted….')
f1.close()
f2.close()
os.remove("cars.bin")
