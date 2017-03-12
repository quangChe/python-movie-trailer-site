# The media module is used to create unique instances of movies and
# the fresh_tomatoes module is used to render the movie page.
import media
import fresh_tomatoes

# The class format can be found in: media.Movie.__doc__
iron_man = media.Movie("Iron Man (2008)", "After being held captive in an Afg"
                       "han cave, billionaire engineer Tony Stark creates a u"
                       "nique weaponized suit of armor to fight evil.", "http"
                       "s://images-na.ssl-images-amazon.com/images/M/MV5BMTcz"
                       "NTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_C"
                       "R0,0,674,1000_AL_.jpg", "https://www.youtube.com/watc"
                       "h?v=8hYlB38asDY")

captain_america = media.Movie("Captain America (2011)", "Steve Rogers, a reje"
                              "cted military soldier transforms into Captain "
                              "America after taking a dose of a Super-Soldier"
                              " serum. But being Captain America comes at a p"
                              "rice as he attempts to take down a war monger "
                              "and a terrorist organization.", "https://image"
                              "s-na.ssl-images-amazon.com/images/M/MV5BMTYzOT"
                              "c2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_SY1"
                              "000_CR0,0,640,1000_AL_.jpg", "https://www.yout"
                              "ube.com/watch?v=jh8q4y7tbuQ")

thor = media.Movie("Thor (2011)", "The powerful but arrogant god Thor is cast"
                   " out of Asgard to live amongst humans in Midgard (Earth),"
                   " where he soon becomes one of their finest defenders.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BOGE4"
                   "NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQ"
                   "XVyNTgzMDMzMTg@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "http"
                   "s://www.youtube.com/watch?v=JOddp-nlNvQ")

the_avengers = media.Movie("The Avengers (2012)", "Earth's mightiest heroes m"
                           "ust come together and learn to fight as a team if"
                           " they are to stop the mischievous Loki and his al"
                           "ien army from enslaving humanity.", "https://imag"
                           "es-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1"
                           "MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_C"
                           "R0,0,675,1000_AL_.jpg", "https://www.youtube.com/"
                           "watch?v=NPoHPNeU9fc")

civil_war = media.Movie("CA: Civil War (2016)", "Political interference in th"
                        "e Avengers' activities causes a rift between former "
                        "allies Captain America and Iron Man.", "https://imag"
                        "es-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjA"
                        "xMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,6"
                        "74,1000_AL_.jpg", "https://www.youtube.com/watch?v=2"
                        "1HP6OFn5OE")

deadpool = media.Movie("Deadpool (2016)", "A fast-talking mercenary with a mo"
                       "rbid sense of humor is subjected to a rogue experimen"
                       "t that leaves him with accelerated healing powers and"
                       " a quest for revenge.", "https://images-na.ssl-images"
                       "-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFt"
                       "ZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg", "https://"
                       "www.youtube.com/watch?v=ONHBaC-pfsk")


# The open_movies_page() function from the fresh_tomatoes module
# will load whichever movie instances we pass into it and render the
# movies on the page.
movies = [iron_man, captain_america, thor, the_avengers, civil_war, deadpool]
fresh_tomatoes.open_movies_page(movies)
