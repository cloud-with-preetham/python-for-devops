nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(nums))

clouds = list()
clouds.append("aws")
clouds.append("azure")
clouds.append("GCP")
clouds.append("utho")

print(clouds)

for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} Mostly Used world wide...!")
    elif cloud == "azure" or cloud == "GCP":
        print(f"{cloud} Top market contenders after AWS")
    else:
        print(f"{cloud} Startup in India...!")
