info = {
    "Name": "Preetham Pereira",
    "Age": 24,
    "Occupation": "Internship",
    "Education": "Master in Computer Application",
}

print(
    f"My name is {info['Name']}, and i am {info['Age']} years old. I completed my bachelors in {info['Education']} and now i am currently doing {info['Occupation']} "
)


for key, value in info.items():
    print(key, value)
