length = 10
width = 2
area = length * width
print("the area is " + str(area))

def area(length, width):
    return length * width

area_a = area(10, 2)
area_b = area(20, 2)
sum = area_a + area_b
print("the sum of the areas is " + str(sum))

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

def convert_seconds(secondss):
    hours = secondss // 3600
    minutes = (secondss - hours * 3600) // 60
    seconds = secondss - hours * 3600 - minutes * 60
    return hours, minutes, seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)