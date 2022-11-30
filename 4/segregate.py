import os

f = open("data.txt", "r")
i=0
for x in f:
  k = int(x)
  os.system('mv '+str(i)+'.jpg '+str(k)+'/')
  i = i + 1
  
