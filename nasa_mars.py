#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:29:12 2020

@author: tylerwilson
"""

import requests
import urllib
import csv

## set parameter
my_api_key = "Dsn4DZhP7FkuhxbrFEy8Xphf5cqeeBfhvA5Zb9Gh"
date = "2016-2-2"
mars_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+ date + "&api_key="+ my_api_key
mars_photos = []


## retrieve json file
recv = requests.get(mars_url)
mars_json = recv.json()


## extract images
for i in range(len(mars_json["photos"])):
    img_url = mars_json["photos"][i]["img_src"]
    mars_photos.append(img_url)


## locally save images
for i in range(len(mars_photos)):
    urllib.request.urlretrieve(mars_photos[i], "mars_img#"+str(i)+".jpg")


##append our local image title to each image's metadata for convienence
for i in range(len(mars_json['photos'])):
    mars_json['photos'][i]["local_id"] = "mars_img#"+str(i)+".jpg"


##get column headers for our csv
cols = list(mars_json['photos'][0].keys())


##create csv file
with open('mars_photos_metadata.csv','w',newline = '') as csvfile:
    #header
    writer = csv.DictWriter(csvfile, fieldnames = cols)
    writer.writeheader()
    #rows
    for i in range(len(mars_json['photos'])):
        writer.writerow({
                'id':mars_json['photos'][i]['id'],
                'sol':mars_json['photos'][i]['sol'],
                'camera':mars_json['photos'][i]['camera'],
                'img_src':mars_json['photos'][i]['img_src'],
                'earth_date':mars_json['photos'][i]['earth_date'],
                'rover':mars_json['photos'][i]['rover'],
                'local_id':mars_json['photos'][i]['local_id']})