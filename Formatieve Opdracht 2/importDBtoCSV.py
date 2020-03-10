from pymongo import MongoClient
import csv

envvals = ["MONGODBUSER", "MONGODBPASSWORD", "MONGODBSERVER", "RECOMADDRESS"]
dbstring = 'mongodb+srv://{0}:{1}@{2}/test?retryWrites=true&w=majority'

client = MongoClient()
database = client.huwebshop

products = database.products.find()
sessions = database.sessions.find()
profiles = database.profiles.find()


"""
-- -----------------------------------------------------
-- Generate products.csv file
-- -----------------------------------------------------
"""

"""
-- -----------------------------------------------------
-- Generate products.csv file
-- -----------------------------------------------------
"""

print("Creating the product database contents...")
with open('products.csv', 'w', newline='', encoding='utf-8') as csvout:
    fieldnames = ['id', 'name', 'gender', 'category', 'subcategory', 'subsubcategory', 'brand']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    c = 0
    for product in products:
        writer.writerow({'id': product["_id"],
                         'name': product.get("name", None),
                         'gender': product.get("gender", None),
                         'category': product.get("category", None),
                         'subcategory': product.get("sub_category", None),
                         'subsubcategory': product.get("sub_sub_category", None),
                         'brand': product.get("brand", None)
                         })
        c += 1
        if c % 10000 == 0:
            print("{} product records written...".format(c))
print("Finished creating the product database contents.")\

"""
-- -----------------------------------------------------
-- Generate sessions.csv file
-- -----------------------------------------------------
"""
print("Creating the sessions database contents...")
with open('sessions.csv', 'w', newline='', encoding='utf-8') as csvout:
    fieldnames = ['id', 'segment']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    c = 0
    for session in sessions:
        writer.writerow({'id': session["_id"],
                         'segment': session.get("segment", None)
                         })
        c += 1
        if c % 10000 == 0:
            print("{} product records written...".format(c))
print("Finished creating the session database contents.")

"""
-- -----------------------------------------------------
-- Generate profiles.csv file
-- -----------------------------------------------------
"""
print("Creating the profile database contents...")
with open('profiles.csv', 'w', newline='', encoding='utf-8') as csvout:
    fieldnames = ['id', 'browser_id']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    c = 0
    for profile in profiles:
        writer.writerow({'id': profile["_id"],
                         'browser_id': profile.get("buids", None)
                         })
        c += 1
        if c % 10000 == 0:
            print("{} product records written...".format(c))
print("Finished creating the profile database contents.")

#           BRONVERMELDING
#   Dit is de code die gebruikt is tijdens de les van 5 maart met Nick.
