import requests
import json
req="http://saral.navgurukul.org/api/courses"
x=requests.get(req)
a=x.json()
f=open("course.json","w")
json.dump(a,f,indent=4)       
def option(s,m,slug,b):
    while True:
        x=m
        options=input("enter your option up,back,next,exit = ")
        if options=="up":
            x-=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[x]))
            r=req.json()
            print("content",r["content"])
            print(x)
        elif options=="next":
            x+=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1["content"])
            print(x)
        elif options=="back":
            c=1
            for dic1 in b["data"]:
                print(c,dic1["name"])
                c+=1
                for i in dic1["childExercises"]:
                    print(" ",c,i["name"])
                    c+=1
        else:
            break
def course():
    index=1
    for i in a["availableCourses"]:
        print(index,i["name"],i["id"])
        index=index+1
    for j in a["availableCourses"]:
        n=int(input("enter your number of courrse:-"))
        s=a["availableCourses"][n-1]["id"]
        req1="http://saral.navgurukul.org/api/courses/"+str(s)+"/exercises"
        y=requests.get(req1)
        b=y.json()
        print(b)
        #print(b)(for row data or text data)
        c=1 
        slug=[]
        for k in b["data"]:
            print(c,k["name"])
            slug.append(k["slug"])
            c=c+1
            for child in k["childExercises"]:
                print(c,child["name"])
                slug.append(child["slug"])
                c+=1
        m=int(input("show content slug = "))
        req3="http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[m-1])
        z=requests.get(req3)
        d=z.json() 
        print(d["content"])
        option(s,m,slug,b)
course()