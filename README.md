# NasaAPOD
Simple Python Script Get Astronomy Picture of the Day

module require :
  - json
  - requests
  - os , system
  - random


we need ApiKey : https://api.nasa.gov/#signUp


One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery.


Example :
  - python nasaAPOD.py -k dHcONxPz7************************ -r
  - python nasaAPOD.py -k dHcONxPz7************************ 2019-1-9
