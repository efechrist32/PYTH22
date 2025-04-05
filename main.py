def convert(bin):
    dec=0
    ans = []
    num=int(len(str(bin))-1)
    while num>0:
        for i in str(bin):
            print(num)
            ans.append((int(i)) * (num**2))
            num-=1
        print(ans)
        dec=sum(ans)
        print(dec)

input1 = int(input("Enter a binary number: "))
convert(input1)