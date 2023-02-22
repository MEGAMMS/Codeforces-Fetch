import urllib.request
from bs4 import BeautifulSoup

url = "https://codeforces.com/contest/1/submission/165594039#program-source-text.html"
html = urllib.request.urlopen(url).read()

with open("output.txt", "wb") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")
tags = soup('pre')
