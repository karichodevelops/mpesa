class Car:
    model = "BMW"
    colour = "Red"

    def park(self):
        print("am parking")

    def reverse(self, amount):
        print("reverse")


range = Car()
print(range.model)

range.park()