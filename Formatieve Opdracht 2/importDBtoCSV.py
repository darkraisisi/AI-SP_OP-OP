from pymongo import MongoClient
import csv

envvals = ["MONGODBUSER", "MONGODBPASSWORD", "MONGODBSERVER", "RECOMADDRESS"]
dbstring = 'mongodb+srv://{0}:{1}@{2}/test?retryWrites=true&w=majority'

client = MongoClient()
database = client.huwebshop

products = database.products.find()
sessions = database.sessions.find()
profiles = database.profiles.find()


def generateCSV(fileNameString, category, fieldnames, values):
    print("Creating the product database contents...")
    with open(fileNameString, 'w', newline='', encoding='utf-8') as csvout:
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for record in category:
            writeDict = {}
            for x in range(len(fieldnames)):
                if x == 0:
                    writeDict.update({fieldnames[x]: record[values[0]]})
                else:
                    writeDict.update({fieldnames[x]: record.get(values[1], None)})
            writer.writerow(writeDict)
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
    print("Finished creating the product database contents.")


generateCSV('products.csv', products,
            ['id', 'name', 'gender', 'category', 'subcategory', 'subsubcategory', 'brand'],
            ["_id", "name", "gender", "category", "sub_category", "sub_sub_category", "brand"])
generateCSV('sessions.csv', sessions,
            ['id', 'segment'],
            ["_id", "segment"])
generateCSV('profiles.csv', profiles,
            ['id', 'browser_id'],
            ["_id", "buids"])

#           BRONVERMELDING
#   Dit is de code die gebruikt is tijdens de les van 5 maart met Nick.