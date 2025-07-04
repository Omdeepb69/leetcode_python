mt_dic = dict(name = "omdeep ", age = 20, state = "goa", country = "india")
mt_dic["hobby"] = "coding"
mt_dic.update({"hobby": "coding", "language": "python"})
mt_dic.pop("age")
mt_dic.popitem() # Removes the last inserted key-value pair
mt_dic.update({"hobby": "coding", "language": "python"})
mt_dic["hobby"]="gooning"
name = mt_dic.get("name")  # Returns the value for the specified key
gg = {
    "omdeep":{"marks":94,"kk":"yoo"},
    "ujjj":{"marks":99,"kk":"yooshiii"}  
}
print(gg["omdeep"]["marks"])
print(mt_dic)
print(mt_dic["name"])
print(mt_dic.get("language","not found"))

for key in gg:
    print(key,gg[key])