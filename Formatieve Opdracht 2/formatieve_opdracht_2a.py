from pymongo import MongoClient
import random, os, json, urllib.parse, requests


envvals = ["MONGODBUSER","MONGODBPASSWORD","MONGODBSERVER","RECOMADDRESS"]
dbstring = 'mongodb+srv://{0}:{1}@{2}/test?retryWrites=true&w=majority'

client = MongoClient()
database = client.huwebshop

products = database.products.find()

def printFristProductInfo():
    print(f'Product: {products[0]["name"]}, Prijs: {products[0]["price"]["discount"]}')

def printFirstR():
    for product in products:
        if product["name"][0] == "r":
            print(product["name"])
            break

def printAveragerPrice():
    total = 0
    for product in products:
        try:
            total += product['price']['discount']
        except:
            pass
    print(total / database.products.count())

printFristProductInfo()
printFirstR()
printAveragerPrice()