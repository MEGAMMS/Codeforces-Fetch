import urllib.request
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import json
import sys

def getCode(contestId, submissionId):
    url = "https://codeforces.com/contest/" + contestId + "/submission/" + submissionId
    print('Retrieving the code form ' + url + '\n...')
    try:
        html = urllib.request.urlopen(url).read()
        print('...')
    except:
        print("Error in retrieval")
        return
    
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup('pre'):
      if tag.attrs.get('id') == 'program-source-text':
          content = tag.contents[0]
    return content



contestId = input("Enter the contest id: ") or "1791"
handle = input("Enter your handle: ") or "MEGAMMS"

url = "https://codeforces.com/api/contest.status?contestId=" + contestId + "&handle=" + handle

try:
    jf = urllib.request.urlopen(url).read()
except:
    print("Error in retrieval")
    sys.exit()


info = json.loads(jf)
for sub in info["result"]:
    print(getCode(str(sub["contestId"]),str(sub["id"])))


        
