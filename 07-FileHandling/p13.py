movie_titles = ["FF1", "FF2", "FF3", "FF4", "FF5"]

file = open("movies.txt", "a")
file.write("\n".join(movie_titles))
file.close()
