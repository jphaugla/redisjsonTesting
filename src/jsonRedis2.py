import os, json
from redis import StrictRedis, Redis

rj = StrictRedis('localhost', 6379, decode_responses=True)
print("connect successful")
base_directory = "../data/"
cnt = 0
for (dirpath, dirnames, filenames) in os.walk(base_directory):
    print("dirpath=" + dirpath)
    for file in filenames:
        # print("file=" + file)
        if ("json" in file):
            shortname = file.replace(".json", "")
            print("shortname is" + shortname)
            openname = dirpath + "/" + file
            print("openname is " + openname)
            data = json.loads(open(openname, "r").readline())
            print("data is ")
            print(data['data'])
            print("members is")
            print(data['data']['members'])
            for member in data['data']['members']:
                print("the id is", member['id'])
                memberIdInt = member['id']
                memberId = str(memberIdInt)
                memberIdFloat = float(memberIdInt)
                keyname="member:" + memberId
                idxKeyName="memberIndex:" + memberId
                zkeyname = "identifier:"
                # memberStr = json.dumps(member)
                memberStr = '{"id": 2048306}'
                jsonCommand = "json.set " + keyname + " . '" + memberStr + "'"
                # jsonCommand = "json.set " + keyname + " $ '" + memberStr + "' INDEX ID"
                print("jsonCommand is " + jsonCommand)
                #  can't use jsonset command because index not available but otherwise, this worked
                # rj.jsonset(keyname, Path.rootPath(), member)
                rj.execute_command(jsonCommand)
                # rj.execute_command("json.index add ID $.identifiers.type")
