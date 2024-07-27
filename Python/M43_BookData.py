import pandas as pd
from shutil import copyfile
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from copy import deepcopy

def excelToPickle():
    data = pd.ExcelFile("2023-24-Bahar-Kitap-Listesi.xlsx")
    dataFrame = data.parse(0)
    books = list()
    index = 1
    for i in range(index,844):
        try:
            book = dataFrame.iloc[i]
            books.append(tuple([book.iloc[1], book.iloc[2]]))
        except Exception:
            with open("BookList.pkl", "wb") as file:
                pickle.dump(books, file)
                pickle.dump(i, file)

    with open("BookList.pkl", "wb") as file:
                pickle.dump(books, file)
                pickle.dump(844, file)

    with open("BookList.pkl", "rb") as file:
        books = pickle.load(file)

    counter = 1
    for bookTuple in books:
        print(f"{counter}: {bookTuple[0]:100} {bookTuple[1]}")
        counter += 1

def resetMissing():
    copyfile("BookList.pkl", "MissingBooks.pkl")

def initialization():
    global DRIVER
    DRIVER = webdriver.Chrome()
    DRIVER.get("https://www.kitapyurdu.com/")
    DRIVER.maximize_window()

def getBookPage():
    booksList: list
    with open("MissingBooks.pkl", "rb") as file:
        booksList = pickle.load(file)

    try:
        with open("ActualData.pkl", "rb") as file:
            actualData = pickle.load(file)
    except Exception:
        actualData = list()

    nameInput: WebElement
    tempBookList = deepcopy(booksList)

    dumpCount = 0
    counter = 0
    for bookData in tempBookList:
        counter += 1
        nameInput = WebDriverWait(DRIVER,3).until(EC.presence_of_element_located((By.ID, "search-input")))
        nameInput.clear()
        try:
            nameInput.send_keys(bookData[0]," ",bookData[1],Keys.ENTER)
            bookPageLink = WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "cover"))).find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            try:
                DRIVER.find_element(By.LINK_TEXT, "Benzer Sonuçları da Göster").click()
                bookPageLink = WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "cover"))).find_element(By.TAG_NAME, "a").get_attribute("href")
            except Exception as e:
                print(f"An error occured while trying to get the WebPage of {bookData[0]}.")
                print(f"Exception: {e}")
                continue
        try:
            DRIVER.get(bookPageLink)
            attributeTable: WebElement
            attributeTable = WebDriverWait(DRIVER, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "attributes")))
            tableRow: WebElement
            tableRow = attributeTable.find_elements(By.TAG_NAME, "tr")
            row: WebElement
            for row in tableRow:
                tdatas = row.find_elements(By.TAG_NAME, "td")
                if tdatas[0].text == "Sayfa Sayısı:":
                    pageNum = tdatas[1].text
                    break
            booksList.remove(bookData)
            actualData.append(tuple([bookData[0], bookData[1], int(pageNum)]))
        except Exception as e:
            print(f"An error occured while trying to get the data of {bookData[0]}.")
            print(f"Exception: {e}")
        if counter % 200 == 0:
            dumpCount += 1
            with open("ActualData.pkl", "ab") as file:
                pickle.dump(actualData, file)
            actualData = list()
            with open("MissingBooks.pkl", "wb") as file:
                pickle.dump(booksList, file)
    return dumpCount
        
def printActual(dumpCount):
    with open("ActualData.pkl", "rb") as file:
        print(f"Collected Data:\n" + "-" * 100)
        bookCounter = 0
        for i in range(dumpCount):
            booksList = pickle.load(file)
            for bookTuple in booksList:
                bookCounter += 1
                print(f"{bookCounter}- ", end="")
                for bookInfo in bookTuple:
                    print(bookInfo)
                print()
            print()

def printMissing(dumpCount):
    with open("MissingBooks.pkl", "rb") as file:
        print(f"Missing Books:\n" + "-" * 100)
        bookCounter = 0
        for i in range(dumpCount):
            booksList = pickle.load(file)
            for bookTuple in booksList:
                bookCounter += 1
                print(f"{bookCounter}- ", end="")
                for bookInfo in bookTuple:
                    print(bookInfo)
                print()

""" with open("ActualData.pkl", "rb") as file:
    sum = 0
    booksList = list()
    for _ in range(6):
        booksList += pickle.load(file)
    failedList = [0] * 10
    for i in range(10):
        failedList[i] = 0
    for bookTuple in booksList:
        repetition = booksList.count(bookTuple)
        if (repetition > 1):
            failedList[repetition - 2] += 1

    for i in range(10):
        print("Repetition counts:")
        print(i + 2, ": ", failedList[i])
    print("Collected book data: ", len(booksList))

with open("MissingBooks.pkl", "rb") as file:
    booksList = pickle.load(file)
    print("Missing book data: ", len(booksList))
 """

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mha53825382",
    database="BookList"
)

cursor = mydb.cursor()

printActual(6)
printMissing(1)