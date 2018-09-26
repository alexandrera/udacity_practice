import media
import fresh_tomatos

toy_story = media.Movie("Toy Story",
                        "A story of a child that own toys which comes to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

cloud_atlas = media.Movie("Cloud Atlas",
                          "Impossible to describe with some few words. It is a masterpiece.",
                          "https://upload.wikimedia.org/wikipedia/pt/7/7d/Cloud_Atlas.jpg",
                          "https://www.youtube.com/watch?v=hWnAqFyaQ5s")

rocknrolla = media.Movie("Rock'n Rolla",
                         "Movie about british gangsters doing a lot of gangster stuff.",
                         "https://upload.wikimedia.org/wikipedia/pt/3/34/Rocknrolla_poster_promocional.jpg",
                         "https://www.youtube.com/watch?v=TdpR8VuvbCM")

#movies = [toy_story, cloud_atlas, rocknrolla]
#fresh_tomatos.open_movies_page(movies)

print media.Movie.VALID_REATINGS