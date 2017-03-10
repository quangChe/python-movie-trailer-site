import media
import fresh_tomatoes


iron_man = media.Movie("Iron Man (2008)",
                       "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

captain_america = media.Movie("Captain America (2011)",
                              "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a Super-Soldier serum. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=jh8q4y7tbuQ")

thor = media.Movie("Thor (2011)",
                   "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

the_avengers = media.Movie("The Avengers (2012)",
                          "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=NPoHPNeU9fc")

civil_war = media.Movie("CA: Civil War (2016)",
                        "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=21HP6OFn5OE")

deadpool = media.Movie("Deadpool (2016)",
                       "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

movies = [iron_man, captain_america, thor, the_avengers, civil_war, deadpool]
fresh_tomatoes.open_movies_page(movies)


