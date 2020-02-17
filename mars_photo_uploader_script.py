#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 01:04:17 2020

@author: tylerwilson
"""

from __future__ import print_function
import httplib2
from oauth2client import tools
import credentials
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

##sending params to get credentials
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'MARS PHOTO UPLOADER'
creds_obj = credentials.credentials(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
credentials = creds_obj.get_credentials()

##creating link
http = credentials.authorize(httplib2.Http())
drive_service = build('drive', 'v3', http)

            
##upload files to mars_photos folder
def upload(filename,filepath,mimetype):
    folder_id = '1Ew6RTaoTrlJNfurpjQfHWaI6x9etGwH2'
    file_metadata = {'name': filename,'parents':[folder_id]}
    media = MediaFileUpload(filepath, mimetype=mimetype, resumable=True)
    file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()
    print('File ID: %s' % file.get('id'))
    
#photos
for i in range(201):
    upload('mars_img#'+str(i)+'.jpg','mars_img#' + str(i) + '.jpg','image/jpeg')

#csv
upload('mars_photos_metadata.csv','mars_photos_metadata.csv','text/csv')
    

       
       
       
       
       
       
       