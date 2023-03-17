from datetime import date

cusName = []
cusAddress = []
cusEmail = []
cusTotal = []
cusNetAmt = []
cusDiscount = []


def initialDisplay():
    display = f"""
    BhatBhateni Supermarket
        Kathmandu,Nepal
        {date.today()}"""
    print(display)


initialDisplay()
n = int(input("Enter the number of customers: "))


def inputInformation():
    # first for loop for different customers
    for i in range(n):
        cusName.append(input(f"Enter the name of customer [{i + 1}]: "))
        cusAddress.append(input(f"Enter the address of customer [{i + 1}]: "))
        cusEmail.append(input(f"Enter the email of customer [{i + 1}]: "))
        noOfItems = int(input(f"Enter the number of items of customer [{i + 1}] : "))
        totalPrice = 0
        for j in range(noOfItems):
            itemName = input(f"Enter the name of item [{j + 1}]: ")
            itemPrice = int(input(f"Enter the price of item [{j + 1}]: "))
            itemQty = int(input(f"Enter the quantity of item [{j + 1}]: "))
            totalPrice = totalPrice + itemPrice * itemQty
        cusTotal.append(totalPrice)
        netAmount, discount = calculation(totalPrice)
        cusNetAmt.append(netAmount)
        cusDiscount.append(discount)


def calculation(totalPrice):
    discount = 0
    if totalPrice <= 5000:
        discount = totalPrice * 0.05
    elif totalPrice <= 7000:
        discount = (5000 * 0.05) + (totalPrice - 5000) * 0.08
    elif totalPrice <= 10000:
        discount = (5000 * 0.05) + (2000 * 0.08) + (totalPrice - 7000) * 0.10
    else:
        discount = (5000 * 0.05) + (2000 * 0.08) + (3000 * 0.10) + (totalPrice - 10000) * 0.15
    # net amount after discount
    netAmount = totalPrice - discount
    return netAmount, discount


# function for displaying information by printing them
def displayInformation():
    for i in range(n):
        initialDisplay()
        print(f"""
        Customer Name: {cusName[i]}
        Customer Address: {cusAddress[i]}
        Customer Email: {cusEmail[i]}
        Total Price: {cusTotal[i]}
        Discount: {cusDiscount[i]}
        Net Amount: {cusNetAmt[i]}""")


inputInformation()
displayInformation()