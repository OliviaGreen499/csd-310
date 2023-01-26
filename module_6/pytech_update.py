
from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.k1mrjrp.mongodb.net/?retryWrites=true&w=majority')


db = client.pytech


students = db.students

 
record = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


record = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


for doc in record:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "banks"}})

 
fred = students.find_one({"student_id": "1007"})


print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")


print("  Student ID: " + fred["student_id"] + "\n  First Name: " + fred["first_name"] + "\n  Last Name: " + fred["last_name"] + "\n")


input("\n\n  End of program, press any key to continue...")