# In the first blank, we should complete the incomplete function and make function to return the result after conversion

def convert_distance(miles):
    km = miles*1.6
    return km

my_trip_miles = 55

# In this blank, we have to convert my_trip_miles to kilometers by calling the above defined function

my_trip_km = convert_distance(my_trip_miles)

# Here, we are printing the result after the conversion

print("The distance in kilometers is " + str(my_trip_km))

# Here, we are calculating the number of kilometers in round trip by doubling the above result.

print("The round-trip in kilometers is " + str(my_trip_km*2))