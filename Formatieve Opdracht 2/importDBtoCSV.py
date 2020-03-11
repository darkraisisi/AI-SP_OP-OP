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
<<<<<<< HEAD
                    if record[values[0]] != '':
                        dashIndex = str(record[values[0]]).find('-')
                        if dashIndex is not -1:
                            writeDict.update({fieldnames[x]: record[values[0]][:dashIndex] })
                        else:
                            try:
                                int(record[values[0]])
                                writeDict.update({fieldnames[x]: record[values[0]]})
                            except:
                                pass
                else:
                    writeDict.update({fieldnames[x]: record.get(values[x], None)})
                    x +=1
=======
                    writeDict.update({fieldnames[x]: record[values[0]]})
                else:
                    writeDict.update({fieldnames[x]: record.get(values[1], None)})
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e
            writer.writerow(writeDict)
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
<<<<<<< HEAD
    print(f"Finished creating {fileNameString}")
=======
    print("Finished creating the product database contents.")
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e


generateCSV('products.csv', products,
            ['id', 'name', 'gender', 'category', 'subcategory', 'subsubcategory', 'brand'],
            ["_id", "name", "gender", "category", "sub_category", "sub_sub_category", "brand"])
<<<<<<< HEAD
# generateCSV('sessions.csv', sessions,
#             ['id', 'segment'],
#             ["_id", "segment"])
# generateCSV('profiles.csv', profiles,
#             ['id', 'browser_id'],
#             ["_id", "buids"])
=======
generateCSV('sessions.csv', sessions,
            ['id', 'segment'],
            ["_id", "segment"])
generateCSV('profiles.csv', profiles,
            ['id', 'browser_id'],
            ["_id", "buids"])
>>>>>>> c7c39c2d46b66c1d5a7fa61ebc0c517db0c9315e

#           BRONVERMELDING
#   Dit is de code die gebruikt is tijdens de les van 5 maart met Nick.