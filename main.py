#Notice

print("=- NZ:P Mapping Script Generator -=")
print("       (c) Ian Bowling 2018")
print("-----------------------------------")
print("NOTE: If an option is left blank,")
print("default values will be used.")
print("-----------------------------------")

#Input

a = input("Map Name (case sensitive): ")
b = input("Start/Debug Message: ")
c = input("Starting Round: ")
d = input("Starting Weapon: ")
if d != "":
    e = input("Primary magazine: ")
    f = input("Primary reserve ammo: ")
g = input("Secondary Weapon: ")
if g != "":
    h = input("Secondary magazine: ")
    i = input("Secondary reserve ammo: ")

#Conversion

file = open(a + ".nzd", "a+")
file.write("game {")
if b != "":
    file.write("\n    startdbg:"+b)
if c != "":
    file.write("\n    startrnd:"+c)
if d != "":
    file.write("\n    wpn:"+d)
    file.write("\n    mag:"+e)
    file.write("\n    res:"+f)
if g != "":
    file.write("\n    wpn2:"+g)
    file.write("\n    mag2:"+h)
    file.write("\n    res2:"+i)
file.write("\n}")

#Prompt

print("-----------------------------------")
print("Finished writing to "+a+".nzd, place")
print("file in nzp/data/maps and launch!")
