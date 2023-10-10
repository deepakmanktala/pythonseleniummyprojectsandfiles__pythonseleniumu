import os
def findall(directory):
    files=os.listdir(directory)
    print (files)
    for fl in files:
        path=os.path.join(directory+'/'+fl)
        if os.path.isdir(path):
            findall('c:/')
        else:
            dosomethingwithfile(path)
    return

findall('c:/')

