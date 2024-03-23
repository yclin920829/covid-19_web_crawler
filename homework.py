import csv
import json
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties as font

font1 = font(fname="/Users/yu-chiaolin/Documents/大二/大二上/網路程式設計/網路期末專題/NotoSansTC-Light.otf")

links, data_url = [], []

html1 = requests.get("https://covid-19.nchc.org.tw/dt_005-covidTable_taiwan.php")
soup1 = BeautifulSoup(html1.content, "lxml")

time = 0
for a in soup1.find_all("div", class_ = "container"):
    time += 1
    if time == 2:
        for b in a.find_all("span", style = "font-size: 0.9em;"):
            if b.find("a") != None:
                links.append(b.find("a").get("href"))

for i in range(4):
    if i == 1 or i == 2:
        #print(links[i])
        html2 = requests.get(links[i])
        soup2 = BeautifulSoup(html2.content, "lxml")  
        time = 0
        for a in soup2.find_all("code"):
            time += 1
            if time == 3:
                data_url.append(a.text)
                
html3 = requests.get(data_url[0])
soup3 = BeautifulSoup(html3.content, "lxml")

html4 = requests.get(data_url[1])
soup4 = BeautifulSoup(html4.content, "lxml")

a = json.loads(soup3.text)
b = json.loads(soup4.text)

taiwan_diagnoses, taiwan_deaths, taiwan_deathrate = [], [], []
month_taiwan_diagnose, month_taiwan_death = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in a: taiwan_diagnoses.append([i['a01'], i['a06']])
for i in b: taiwan_deaths.append(i['a01'])

for taiwan_diagnose in taiwan_diagnoses:
    taiwan_diagnose[0] = int(taiwan_diagnose[0].replace("-", ""))
    if taiwan_diagnose[0] >= 20220100 and taiwan_diagnose[0] <= 20220200:
        month_taiwan_diagnose[0] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220200 and taiwan_diagnose[0] <= 20220300:
        month_taiwan_diagnose[1] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220300 and taiwan_diagnose[0] <= 20220400:
        month_taiwan_diagnose[2] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220400 and taiwan_diagnose[0] <= 20220500:
        month_taiwan_diagnose[3] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220500 and taiwan_diagnose[0] <= 20220600:
        month_taiwan_diagnose[4] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220600 and taiwan_diagnose[0] <= 20220700:
        month_taiwan_diagnose[5] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220700 and taiwan_diagnose[0] <= 20220800:
        month_taiwan_diagnose[6] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220800 and taiwan_diagnose[0] <= 20220900:
        month_taiwan_diagnose[7] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20220900 and taiwan_diagnose[0] <= 20221000:
        month_taiwan_diagnose[8] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20221000 and taiwan_diagnose[0] <= 20221100:
        month_taiwan_diagnose[9] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20221100 and taiwan_diagnose[0] <= 20221200:
        month_taiwan_diagnose[10] += int(taiwan_diagnose[1])
    elif taiwan_diagnose[0] >= 20221200 and taiwan_diagnose[0] <= 20221300:
        month_taiwan_diagnose[11] += int(taiwan_diagnose[1])

for taiwan_death in taiwan_deaths:
    taiwan_death = int(taiwan_death.replace("-", ""))
    if taiwan_death >= 20220100 and taiwan_death <= 20220200:
        month_taiwan_death[0] += 1
    elif taiwan_death >= 20220200 and taiwan_death <= 20220300:
        month_taiwan_death[1] += 1
    elif taiwan_death >= 20220300 and taiwan_death <= 20220400:
        month_taiwan_death[2] += 1
    elif taiwan_death >= 20220400 and taiwan_death <= 20220500:
        month_taiwan_death[3] += 1
    elif taiwan_death >= 20220500 and taiwan_death <= 20220600:
        month_taiwan_death[4] += 1
    elif taiwan_death >= 20220600 and taiwan_death <= 20220700:
        month_taiwan_death[5] += 1
    elif taiwan_death >= 20220700 and taiwan_death <= 20220800:
        month_taiwan_death[6] += 1
    elif taiwan_death >= 20220800 and taiwan_death <= 20220900:
        month_taiwan_death[7] += 1
    elif taiwan_death >= 20220900 and taiwan_death <= 20221000:
        month_taiwan_death[8] += 1
    elif taiwan_death >= 20221000 and taiwan_death <= 20221100:
        month_taiwan_death[9] += 1
    elif taiwan_death >= 20221100 and taiwan_death <= 20221200:
        month_taiwan_death[10] += 1
    elif taiwan_death >= 20221200 and taiwan_death <= 20221300:
        month_taiwan_death[11] += 1

for i in range(12): taiwan_deathrate.append((month_taiwan_death[i] / month_taiwan_diagnose[i]) * 100)

print(month_taiwan_diagnose)
print(month_taiwan_death)
for i in taiwan_deathrate: print(round(i,3), end = " ")

fig, ax1 = plt.subplots()

month = [1,2,3,4,5,6,7,8,9,10,11,12]    
diagnose_num = ["0", "0.25", "0.5", "0.75", "1", "1.25", "1.5", "1.75", "2"]
death_num = ["0", "0.625", "1.25", "1.875", "2.5", "3.125", "3.75", "4.375", "5"]
x = range(0, 2250000, 250000)
y = [0, 0.625, 1.25, 1.875, 2.5, 3.125, 3.75, 4.375, 5,]

ax1.bar(month, month_taiwan_diagnose, label = "死亡個數(每百萬人)")
ax1.set_xticks(month)
ax1.set_yticks(ticks=x, labels=diagnose_num)
ax1.set_xlabel('月份', fontproperties=font1, fontsize="17", loc='right')
ax1.set_ylabel('死亡個數', fontproperties=font1, fontsize="12", rotation=360, loc = 'center')
ax1.set_title("2022年確診個數與人口數比較", fontproperties=font1, fontsize="20")
ax1.legend(prop=font1, loc ="upper left")
ax2 = ax1.twinx()
ax2.plot(month, taiwan_deathrate, color = 'red',  linewidth="2", markersize="7.5", marker=".", label = "死亡率")
ax2.set_yticks([0, 5])
ax2.set_ylabel('死亡率', fontsize="12", fontproperties=font1, rotation=360, loc = 'center')
ax2.legend(prop=font1, loc ="upper right")
ax2.set_yticks(ticks=y, labels=death_num)

plt.show()    

with open('covid19.csv', newline='',encoding="utf-8") as csvfile: 
    data = csv.reader(csvfile)
    taiwan_diagnoses= list(data)

age_name = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70+"]
age_female, age_male  = [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]

#統計
for i in taiwan_diagnoses:
    if i[1] == "2022"  and i[5] == "F":
        if len(i[7]) == 1 or i[7] == "5-9":
            age_female[0] += int(i[8])
        elif i[7] == "10-14" or i[7] == "15-19":
            age_female[1] += int(i[8])
        elif i[7] == "20-24" or i[7] == "25-29":
            age_female[2] += int(i[8])
        elif i[7] == "30-34" or i[7] == "35-39":
            age_female[3] += int(i[8])
        elif i[7] == "40-44" or i[7] == "45-49":
            age_female[4] += int(i[8])
        elif i[7] == "50-54" or i[7] == "55-59":
            age_female[5] += int(i[8])
        elif i[7] == "60-64" or i[7] == "65-69":
            age_female[6] += int(i[8])
        elif i[7] == "70+":
            age_female[7] += int(i[8])
    elif i[1] == "2022"  and i[5] == "M":
        if len(i[7]) == 1 or i[7] == "5-9":
            age_male[0] += int(i[8])
        elif i[7] == "10-14" or i[7] == "15-19":
            age_male[1] += int(i[8])
        elif i[7] == "20-24" or i[7] == "25-29":
            age_male[2] += int(i[8])
        elif i[7] == "30-34" or i[7] == "35-39":
            age_male[3] += int(i[8])
        elif i[7] == "40-44" or i[7] == "45-49":
            age_male[4] += int(i[8])
        elif i[7] == "50-54" or i[7] == "55-59":
            age_male[5] += int(i[8])
        elif i[7] == "60-64" or i[7] == "65-69":
            age_male[6] += int(i[8])
        elif i[7] == "70+":
            age_male[7] += int(i[8])
        
for i in range(8): age_male[i] = -age_male[i]

index = range(0, 8)
a = ["1", "0.75", "0.5", "0.25", "0", "0.25", "0.5", "0.75", "1"]
b = [-1000000, -750000, -500000, -250000, 0, 250000, 500000, 750000, 1000000]

plt.xlim(-1100000,1100000)
plt.barh(index, age_female, height=0.8, facecolor='r', linewidth=2, label='女')
plt.barh(index, age_male, height=0.8, facecolor='b', linewidth=2, label='男')
plt.xticks(ticks = b, labels = a)
plt.yticks(ticks=index, labels=age_name)
plt.xlabel('確診人數(每百萬人)', fontproperties=font1, fontsize="15", loc='right')
plt.ylabel('各年齡層', fontproperties=font1, fontsize="15", rotation=360, loc ='top')
plt.title("2022年各年齡層男女確診人數", fontproperties=font1, fontsize="20")
plt.legend(loc=0, prop=font1)

for x,y in zip(index, age_female): plt.text(y, x, y, ha='left', va='center')
for x,y in zip(index, age_male): plt.text(y, x, -y, ha='right', va='center')

plt.show()
