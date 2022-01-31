import requests
import json
import os 
if os.path.isfile("maraki_course.json"):
    with open("maraki_course.json","r") as k:
        text_data=json.load(k)

else:
    saral=requests.get("http://saral.navgurukul.org/api/courses" )
    saral_url=requests.get(saral)
    data=saral_url.json()
    with open("maraki_course.json","w") as k:
        text_data=json.dump(data,k,indent=4)
serial=0
for i in text_data["availableCourses"]:
    print(serial+1,(" - "),i["name"],(" - "),i["id"])
    serial+=1
    print(" ")
user_input=int(input("What Course Do You Want Plase Enter of Number of cousre:-"))
# parent_name=data["availableCourses"][user_input-1]["id"]
parent_id=text_data["availableCourses"][user_input-1]["id"]
parent_name=text_data["availableCourses"][user_input-1]["name"]
print(parent_name)


if os.path.isfile("parents.json"):
    with open("parnets.json","r")as data:
        text_data=json.load(k)
else:
    parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercises"
    parent_url = requests.get(parent_api)
    data_1 = parent_url.json()
    with open ("parents.json","w") as data:
        json.dump(data_1,data,indent=4)

serial_no_1=0
#for printing the details of the specific courses:
for index1 in data_1["data"]:
    if len(index1["childExercises"])==0:
        print("   ",serial_no_1,".",index1["name"])
        serial_no_1=serial_no_1+1
        if len(i["childExercises"])>0:
            s=0
            for j in i['childExercises']:
                s=s+1
                print("         ",s.j['name'])

    else:
        print("            1",i["slug"])
        serial_no_1+=1
print("")
if os.path.isfile("contents.json"):
    with open("contents.json","r")as data:
        json.load(data)

else:
    topic_no_1=int(input("enter the number"))
    m=0
    list_1=0
    while m<len(text_data["data"][topic_no_1]["childExercises"]):
        print("      ",m+1,data_1["data"][topic_no_1]["childExercises"][m]["name"])  
    slug=(text_data["data"][topic_no_1]["childExercises"][m]["slug"])
    conten_api= ("http://saral.navgurukul.org/api/courses/"+str(parent_id)+'exercise/getBySlug?slug='
# ug_list=[]
# print("     ",slug,".",topic_list[slug-1])

# s_num=1
# for index1 in data_1["data"][slug-1]["childExercises"]:
#     print("    sl       ",s_num,".",index1["name"])
#     question_list.append(index1["name"])
#     s_num+=1

# que=int(input("Enter question number:")) 
# w=requests.get("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercise/getBySlug?slug="+str(data_1["data"][slug-1]["childExercises"][que-1]["slug"]))
# DATA=w.json()
# with open("question.json","w") as a:
#     json.dump(DATA,a,indent=4)
#     print(DATA["content"])
# break