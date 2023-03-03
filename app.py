import json
import sys
import os
from cf_fetch import getCode, callApi

MAXERROR = 10
errorCnt = 0

handle = input("Enter your handle: ") or "MEGAMMS"
info = callApi(handle)

path = os.path.join(os.getcwd(),"Subs")
os.makedirs(path,exist_ok = True)

with open("programmingLanguages.json","r") as file:
    extinctions = json.loads(file.read())


subs = list()
for sub in info["result"]:
    filePath = path + "\\" + str(sub["id"]) + "." + extinctions[sub.get("programmingLanguage", "txt")]
    if(os.path.isfile(filePath)):
        print(str(sub["id"]),"is already in the dir.")
        continue
    if(sub["verdict"] != "OK"):
        continue
    sub["filePath"] = filePath
    subs.append(sub)

print("There is", len(subs),"submission to retrieve")
for i,sub in enumerate(subs,start=1):
    print(i,end=" - ")
    try:
        Code = getCode(str(sub["contestId"]), str(sub["id"])).replace("\r\n","\n").replace("\r","\n")
    except:
        print("Failed!")
        errorCnt += 1
        if(errorCnt >= MAXERROR):sys.exit()
        continue
    with open(sub["filePath"], 'w', encoding="utf-8") as file:
        file.write(Code)
