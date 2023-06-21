
# creates a dictionary with food prices.
food_prices = {
    "chicken" : 1.59,
    "beef" : 1.99,
    "cheese" : 1.00,
    "milk" : 2.50, 
}

# assigned a variable for each food price.
chicken_price = food_prices["chicken"]
beef_price = food_prices["beef"]
cheese_price = food_prices["cheese"]
milk_price = food_prices["milk"]

# prints the price for food items from the variable it was assigned to.
print(chicken_price)
print(beef_price)
print(cheese_price)
print(milk_price)

# alternatively if we were to print the price with the item name 
# prints the dictionary with all its contents.
print(food_prices)

# creates a list of song with their artists.
playlist = [
    "The Weekend - Reminder",
    "Oliver Tree - Life goes on",
    "Conan Gray - Maniac",
    "Post Malone - WoW"
]

# prints the playlist to check if all the songs show up
print(playlist)

# prints the first song from my playlist
first_song = playlist[-4]  # or playlist[0]
print(first_song)

# accesses the 2nd and 3rd song as favorite songs and prints it.
fav_songs = playlist[1:3]   # slicing operator
print(fav_songs)

# changes the last song in the playlist to another song
playlist[3] = "J Cole - Middle child" 

# adds another song to the playlist and prints the new playlist.
playlist.append("Lana Del Ray - Love")

print(playlist)

# deletes the last song from the playlist and prints it.
playlist.pop()
print(playlist)

# how many songs are in the playlist. = 4
print(len(playlist))

# sorts the playlist in alphabetical order
print(sorted(playlist))
