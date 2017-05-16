from bs4 import BeautifulSoup
import urllib2
import sys
import json

#Scrapes HTML data from the met office API 
class Scraper(object):

    def __init__(self, url):
        self.url = url      #Specified url to obtain data from

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    #Scrape HTML
    def scrape_html(self, url):
        #Use a header, this url gets funny about letting us scan its contents
        headers = {'User-Agent' : 'Mozilla 5.10'}
        #Generate a request using the given headers
        request = urllib2.Request(url, None, headers)
        #Gather the server response from that request
        response = urllib2.urlopen(request)
        #Scrape the html from the response
        html = response.read()
        #Return the html data
        return html
        