class Movie():
    """
    This class is used to create unique movie instances. Each movie
    instance may contain four arguments.

    Example:

        <example1> = media.Movie('title', 'plot', 'poster url',
                                 'trailer url')

        <example2> = media.Movie('title', 'plot', 'poster url',
                                 'trailer url')

    Note:
        This class can only take arguments in the form of a string.
    """

    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
