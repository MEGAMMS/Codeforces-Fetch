import urllib.request

url = "https://codeforces.com/contest/1/submission/165594039#program-source-text.html"

fhand = urllib.request.urlopen(url)
f = open("output.txt", "wb")
# for line in fhand:
f.write(fhand.read())
