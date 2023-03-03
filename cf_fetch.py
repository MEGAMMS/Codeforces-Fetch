from bs4 import BeautifulSoup
import urllib.request
import json
import sys


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


def callApi(handle):
    urlApi = "https://codeforces.com/api/user.status?handle=" + handle
    print('Calling codeforces API...')
    try:
        jsonFile = urllib.request.urlopen(urlApi)
    except urllib.error.HTTPError:
        print("Wrong Handle.")
        sys.exit()
    except:
        print("Error in retrieval")
        sys.exit()

    return json.loads(jsonFile.read())