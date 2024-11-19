import time
import requests
import json


HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MWIzODcwMDhhMDQ4NWEwZDU4N2U4OGQxNGQwY2QzZCIsIm5iZiI6MTcyMTcyOTc1Ni43MTcyMTIsInN1YiI6IjY2OWY4MjAwNDA4NmU3OGU1MGNkZDBiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZX--77MnS6COxN8sJj6TzG6d3ibSPS2On12ucFFed3s"
}

for page_num in range(1, 11):
    time.sleep(20)
    print(f"I woke up, I'am on page {page_num}")
    url = f'https://api.themoviedb.org/3/movie/popular?language=en-US&page={page_num}'
    res = requests.get(url,
        headers=HEADERS
    )
    print(url)
    print(res.status_code)
    data:dict = json.loads(res.text)
    movies_list = data.get('results',[])
    with open('file.txt', 'a') as f:
        for movie in movies_list:
            f.writelines([
                f"-Name: {movie['original_title']}\n",
                f"-Description: {movie['overview']}\n",
                f'-Date: {movie['release_date']}\n',
                f'-Poster: {movie['poster_path']}\n',
                f'-Rating: {movie['vote_average']}\n',
            ])
            if movie != movies_list[-1]:
                f.write("-----------------------------------\n")
#TODO:
#save all info about films in movies.txt : 1. Poster 2.Rating 3.Release Date 4.Title 5.Overview
#Well Organized

