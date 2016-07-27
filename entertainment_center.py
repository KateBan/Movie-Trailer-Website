# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# Creating instances of the Movie class

the_internship = media.Movie("The Internship",
                        "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=cdnoqCViqUo")


dangerous_beauty = media.Movie("Dangerous Beauty",
                               "https://upload.wikimedia.org/wikipedia/en/5/5b/Dangerous_beauty_poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=xYu37jF0d3c")


eat_pray_love = media.Movie("Eat, Pray, Love",
                            "https://upload.wikimedia.org/wikipedia/en/c/c4/Eat%2C_Pray%2C_Love_%E2%80%93_Elizabeth_Gilbert%2C_2007.jpg",  # noqa
                            "https://www.youtube.com/watch?v=mjay5vgIwt4")


the_last_samurai = media.Movie("The Last Samurai",
                               "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",  # noqa
                               "https://www.youtube.com/watch?v=T50_qHEOahQ")


memories_of_a_geisha = media.Movie("Memoirs of a Geisha",
                                   "https://upload.wikimedia.org/wikipedia/en/0/09/Memoirs_of_a_Geisha_Poster.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=i_TXEEgNiWE")  # noqa


inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",  # noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Adding the instances of the Movie class into a list

movies = [the_internship, dangerous_beauty, the_last_samurai,
          memories_of_a_geisha, eat_pray_love, inception]

# Calling the extrenal rendering function

fresh_tomatoes.open_movies_page(movies)

