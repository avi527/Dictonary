def cubeFinder(n):
    cube={}
    for i in range(1,n):
        cube[i]=i**3
    return cube
print(cubeFinder(3))
