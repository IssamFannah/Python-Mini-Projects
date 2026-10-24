
price = float(input("Enter the product price: "))
print(f"Product price is: {price}DH ")

loyal = input("Does the customer have a loyalty card? (yes/no): ")
if loyal == "yes":
    price = price - 10
    print(f"Ok, so your price is {price} ")

else:
    print("No discount applied ")

print("TVA est 20% ")
TVA = price * 0.20
TTC = price + TVA

print(f"Total price to pay is: {TTC}DH ")
