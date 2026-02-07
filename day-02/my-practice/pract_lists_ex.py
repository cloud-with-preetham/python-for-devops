a = [100, 200, 900, True, 0.68]    # LIST bananeka 1st tarika
print(type(a))
a.append(500)
print(a)

clouds = list() # LIST bananeka 2nd tarika
clouds.append("aws")
clouds.append("azure")
clouds.append("GCP")
clouds.append("utho")
clouds.append("IBM")
clouds.append("Alibaba")
print(clouds)
print(f"Length of list is: {len(clouds)}")
print(f"World leader of cloud industry is: {clouds[0]}")
print(f"Indian cloud service provider is: {clouds[-3]}")

# print(dir(clouds))
# print(clouds.reverse.__doc__)

for cloud in clouds:
    if cloud == "aws":
        print(f"{cloud} is the market leader in the cloud industry.")
    elif cloud == "azure" or cloud == "GCP":
        print(f"{cloud} is the highest market captured company in the cloud service industry after AWS.")
    elif cloud == "utho":
        print(f"{cloud} is the India's #1 Ranked Cloud Service Provider.")
    else:
        print(f"{cloud} is not into the competition in the market.")
