from bs4 import BeautifulSoup
import urllib.request
import json
import sys


def getCode(contestId, submissionId):
    url = "https://codeforces.com/contest/" + \
        contestId + "/submission/" + submissionId
    print('Retrieving the code form ' + url)
    req = urllib.request.Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        html = urllib.request.urlopen(req).read()
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
        print(urlApi)
        req = urllib.request.Request(
            url=urlApi,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        jsonFile = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        print("Wrong Handle or somthing went wrong.")
        sys.exit()
    except:
        print("Error in retrieval")
        sys.exit()

    return json.loads(jsonFile.read())
