def hint_username(username):
    if len(username) < 3:
        return "Username must be at least 3 characters long"
    elif len(username) > 20:
        return "Username must be less than 20 characters long"
    else:
        return "Username is valid"
print (hint_username(input("Enter a username: ")))


def is_positive(number):
  if number >0:
    return True


print(is_positive(5))
print(is_positive(-5))
print(is_positive(0))