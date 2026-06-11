import array as arr
b=arr.array('i',[2,4,-6,8,-3])
max=b[0]
min=b[0]
for i in range(len(b)):
    if b [i]>max:
        max=b[i]
for i in range(len(b)):
    if b [i]<min:
        min=b[i]
print(max-min)