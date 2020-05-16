# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:39:15 2020

@author: Hao

This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.

Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

Try invoking your function with the input “Black Panther”.

HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.

"""
import requests_with_caching
import requests
import json

movie_name='fargo'
baseurl='https://tastedive.com/api/similar'
params={}
params['q']=movie_name
params['type']='movies'
params['limit']=5
rq=requests.get(baseurl,params)
js=json.loads(rq.text)
print(json.dumps(js,indent=4))


def get_movies_from_tastedive(movie_name):
    baseurl='https://tastedive.com/api/similar'
    params={}
    params['q']=movie_name
    params['type']='movies'
    params['limit']=5
    rq=requests.get(baseurl,params)
    js=json.loads(rq.text)
    return js


"""
Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
"""
def extract_movie_titles(js):
    lst=js['Similar']['Results']
    movie_lst=[x['Name'] for x in lst]
    return movie_lst

extract_movie_titles(get_movies_from_tastedive(movie_name))


#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

def get_related_titles(movie_lst):
    
    
movie_requests=["Black Panther", "Captain Marvel"]
full_lst=[]
for m in movie_requests:
    new_lst=extract_movie_titles(get_movies_from_tastedive(m))
    full_lst.append(new_lst)
flat_lst=[item for sublst in full_lst for item in sublst]
flat_lst=list(dict.fromkeys(flat_lst))

"""
Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.
"""

movie_title='black panther'
def get_movie_date(movie_title):
    baseurl='http://www.omdbapi.com/?t=black+panther'
    params={}
    params['q']=movie_title
    params['r']='Json'
    rq=requests.get(baseurl,params)
    js=json.loads(rq.text)
    return js
    

js={"Type":"movie","Title":"Baby Mama","Year":"2008","Rated":"PG-13","Released":"25 Apr 2008","Runtime":"99 min","Genre":"Comedy, Romance","Director":"Michael McCullers","Writer":"Michael McCullers","Actors":"Amy Poehler, Tina Fey, Greg Kinnear, Dax Shepard","Plot":"A successful, single businesswoman who dreams of having a baby discovers she is infertile and hires a working class woman to be her unlikely surrogate.","Language":"English","Country":"USA","Awards":"1 win & 5 nominations.","Poster":"https://m.media-amazon.com/images/M/MV5BMTYwNTc1Nzk1N15BMl5BanBnXkFtZTcwNjE4OTI2MQ@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.0/10"},{"Source":"Rotten Tomatoes","Value":"64%"},{"Source":"Metacritic","Value":"55/100"}],"Metascore":"55","imdbRating":"6.0","imdbVotes":"37,454","imdbID":"tt0871426","DVD":"09 Sep 2008","BoxOffice":"$60,269,340","Production":"Universal Pictures","Website":"http://www.babymamamovie.net/","Response":"True"}

print(json.dumps(js,indent=4))

lst=js['Ratings']
#rating=[r['Value'] for r in lst if r['Source']=='Rotten Tomatoes'][0].replace('%','')

rating=[r['Value'] if r['Source']=='Rotten Tomatoes' else '' for r in lst ]
if rating!='':
    num=rating[0].replace('%','')
else:
    num=0

{js['Title']: num}

test={'baby': 54, 'a':55,'b':76}
rec=test.keys()

{'Baby Mama': 64, 'The Five-Year Engagement': 63, 'Bachelorette': 56, 'The Heat': 65, 'Date Night': 67, 'Sherlock Holmes: A Game Of Shadows': 60, 'Yahşi Batı': 0, 'Eyyvah Eyvah': 0, 'Pirates Of The Caribbean: On Stranger Tides': 32, 'Prince Of Persia: The Sands Of Time': 36}
['Date Night', 'The Heat', 'Baby Mama', 'The Five-Year Engagement', 'Sherlock Holmes: A Game Of Shadows', 'Bachelorette', 'Prince Of Persia: The Sands Of Time', 'Pirates Of The Caribbean: On Stranger Tides', 'Eyyvah Eyvah', 'Yahşi Batı']
