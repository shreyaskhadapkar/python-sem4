import os

os.mkdir('python')

print("Current working directory")
print(os.getcwd())
print()

print("Changing the Current working directory\n")
os.chdir('python')
print("Dir changed")

print("after changing Current working directory\n")
print(os.getcwd())
print()

os.mkdir("django")
os.mkdir("flask")
os.mkdir("others")
os.mkdir("frameworks")
print("Removing the  directory\n")
os.rmdir("others")
print("Dir removed")


print("List of dir \n")
path = os.getcwd()
list=os.listdir(path)
print(list)

print("Checking a file or not")
res=os.path.isfile("Django")
print(res)

print("Checking a directory or not")
res=os.path.isdir("Django")
print(res)