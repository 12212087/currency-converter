                                                           #Project of Internet Programing Language "Currency Converter"
print("Rate of Dollar =RS 82.83")
print("Rate of Euros =RS 80.72")
print("Rate of Yuan =RS 11.64")
print("Rate of Pound =RS 91.83")
print("Rate of Rubal =RS 1.33")
print("Rate of Canadian Rupees =RS 60.28")
print("Rate of Taka =RS 0.80")
print("Rate of Sri Lankan Rupess =RS 0.23")


amu=int(input("Enter the amount:"))


print("choice 1 to change amount in Dollar")
print("choice 2 to change amount in Euros")
print("choice 3 to change amount in Yuan")
print("choice 4 to change amount in Pound")
print("choice 5 to change amount in Rubal")
print("choice 6 to change amount in Canadian Dollar")
print("choice 7 to change amount in Taka")
print("choice 8 to change amount in Sri Lankan Rupees")


choice=int(input("Enter your choice:"))

if choice==1:
    d=amu//82.83
    print("RS:",d)
elif choice==2:
    e=amu//80.72
    print("RS:",e)
elif choice==3:
    y=amu//11.64
    print("RS:",y)
elif choice==4:
    p=amu//91.83
    print("RS:",p)
elif choice==5:
    r=amu//1.33
    print("RS:",r)
elif choice==6:
    c=amu//60.28
    print("RS:",c)
elif choice==7:
    t=amu//0.80
    print("RS:",t)
elif choice==8:
    s=amu//0.23
    print("RS:",s)
else:
    print("Choice Not Avialable")
print("Thank You")
print("Visit Again")

