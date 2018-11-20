import fresh_tomatoes
import webbrowser

"""
  Defining the attributes of the Movies class.
              """


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
"""
  Creating a function to open the trailers for each movie when requested.
                                                                      """


def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
"""
By creating instances of the Movie class, that is my favorite movies.
And each of these instances contains the attributes of the Movie class.
"""

avatar = Movie("Avatar",
               "A marine on an alien planet",
               "https://vignette.wikia.nocookie.net/avatar/images/3/3f/Avatar-poster.jpg/revision/latest?cb=20091209142005&path-prefix=hu",
               "https://www.youtube.com/watch?v=d1_JBMrrYw8")

cars = Movie("Cars",
             "A racing car will stop in an inner city and learn that there are more important things than a competition.",
             "https://vignette.wikia.nocookie.net/disney/images/f/fc/Cars_-_Poster.jpg/revision/latest?cb=20140902165352",
             "https://www.youtube.com/watch?v=SbXIj2T-_uk")

ghost_rider = Movie("Ghost Rider",
                    "A stuntman sells his soul and must hunt down demons to have her back.",
                    "https://www.vintagemovieposters.co.uk/wp-content/uploads/2015/07/ghostriderquadlarge1.jpg",
                    "https://www.youtube.com/watch?v=tp12CD2A4NA")

im_a_legend = Movie("I'm a Legend",
                    "In 2012, after a major epidemic, scientist becomes the only man on Earth.",
                    "http://www.movieposter.com/posters/archive/main/59/MPW-29679",
                    "https://www.youtube.com/watch?v=dtKMEAXyPkg")

i_robot = Movie("Irobot",
                "In 2035, police officer Del Spooner (Will Smith) investigates a crime in which the prime suspect is a robot.",
                "https://upload.wikimedia.org/wikipedia/pt/e/ee/I%2C_Robot.jpg",
                "https://www.youtube.com/watch?v=rL6RRIOZyCM")

spider_man = Movie("Spider Man",
                   "Boy gets incredible powers and becomes a hero when bitten by a spider.",
                   "https://images-na.ssl-images-amazon.com/images/I/418zjk8EnnL.jpg",
                   "https://www.youtube.com/watch?v=TYMMOjBUPMM")

"""
Creating an array in which you have all the values of all instants created from the Movie class.
                                                                                             """
movies = [avatar, cars, im_a_legend, i_robot, spider_man, ghost_rider]

"""
Calling the fresh_ tomatoes function using the array values that contain the values of all instances.
                                                                                                  """
fresh_tomatoes.open_movies_page(movies)
