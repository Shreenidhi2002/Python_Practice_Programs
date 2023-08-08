#weight convertor program

weight = float(input("Weight :"))

print("Enter l if weight is in lbs and u want in kg or k otherwise")
value = input()
if value.lower() == 'l':
    weight *= 0.45
    print(f"your are {weight} kilogram")
elif value.lower() =='k':
    weight *= 2.2
    print(f"you are {weight} pounds")
