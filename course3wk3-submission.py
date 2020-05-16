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
import json

def get_movies_from_tastedive(movie_name):
    baseurl='https://tastedive.com/api/similar'
    params={}
    params['q']=movie_name
    params['type']='movies'
    params['limit']=5
    rq=requests_with_caching.get(baseurl,params)
    js=json.loads(rq.text)
    return js

def extract_movie_titles(js):
    lst=js['Similar']['Results']
    movie_lst=[x['Name'] for x in lst]
    return movie_lst
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
def get_related_titles(movie_requests):
    full_lst=[]
    for m in movie_requests:
        new_lst=extract_movie_titles(get_movies_from_tastedive(m))
        full_lst.append(new_lst)
    flat_lst=[item for sublst in full_lst for item in sublst]
    flat_lst=list(dict.fromkeys(flat_lst))
    return flat_lst
    
def get_movie_data(movie_title):
    baseurl='http://www.omdbapi.com/'
    params={}
    params['t']=movie_title
    params['r']='json'
    rq=requests_with_caching.get(baseurl,params)
    js=json.loads(rq.text)
    return js


def get_movie_rating(js):
    lst=js['Ratings']
    rating=[r['Value'] for r in lst if r['Source']=='Rotten Tomatoes']
    if rating!=[]:
        num=rating[0].replace('%','')
    else:
        num=0
    return int(num)

def get_sorted_recommendations(movie_lst):
    lst=get_related_titles(movie_lst)
    ratings=[get_movie_rating(get_movie_data(m)) for m in lst]
    movie_dict=dict(zip(lst,ratings))
    sort_dict=sorted(movie_dict, key=lambda k: (movie_dict[k],k), reverse=True)
    return sort_dict

