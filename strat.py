
class DebitCard:
    def pay(self):
        print("Payment made using Debit Card")


class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")


class UPI:
    def pay(self):
        print("Payment made using UPI")


class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self):
        self.method.pay()


print("Select Payment Method")
print("1. Debit Card")
print("2. Credit Card")
print("3. UPI")

choice = int(input("Enter Choice: "))

if choice == 1:
    payment = Payment(DebitCard())
elif choice == 2:
    payment = Payment(CreditCard())
elif choice == 3:
    payment = Payment(UPI())
else:
    print("Invalid Choice")
    exit()

payment.make_payment()
