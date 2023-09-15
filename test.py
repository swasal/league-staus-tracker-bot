f=open("text formatter.txt", "r")

l=f.readlines()
print(l)

s="\n".join(l)
print(s)
f.close()

f=open("out.txt", "w")
f.write(s)
f.close()
