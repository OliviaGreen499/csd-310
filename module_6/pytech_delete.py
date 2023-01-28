from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.k1mrjrp.mongodb.net/?retryWrites=true&w=majority')


db = client.pytech


students = db.students

 
record = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in record:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


new_doc = {
    "student_id": "1010",
    "first_name": "Janet",
    "last_name": "Lee"
}


new_doc_id = students.insert_one(new_doc).inserted_id


print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_doc_id))


student_new_doc = students.find_one({"student_id": "1010"})


print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_new_doc["student_id"] + "\n  First Name: " + student_new_doc["first_name"] + "\n  Last Name: " + student_new_doc["last_name"] + "\n")


deleted_student_new_doc = students.delete_one({"student_id": "1010"})


new_record = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

 
for doc in new_record:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


input("\n\n  End of program, press any key to continue...")
