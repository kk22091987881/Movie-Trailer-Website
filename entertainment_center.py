import fresh_tomatoes
import media

#creating instances for Movie
Rise_of_an_empire = media.Movie("300: Rise of an Empire",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcS2L0J4EY3rzzJa7qUYVLEaqE8g9tzXAnTwnsJcYw_4RIraGENR",
                   "https://www.youtube.com/watch?v=2zqy21Z29ps")
Black_Water = media.Movie("Black Water",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcSWwM25A2np6mcmDIItrxBCIDKDClITAUnmMvB5CQDgr2Znvq-t",
                        "https://www.youtube.com/watch?v=8yBWq-75DX0")
Jaws = media.Movie("Jaws",
                   "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",
                   "https://www.youtube.com/watch?v=U1fu_sA7XhE")
Mission_impossible = media.Movie("Mission: Impossible Rogue Nation",
                           "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                           "https://www.youtube.com/watch?v=gOW_azQbOjw")
Raging_Bull = media.Movie("Raging Bull",
                        "http://bttm.co.uk/wp-content/uploads/2015/11/Raging-Bull.jpg",
                        "https://www.youtube.com/watch?v=yUp6d79WRVI")
The_Conjuring = media.Movie("The Conjuring",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcQnHDbJFDDZYC5g9gHa6-NqBE8JUet_iRIPXJym8CtaHsVQa76M",
                          "https://www.youtube.com/watch?v=ejMMn0t58Lc")
#creating an array to store the instances created for the Movie
array=[Rise_of_an_empire,Black_Water,Jaws,Mission_impossible,Raging_Bull,The_Conjuring]
#pass the movies array to the function open_movies_page in fresh_tomatoes
fresh_tomatoes.open_movies_page(array)





    








    
