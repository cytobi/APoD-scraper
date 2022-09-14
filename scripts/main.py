import requests
from bs4 import BeautifulSoup #to parse webpage
import subprocess

url = "https://apod.nasa.gov/apod/astropix.html" #url to get
baseurl = "https://apod.nasa.gov/apod/"

print("Getting webpage...")
page = requests.get(url) #get webpage

print("Passing to soup...")
soup = BeautifulSoup(page.content,  "html.parser")

print("Parsing.")
img = soup.find("img")
print("Parsing..")
img = img.parent
print("Parsing...")
img = img.attrs["href"]

imgurl = baseurl + img

print("Calling wget...")
cmd = ["wget", "-O", "../results/img.jpg", imgurl]
subprocess.Popen(cmd).communicate()