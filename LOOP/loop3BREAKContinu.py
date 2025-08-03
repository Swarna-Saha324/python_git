"""i=1
while i<=5:
    print(i)
    if(i==3):
        print("Breaking the loop at i =", i)
        break
    print("Loop continues...")
    print("End of loop iteration:", i)
    i += 1"""
i=0
while i<=5:
   if(i==3):
      i += 1
      continue # Skip the rest of the loop when i is 3
   print("Loop continues...")
   i += 1