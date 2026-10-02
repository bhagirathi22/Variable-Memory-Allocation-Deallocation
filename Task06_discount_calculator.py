# Task6:
# Create a function that accepts the purchase amount.
# apply ₹5000 or more(20% discount)
#       ₹3000  to 4999(10% discount)
#       below ₹3000(5% discount)
# return discount amount and final payable amount

def calculate_discount(amount):
    if amount >= 5000:
        discount_rate = 0.20
    elif amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = amount * discount_rate
    final_amount = amount - discount_amount
    return discount_amount, final_amount


purchase_amount = float(input("Enter the purchase amount in rupees: "))
discount, payable = calculate_discount(purchase_amount)

print("Discount amount: Rs.", format(discount, ".2f"))
print("Final payable amount: Rs.", format(payable, ".2f"))