#Magic square or sudoko program

r=3
c=3
count=1
for i in range(r):
    for j in range(c):
        print(count, end='')
        count+=1
    print("")