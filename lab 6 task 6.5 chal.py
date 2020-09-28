count=1
total=0
rubric=0
while rubric==0:
    no=int(input("Enter number %d:"%(count)))
    total=total+no
    count=count+1
    average=total/10
    if no==-1:
        break
print("Average:", average)
