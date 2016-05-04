import fresh_tomatoes
import media


# Movie objects built from the Movie class in media.py 

interstellar = media.Movie("Interstellar", " An epic science fiction flim","Starring : Matthew McConaughey and Anne Hathaway", "Release Date : November 7, 2014",
                        "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://www.youtube.com/watch?v=0vxOhd4qlnA")

hobbit = media.Movie("Hobbit", " Desolation of Smaug", "Starring : Ian McKellen and Martin Freeman", "Release Date: December 13, 2013",
                        "http://upload.wikimedia.org/wikipedia/en/4/4f/The_Hobbit_-_The_Desolation_of_Smaug_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=OPVWy1tFXuc")

avengers = media.Movie("Avengers", " Age of Ultron", "Starring : Robert Downey Jr. and Jeremy Renner", "Release Date: May 1, 2015",
                        "http://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")

lucy = media.Movie("Lucy", " A perplexing blend of science and fiction", "Starring : Scarlett Johansson and Morgan Freeman", "Release Date: July 25, 2014",
                        "http://upload.wikimedia.org/wikipedia/en/1/14/Lucy_%282014_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=MVt32qoyhi0")

hercules = media.Movie("Hercules", " The story of Hercules", "Starring : Dwayne Johnson and John Hurt", "Release Date: July 25, 2014",
                        "http://upload.wikimedia.org/wikipedia/en/0/09/Hercules_%282014_film%29.jpg",
                        "https://www.youtube.com/watch?v=1L41RWI1oUg")

pirates = media.Movie("Pirates of the Caribbean", "The curse of the black pearl", "Starring : Johnny Depp and Geoffrey Rush", "Release Date: June 28, 2003", 
                        "http://upload.wikimedia.org/wikipedia/en/0/0e/Pirates_of_the_Caribbean_movie.jpg",
                        "https://www.youtube.com/watch?v=naQr0uTrH_s")

harrypotter = media.Movie("Harry Potter", "The Story of the Goblet of fire", "Starring : Daniel Radcliffe and Emma Watson", "Release Date: November 18, 2005", 
                        "http://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                        "https://www.youtube.com/watch?v=PFWAOnvMd1Q")

lordoftherings = media.Movie("The Lord of the rings", "The return of the king", "Starring : Elijah Wood and Viggo Mortensen", "Release Date: December 17, 2003", 
                        "http://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                        "https://www.youtube.com/watch?v=co9SNfJNDN8")

guardians = media.Movie("Guardians of the galaxy", "Cosmic Adventurers protecting our galaxy ","Starring : Chris Pratt and Dave Bautista", "Release Date: August 1, 2014", 
                        "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")


# creating an array of movie objects that will be used when creating the HTML page
movies = [interstellar,hobbit,avengers,lucy,hercules,pirates,harrypotter,lordoftherings,guardians]
# passes the movies array to the open_movies_page() function
fresh_tomatoes.open_movies_page(movies)
