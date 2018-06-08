import os

def getDirSize(dir):
    for (root, dirs, files) in os.walk(dir, False):
        Size = 0

    for filename in files:
        Size += os.path.getsize(os.path.join(root, filename))
        print (root,Size / 1024)

path = "/Users/huangweiqi/Projects/OnceCompany/ComLan/"
getDirSize(path)
