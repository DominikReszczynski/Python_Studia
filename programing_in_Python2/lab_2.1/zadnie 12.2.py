import math
def squer (rays):
    if rays>0:
        volume=(4/3)*math.pi*(rays**3)
        field=4*math.pi*(rays**2)
        return volume, field
    else:
        return "promień mniejszy od zera"
def cone (hight,ray):
    if hight>0 and ray>0:
        side=hight**2+ray**2
        volume=(1/3)*math.pi*(ray**2)*hight
        field=math.pi*ray*(ray+side)
        return volume, field, side
    else:
        return "wysokość albo promień mniejsze od zera"
def cube (side):
    if side>0:
        volume=side**3
        field=6*side**2
        return volume, field
    else:
        return "długość mniejszy od zera"

ray=int(input("podaj promień: "))
if ray>0:
    volumeSquer, fieldSquer= squer(ray)
    print("dla promienia", ray, "objętość to", volumeSquer, "pole to:", fieldSquer)
else:
    print(squer(ray))

height=int(input("podaj wysokość dla stożka: "))
if ray>0 and height>0:
    volumeCone, fieldCone, sideCone= cone(height,ray)
    print("dla promienia", ray, "dla wysokości", height, "dla długości boku", sideCone, "objętość to", volumeCone, "pole to:", fieldCone)
else:
    print(cone(height,ray))

cubeSide=int(input("podaj bok sześcianu: "))
if cubeSide>0:
    volumeCube, fieldCube=cube(cubeSide)
    print("dla boku o długości", cubeSide, "objętość to", volumeCube, "pole to:", fieldCube)
else:
    print(cube(cubeSide))