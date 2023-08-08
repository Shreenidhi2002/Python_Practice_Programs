name = input("Enter name :")

length=len(name)
if length <3 :
    print("name should be atleast 3 characters")
elif length > 50 :
    print("name can be maximum of 50 characters")
else:
    print("name looks good")