# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

shawshank = media.Movie("Shawshank Redemption",
	("Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms "
	"in prison for the murder, but he didn't commit the crimes."),
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	"https://www.youtube.com/watch?v=K_tLp7T6U1c")

groundhog_day = media.Movie("Groundhog Day",
	("Phil, a weatherman, is out to cover the annual emergence of the"
	" groundhog from its hole, but gets caught in a blizzard and is doomed"
	" to relive the same day over and over again."),
	"http://i43.tower.com/images/mm106995620/groundhog-day-bill-murray-dvd-cover-art.jpg",
	"https://www.youtube.com/watch?v=tSVeDx9fk60")

hard_days_night = media.Movie("A Hard Day\'s Night",
	("The Beatles in their feature film debut, one of the greatest "
	"rock-and-roll comedy adventures ever."),
	"https://cinematiccobwebs.files.wordpress.com/2010/05/a-hard-days-night-poster1.jpg",
	"https://www.youtube.com/watch?v=PeWS5HtCpU4")

taxi_driver = media.Movie("Taxi Driver",
	("Disturbed loner Travis Bickle (Robert De Niro) takes a job as a cabbie, "
	"growing increasingly detached from reality."),
	"https://images-na.ssl-images-amazon.com/images/I/514wPTpgNwL.jpg",
	"https://www.youtube.com/watch?v=NonYMdocz68")

apocalypse_now = media.Movie("Apocalypse Now",
	("Martin Sheen is Army Captain Willard - a troubled man sent on a "
	"dangerous and mesmerizing odyssey into Cambodia to assassinate a "
	":renegade American colonel named Kurtz (Marlon Brando)."),
	"https://files.graphiq.com/7522/media/images/t2/Apocalypse_Now_6820708.jpg",
	"https://www.youtube.com/watch?v=snDR7XsSkB4")

talladega_nights = media.Movie("Talladega Nights",
	("The story of NASCAR racing sensation Ricky Bobby, whose \"win at all "
	"costs\" approach has made him a national hero."),
	"https://images-na.ssl-images-amazon.com/images/I/51X3fTckTpL.jpg",
	"https://www.youtube.com/watch?v=myKtVl8N7jU")

movies = [shawshank, groundhog_day, hard_days_night, taxi_driver,
	apocalypse_now, talladega_nights]

fresh_tomatoes.open_movies_page(movies)
