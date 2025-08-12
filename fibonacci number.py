#program to generate fibonacci series
Terms=int(input("how many terms:"))
F1=0
F2=1
for i in range(0,Terms):
  if(i<=1):
    F3=i
  else:
    F3=F1+F2
    F1=F2
    F2=F3
  print(F3)
  
