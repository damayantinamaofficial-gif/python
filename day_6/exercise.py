# Create a script that:
# Stores a list of your 5 favorite movies
# Prints them one by one
# Converts the list to a tuple and prints the tuple
movies = ["The dark knight", "Inception", "The matrix", "Interstellar", "The Lord of the rings"]

for movie in movies:
    print(movie)

movie_tuple = tuple(movies)    
print(movie_tuple)