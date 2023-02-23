import urllib.request
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
contestId = input("Enter the contest id: ") or "1"
submissionId = input("Enter your submission id: ") or "165594039"
url = "https://codeforces.com/contest/" + contestId + "/submission/" + submissionId
print('Retrieving the code form ' + url + '\n...')
html = urllib.request.urlopen(url).read()
print('...')

soup = BeautifulSoup(html, "html.parser")
for tag in soup('pre'):
    if tag.attrs.get('id') == 'program-source-text':
        content = tag.contents[0]
print(content)
        
