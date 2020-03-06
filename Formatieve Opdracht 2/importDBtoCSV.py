from pymongo import MongoClient
import csv

envvals = ["MONGODBUSER", "MONGODBPASSWORD", "MONGODBSERVER", "RECOMADDRESS"]
dbstring = 'mongodb+srv://{0}:{1}@{2}/test?retryWrites=true&w=majority'

client = MongoClient()
database = client.huwebshop

products = database.products.find()

print("Creating the product database contents...")
with open('products.csv', 'w', newline='') as csvout:
    fieldnames = ['id', 'category', 'subcategory', 'subsubcategory']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    c = 0
    for product in products:
        writer.writerow({'id': product["_id"],
                         'category': product.get("category", None),
                         'subcategory': product.get("sub_category", None),
                         'subsubcategory': product.get("sub_sub_category", None)
                         })
        c += 1
        if c % 10000 == 0:
            print("{} product records written...".format(c))
print("Finished creating the product database contents.")\


#           BRONVERMELDING
#   Nick zijn code gebruikt uit de les