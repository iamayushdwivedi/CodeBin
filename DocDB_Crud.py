from pymongo import MongoClient
import uuid 

class DocumentDBManager:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating document: {e}")
            return None

    def create_many(self, data_list):
        try:
            result = self.collection.insert_many(data_list)
            return result.inserted_ids
        except Exception as e:
            print(f"Error creating documents: {e}")
            return []

    def read(self, query=None):
        try:
            if query:
                result = self.collection.find(query)
            else:
                result = self.collection.find()
            return list(result)
        except Exception as e:
            print(f"Error reading documents: {e}")
            return []

    def get_all_pages(self, query=None, page_size=10):
        try:
            page_number = 1
            all_pages = []

            while True:
                if query:
                    total_count = self.collection.count_documents(query)
                    result = self.collection.find(query).skip((page_number - 1) * page_size).limit(page_size)
                else:
                    total_count = self.collection.count_documents({})
                    result = self.collection.find().skip((page_number - 1) * page_size).limit(page_size)
            
                page_data = list(result)
                all_pages.append(page_data)

                if len(page_data) < page_size:
                    break
            
                page_number += 1
        
            return all_pages
        except Exception as e:
            print(f"Error fetching all pages: {e}")
            return []


    def update(self, query, new_data):
        try:
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0

#Client information
uri = "mongodb://MyDB:Ayush123@docdb-2023-12-16-04-06-01.cznhzxmc5c04.ap-northeast-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false"
db_name = "my_database"
collection_name = "my_col"

# Instantiating the class
document_manager = DocumentDBManager(uri, db_name, collection_name)

data_to_insert = {
    "_id": str(uuid.uuid4()),
    "name": "Mayank Srivastava",
    "age": 23,
    "email": "mayank_srivastava@example.com"
}

documents = [
    {"_id": str(uuid.uuid4()),"name": "Ayush Dwivedi", "age": 23, "email": "ayush_dwivedi@example.com"},
    {"_id": str(uuid.uuid4()), "name": "Aman Saxena", "age": 23, "email": "aman_saxena@example.com"},
    {"_id": str(uuid.uuid4()), "name": "Amar Nath Tripathi", "age": 24, "email": "amarnath_tripathi@example.com"},
]

# # (C)reate
# inserted_id = document_manager.create(data_to_insert)
# if inserted_id:
#     print(f"Document inserted with ID: {inserted_id}")

inserted_ids = document_manager.create_many(documents)
print(f"Inserted {len(inserted_ids)} documents.")

# # (R)ead
all_documents = document_manager.read()
print("All Documents:")
print(all_documents)

#Pagination

all_pages = document_manager.get_all_pages()
for page_number, page_data in enumerate(all_pages, start=1):
    print(f"Page {page_number}:")
    print(page_data)

# # (U)pdate
# update_query = {"name": {"$in": ["Ayush Dwivedi", "Shreya Joshi"]}}
# new_data = {"age": 21}
# updated_count = document_manager.update(update_query, new_data)
# print(f"Updated {updated_count} documents.")

# updated_documents = document_manager.read({"name": {"$in": ["Ayush Dwivedi", "Shreya Joshi"]}})
# print("Updated Documents:")
# print(updated_documents)

# (D)eletes
# delete_query = {}
# deleted_count = document_manager.delete(delete_query)
# print(f"Deleted {deleted_count} documents.")
