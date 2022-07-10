import pandas as pd


dict_city = {"City": ["Moscow", "Saint-Petersburg", "Novosibirsk"],
             "Population" : [12678079, 5398064, 1625631]}

list_city = [["Moscow", "Saint-Petersburg", "Novosibirsk"], [12678079, 5398064, 1625631]]

# df = pd.DataFrame(dict_city)

out2 = pd.DataFrame(list_city).T

# print(out2)

df = pd.read_csv("/Users/mikhailsbitnev/Documents/PrivateMichael/IHME-GBD_2019_DATA-8a2374c7-1.csv")


# df.head(8)
# df.tail()
# df.info()
# print(df.shape)
# print(df.describe())
# print(df)


# print(df.describe(include='all'))

# print(df[["measure_name", "location_id", "sex_name"]])

# print(df.loc[100:110, "location_name": "val"])


# print(df.iloc[100:110, 9:12])


# print(df[(df["sex_name"] == "Both") & (df["location_id"] == 59)])


cardio = df[(df["sex_name"] == "Both") & (df["cause_name"] == "Injuries") & (df["year"] == 2019) & (df["val"] > 0)]

# print(df[(df["sex_name"] == "Both") & (df["cause_name"] == "Injuries") & (df["year"] == 2019) & (df["val"] > 600)])

cardio2 = cardio.sort_values(by = ["val"], ascending=False, inplace=False, na_position='last', ignore_index=False)

print(cardio2.iloc[ : , 10:])

