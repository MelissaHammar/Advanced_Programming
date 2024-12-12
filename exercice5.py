#The faster runner
runner1={
    "name":input("Name: "),
    "time":float(input("Time (in seconds) "))
}
runner2={
    "name":input("Name: "),
    "time":float(input("Time (in seconds) "))
}

if runner1["time"]>runner2["time"]:
    print("The faster runner is: ",runner2["name"])
elif runner1["time"]<runner2["time"]:
    print("The faster runner is: ",runner1["name"])
else: print(f"{runner1["name"]} and {runner2["name"]} have the same time")
