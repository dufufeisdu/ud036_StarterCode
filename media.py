class Media(object):
    """
    Create a media class contains information about this media
    Attributes:
        title(str): title of the media
        description(str): A short description of the media
        poster_image_url(str):the URL of the poster image
        trailer_youtube_url(str): youtube trailer URL of the media
    """

    def __init__(self, title, description, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
