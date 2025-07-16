products={
    1: ["Rice", 60],
    2: ["Wheat Flour", 45],
    3: ["Sugar", 40],
    4: ["Milk", 25],
    5: ["Eggs (12 pcs)", 70],
    6: ["Cooking Oil", 130],
    7: ["Tea Powder", 90],
    8: ["Salt", 20],
    9: ["Bread", 30],
    10: ["Soap", 25]
}
for i in range(1,11):
    print(f'{i.{(data[i]["name"]).ljust(15," ")}:}{data[i]["price"]}')

items=list(map(int,input("enter the item indexes: ").split()))
