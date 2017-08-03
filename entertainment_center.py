import parse_data
import media


def generate_movies():
    """
    Generate media instance and append them into an Array, function
    will return that array
    """
    data = parse_data.parse_json_data()
    length = len(data)
    movies = []
    for x in range(0, length):
        da = data[x]
        movies.append(media.Media(
            da["title"], da["description"], da["poster_image_url"],
            da["trailer_youtube_url"]))
    return movies
