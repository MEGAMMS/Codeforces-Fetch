import json
import urllib.request
import sys
import os
from bs4 import BeautifulSoup

MAXERROR = 5
errorCnt = 0
def getCode(contestId, submissionId):
    url = "https://codeforces.com/contest/" + contestId + "/submission/" + submissionId
    print('Retrieving the code form ' + url)
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
print("There is",len(info["result"]),"submission to retrieve")

for i,sub in enumerate(info["result"]):
    if(errorCnt >= MAXERROR):sys.exit()
    filePath = path + "\\" + str(sub["id"])+ ".txt"
    print(i+1,end="- ")
    if(os.path.isfile(filePath)):
        print(str(sub["id"]),"is already in the dir.")
        continue
    try:
        Code = getCode(str(sub["contestId"]), str(sub["id"])).replace("\r\n","\n").replace("\r","\n")
    except:
        print("Failed!")
        errorCnt += 1
        continue
    with open(filePath, 'w', encoding="utf-8") as file:
        file.write(Code)
