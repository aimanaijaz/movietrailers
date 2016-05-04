import webbrowser

class Movie():
	""" This class provides a way to store movie related information """
        def __init__(self, movie_title, movie_storyline, movie_starring, movie_release_date, poster_image, trailer_youtube):
    	    """ Stores movie information when an instance of the class Movie is initialized """
            self.title = movie_title
            self.storyline = movie_storyline
            self.starring = movie_starring
            self.release_date = movie_release_date
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
    	    """ Shows a movie's trailer. Opens up a web browser and navigates to the trailer of a specific movie """
            webbrowser.open(self.trailer_youtube_url)
