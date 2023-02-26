import json
import sys
import os
from cf_fetch import getCode, callApi


MAXERROR = 5
errorCnt = 0


handle = input("Enter your handle: ") or "MEGAMMS"
info = callApi(handle)

print("There is", len(info["result"]),"submission to retrieve")

path = os.path.join(os.getcwd(),"Subs")
os.makedirs(path,exist_ok = True)

with open("programmingLanguages.json","r") as file:
    extinctions = json.loads(file.read())


for i,sub in enumerate(info["result"],start=1):
    if(errorCnt >= MAXERROR):sys.exit()
    filePath = path + "\\" + str(sub["id"]) + "." + extinctions[sub.get("programmingLanguage", "txt")]
    print(i,end=" - ")
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
