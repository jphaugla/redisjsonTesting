import redis
from redis.commands.json.path import Path

rj = redis.Redis(host='localhost', port=6379, db=0)
print("connect successful")
initialJSON = {
    'a': 2
}
initialDollar = {
    '$a': 2
}
rj.json().set("doc", Path.root_path(), initialJSON)
rj.json().set("doc", Path.root_path(), initialJSON)
rj.json().set("doc", ".a", 3)
print(rj.json().get("doc"))
rj.json().set("doc", "a", 4)
print(rj.json().get("doc"))
# now with dollar in member
rj.delete("doc")
rj.json().set("doc", Path.root_path(), initialDollar)
rj.json().set("doc", ".$a", 3)
print(rj.json().get("doc"))
rj.json().set("doc", "$a", 4)
print(rj.json().get("doc"))
# now with dollar in member and key
rj.delete("$doc")
rj.json().set("$doc", Path.root_path(), initialDollar)
rj.json().set("$doc", ".$a", 3)
print(rj.json().get("$doc"))
rj.json().set("$doc", "$a", 4)
print(rj.json().get("$doc"))
