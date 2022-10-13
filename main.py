from urllib import response
import requests
from bs4 import BeautifulSoup

 
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"




response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup)

all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movie_ranked = movie_titles[::-1]
# print(movie_titles)
# print(movie_ranked)


with open('top_movies', 'w') as f:
    for line in movie_ranked:
        f.write(f"{line}\n")





