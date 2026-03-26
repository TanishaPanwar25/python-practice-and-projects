Amount=int(input("Enter Total Bill Payment"))
Tip=int(input("Enter Tip"))
Total_Amount=Amount+Tip
print("----Your Total_Amount is",Total_Amount,"-----")
Member=int(input("Enter How many member"))
Child_Count=int(input("How many Child "))
Adult_Count=int(input("How many Adult"))
if Child_Count+Adult_Count == Member:
    total_Distribution=Total_Amount/Member
    print("total_Distribution",total_Distribution)
    percent=int(input("how many % you want that child pay less"))
    Less_Amount=total_Distribution*(percent/100)
    print("child pay 30% less amount compare to adult (Less_Amount)",Less_Amount)
    print("Per Child Pay",total_Distribution-Less_Amount)
    extra_For_Adult=Less_Amount/Adult_Count
    print("Per  Adult Pay",total_Distribution+(extra_For_Adult*Child_Count))