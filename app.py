import json
import urllib.request
import sys
import os
from bs4 import BeautifulSoup


def getCode(contestId, submissionId):
    url = "https://codeforces.com/contest/" + contestId + "/submission/" + submissionId
    print('Retrieving the code form ' + url + '\n...')
    try:
        html = urllib.request.urlopen(url).read()
    except:
        print("Error in retrieval")
        return

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup('pre'):
        if tag.attrs.get('id') == 'program-source-text':
            content = tag.contents[0]
    return content


handle = input("Enter your handle: ") or "MEGAMMS"

urlApi = "https://codeforces.com/api/user.status?handle=" + handle
print('Calling codeforces api...')
try:
    jf = urllib.request.urlopen(urlApi).read()
except:
    print("Error in retrieval")
    sys.exit()


path = os.path.join(os.getcwd(),"Subs")

os.makedirs(path,exist_ok = True)

info = json.loads(jf)
for sub in info["result"]:
    with open(path + "\\" + str(sub["id"])+ ".txt",'w') as file:
        file.write(getCode(str(sub["contestId"]), str(sub["id"])))
