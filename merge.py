f1 = open("file1.txt","r")
data1 = f1.read()
f1.close()
f2=open("file2.txt","r")
data2=f2.read()
f2.close()


merged = open("merged.txt","w")
merged.write(data1)
merged.write("\n")#optional newline between contents
merged.write(data2)
merged.close()
print("files merged into merged.txt")