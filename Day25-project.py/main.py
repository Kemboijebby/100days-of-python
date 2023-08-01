# with open("weather_data.csv") as data:
#     data_file=data.readlines()
#     print(data_file)

# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures=[]
#     for column in data:
#         if column[1] !="temp":
#             temperatures.append(int(column[1]))
#
#     print(temperatures)
# import pandas
#pandas DATAFRAME type
# data=pandas.read_csv("weather_data.csv")
# print(data)
import pandas
#data=pandas.read_csv("weather_data.csv")
#pandas series type object
#print(data["temp"])

#convert data to dictionary
#data_dict=data.to_dict()
#print(data_dict)
#covert temperature data to list
# temp_list=data["temp"].to_list()
# print(temp_list)


# sum_temp=sum(temp_list)
# average=sum_temp/len(temp_list)
# print(round(average,2))

#with pandas
# print(data["temp"].mean())
# print(data["temp"].max())
#Getting data in columns
# print(data['condition'])
# print(data.condition)

#Get data in rows
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

#conver temp to Farhneit
# monday= data[data.day=="Monday"]
# monday_temp=int(monday.temp)
# monday_temp_F=monday_temp * 9/5 + 32
# print(monday_temp_F)

#creating a data frame from scratch
# data_dict = {
#     "students":["anitah","jay","shazzy"],
#      "scores":[90,82,77]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("New_data.csv")
import pandas
data=pandas.read_csv("Central_Park_Squirrel_Census.csv")
data_list=data["Primary_Fur_Color"].to_list()

gray = data_list.count('Gray')
print(int(gray))

cinnamon = data_list.count('Cinnamon')
print(int(cinnamon))

black = data_list.count('Black')
print(int(black))

New_sample={
    "Fur_color":["Gray","Cinnamon","Black"],
    "Count":[2473,392,103]
}
sample=pandas.DataFrame(New_sample)
sample.to_csv("Color_sample.csv")











