name = "mia"
number = len(name) * 9

print("Hello, " + name + "! Your number is " + str(number))

name = "Carol"
number = len(name) * 9

print("Hello, " + name + "! Your number is " + str(number))



def lucky_number(name):
    number = len(name) * 9
    print("Hello, " + name + "! Your number is " + str(number))

lucky_number("Mia")
lucky_number("Carol")


def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days(month = "June", days = 30)
month_days(month = "July", days = 31)

june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")

def rectangle_area(base, height):
	area = base*height  # the area is base*height
	print("The area is " + str(area))

rectangle_area(10, 5)