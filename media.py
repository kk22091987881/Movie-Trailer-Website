import webbrowser 
class Movie():
    """common base class for all Movie instances"""
    def __init__(self,movie_title,poster_image,trailer_youtube_url):
        self.movie_title=movie_title
        self.poster_image=poster_image
        self.trailer_youtube_url=trailer_youtube_url
        
    
    
