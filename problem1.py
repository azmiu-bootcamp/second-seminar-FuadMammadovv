num=int(input("Daxil edin:"))
sum=0
while(num!=0):
    remainder=num%10
    sum=sum+remainder
    num=num//10
print("Cavab   : ",sum)
