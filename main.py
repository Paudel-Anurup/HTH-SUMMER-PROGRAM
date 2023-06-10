
# a variable with a string value that holds my full name.
name = "Anurup Paudel"

# a variable with a string value that holds my nickname.
nick_name = 'Lucifer'

# a variable with an integer value that holds my age.
age = 23

# a variable with a boolean value that tells if i used python before.
used_python_before = True

# A variable that contains all my hobbies in a list
hobbies = ['Eat', 'Sleep', 'Code', 'Basketball','Games']

# A dictionary with key value pairs that depicts my favorite things
favorite_things = {
 'movie' : 'Interstellar',
 'food' : 'Pizza',
 'hobby' : hobbies[-3]   # accessing 'code' from my list of hobbies
}

print(
    f"\nHello World! My name is {name}, but many of my friends call me {nick_name}. I am {age} years old.\n"
    )

print(f"Has Python experience: {used_python_before}\n")

# A for loop to print my favorite things from the dictionary
for key in favorite_things.keys():
    print(f"My favorite {key} is {favorite_things[key]}.")

print(f"Here are some of my other hobbies {hobbies}")

all_vars = dict(vars())


