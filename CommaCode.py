def items(List):
    for i in range(len(List)-1):
        print(List[i] , end=", ")
    print("and " ,List[-1] )

fruits = ["apple", "banana", "carrot", "muskmelon"]

items(fruits)