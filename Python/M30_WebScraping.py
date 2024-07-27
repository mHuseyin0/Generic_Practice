from bs4 import BeautifulSoup
"""
with open("index.html", "r") as f:
    doc = BeautifulSoup(f,"html.parser")

myTitle = doc.title
print(doc.prettify())
print(myTitle)
print(myTitle.string)
myTitle.string = "My first parser"
print(myTitle.string, "\n\n")

myLinks = doc.find_all("a")

myLinks[0]["href"] = "This link was set by python"
myLinks[0]["color"] = "blue"
print(myLinks[0].attrs)

myHeaders = doc.find_all(["h"+str(i) for i in range(1,6)]) #Searching for multiple tags with a list
for i in myHeaders:
    print(i)

myColoredHeaders = doc.find_all("span",style="background-color: darkgray;") #Searching with multiple parameters
for i in myColoredHeaders:
    print(i)

for i in doc.find_all("input", type="text"):
    i["placeholder"] = "Changed Placeholder"

print("\n\n")
for i in myLinks:
    print(i)

print("\n\n")

myParagraphs = doc.find_all("p")
for i in myParagraphs:
    print(i)
    print(i.find_all("i"))

with open("changed.html", "w") as webSite:
    webSite.write(str(doc))
"""

import requests

def dataCollector(year):
    months = dict()
    keys = []
    for a in range(1,13):
        sunUrl = f"https://www.timeanddate.com/sun/@304582?month={a}&year={year}"

        sunResult = requests.get(sunUrl)
        sunScraped = BeautifulSoup(sunResult.text, "html.parser")
        #sunGet = sunScraped.find_all(string="Nautical Twilight")

        sunBody = sunScraped.find_all("tbody")[1]

        times = []

        for i in sunBody:
            try:
                times.append(i.find_all("td", class_="c sep")[1].string)
            except IndexError:
                continue
        
        month = sunScraped.head.find("title").string[35:].replace(f" {sunUrl[-4:]}","")

        keys.append(month)
        months[month] = times
    return (months, keys, year)

rows = 2

def calendarPrinter(monthDict, keysList, year):
    dash= "-"*5
    global rows
    rowNum = rows
    loopList =lambda : keysList[int((12/rows)*(rows-rowNum)):int((12/rows)*(rows-rowNum+1))]
    print()
    myTitle = "CALCULATIONS FOR "+str(year)
    print(f"{myTitle:^140}",end="\n\n")
    while rowNum>0:
        loopSequence = loopList()
        print(end="\t")
        for k in loopSequence:
            print(f"{k:^10}", end="\t\t")
        print()
        print(end="\t")
        for _ in loopSequence:
            print("-"*10, end="\t\t")
        print()

        day = 0
        while day<27:
            print(f"{day+1:02}: ",end="\t")
            for i in loopSequence:
                print(f"{str(monthDict[i][day]): ^10}", end="\t\t")
            print()
            day+=1

        while day<31:
            print(f"{day+1:02}: ",end="\t")
            for i in loopSequence:
                try:
                    print(f"{str(monthDict[i][day]): ^10}", end="\t\t")
                except IndexError:
                    print(f"{dash : ^10}", end="\t\t")
            print()
            day+=1
        print("\n")
        rowNum-=1
    print("_"*182, end="\n"*10)

def dataComparator(*years):
    yearsDict = dict()
    counter = 0
    for i in years:
        yearsDict[i],keys = dataCollector(i)[0:2]

"""myCourses = "https://w3.cs.bilkent.edu.tr/course-homepages/"
resultCourses = requests.get(myCourses)
scrapedCourses = BeautifulSoup(resultCourses.text, "html.parser")

for i in scrapedCourses.find_all("a", target="_blank"):
    print(i.parent.string)
    print(i["href"])
    print()

allCourses = "https://www.timeanddate.com/sun/@304582?month=1&year=2023"
resultAll = requests.get(allCourses)
textCourses = BeautifulSoup(resultAll.text, "html.parser")
table = textCourses.find("tr", class_="bg-wt")
tableContents = table.contents
firstElement = table.next_element
secondElement = firstElement.next_sibling
lastElement = tableContents[-1]
print(firstElement)
print(secondElement)
print(lastElement)
for i in secondElement.next_siblings:
    print(i.string)
print(table.parent.name)
print(list(table.descendants)) #children and contents will give similar results"""
