x=range(20)
for y in x:
     if y%2==0:
         print(f"{y} is divisible by 2")
     elif y%3==0:
          print(f"{y} is divisible by 3")
     else:
        print(f"{y} is divisible by 2 or 3")
   

c=range(1,100)
for a in c:
     if a%5==0:
          print(f"{a} is divisible by 5")
     elif a%6==0:
          print(f"{a} is divisible by 6")
     elif a%7==0:
          print(f"{a} is divisible by 7")
     elif a%9==0:
          print(f"{a} is divisible by 9")
     else:
          print(f"{c} is divisible by 5 or 6 or 7 or 9")     
     