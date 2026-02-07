info = {
    "name" : "Preetham Pereira",
    "age" : 24,
    "city" : "Mangalore",
    "qualification" : "Master in Computer Application (Cybersecurity)",
    "favourites" : ["DevOps", "Linux", "python"]
}

print(f"I am {info["name"]}, from {info["city"]}. I am {info["age"]}years old. My qualification is: I am a {info["qualification"]}") 
print("I love", info.get("favorites", "Not found"))
# print(info.get.__doc__)
# print(dir(info))

# Iterate a Dict
for key,value in info.items():
    print(key,value)
    