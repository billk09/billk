#string,integer,t/f(boolean),list,float
#Dictionary(Object)
#Create
# information = {
#     #key:value
#     "do_kho":['snack','thit bo kho'],
#     "dong_lanh":{
#         "do_song":[],
#         "do_gan_chin":[],
#         "do_da_chin":"khong co do"
#     },
#     "is_open":True,#Accepted all type data
#     "gia_dung":"chao ran"
# }

#Get value by key
#C.R.U.D
#Create
#Update
#Read
#Delete

# print(
#     #dictionary[key]
#     information["do_kho"]
# )

# #Update value by key

# #print(information["dong_lanh"]["do_song"].append("ca map"))
# information['dong_lanh']["do_da_chin"] = "ca kho lang vu dai"
# print(information["dong_lanh"]["do_song"])

# #Delete key from dictionary
# del information["is_open"]

# print(information)

# class_info = [
#     {
#        " name":"Nam Khanh",
#         "age":16,
#         "sex":"Male"
#     },
#     {
#         "name":"long",
#         "age":15,
#         "sex":"Male"
#     },
#     {
#         "name":"linh",
#         "age":17,
#         "sex":"Female"
#     },
# ]

# for item in class_info:
#    if item ["sex"] == "Female":
#        print(item)

listDistrict = [
    {
       " name":"DD",
        "square":117.43,
        "people":150300
    },
    {
        "name":"BD",
        "square":9.224,
        "people":247100
    },
    {
        "name":"BTL",
        "square":43.25,
        "people":333300
    }
]

listPeople = []
result = 0
for i in listDistrict:
    listPeople.append(i['people'])
    result = max(listPeople)

districtHasMax = {}

for item in listDistrict:
    if(item['people'])==result:
        districtHasMax = item

print(districtHasMax)


