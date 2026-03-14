import requests
import re

API_KEY = "232f1f58d91cd2f188444e66b0f6e56b"


def clean_title(title):

    # remove year
    title = re.sub(r"\(\d{4}\)", "", title)

    # fix comma titles
    if ", The" in title:
        title = "The " + title.replace(", The", "")
    if ", A" in title:
        title = "A " + title.replace(", A", "")

    # remove quotes
    title = title.replace("'", "")

    return title.strip()


def get_movie_poster(movie):

    try:

        title = clean_title(movie)

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"

        response = requests.get(url)

        data = response.json()

        if data["results"]:
            poster_path = data["results"][0]["poster_path"]

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return None

    except:
        return None