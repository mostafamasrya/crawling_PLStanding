import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest


result=requests.get("https://www.skysports.com/premier-league-table")

src=result.content
soup=BeautifulSoup(src,"lxml")

teams=soup.find_all("tr",{"class":"standing-table__row"})
print("len of teams is : " ,len(teams))
# print(teams[1].find("td",{"class":"standing-table__cell--name"}).attrs['data-short-name'])
print("=============================================")

print(teams[1].find_all("td",{"class":"standing-table__cell"})[9].text)

print("=============================================")

# .find("td")[1].attrs['data-long-name']


teamsNames=[]
numbers=[]
played=[]
win=[]
lost=[]
draw=[]
f=[]
A=[]
GD=[]
PTS=[]



for i in range(len(teams)):
    if(i != 0):

        teamsNames.append(teams[i].find("td",{"class":"standing-table__cell--name"}).attrs['data-short-name'])
        numbers.append(i)
        played.append(teams[i].find_all("td",{"class":"standing-table__cell"})[2].text)
        win.append(teams[i].find_all("td",{"class":"standing-table__cell"})[3].text)
        draw.append(teams[i].find_all("td",{"class":"standing-table__cell"})[4].text)
        lost.append(teams[i].find_all("td",{"class":"standing-table__cell"})[5].text)
        f.append(teams[i].find_all("td",{"class":"standing-table__cell"})[6].text)
        A.append(teams[i].find_all("td",{"class":"standing-table__cell"})[7].text)
        GD.append(teams[i].find_all("td",{"class":"standing-table__cell"})[8].text)
        PTS.append(teams[i].find_all("td",{"class":"standing-table__cell"})[9].text)

        mylists=[numbers,teamsNames,played,win,draw,lost,f,A,GD,PTS]
        exported_data=zip_longest(*mylists)

with open("D:/programming/ITI\Crawling&scraping/primerLeague/PLStanding2022.csv","w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["STANDING" , "TEAM" ,"played", "W" ,"D" ,"L" , "F" ,"A","GD","PTS"])
    wr.writerows(exported_data)
