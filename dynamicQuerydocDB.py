import pymongo

class DocDbClient:
    def __init__(self, username, password, instance_endpoint, port=27017, database="AutomateRouterDB"):
        self.username = username
        self.password = password
        self.instance_endpoint = instance_endpoint
        self.database = database
        conn = f"mongodb://{self.username}:{self.password}@{instance_endpoint}:{port}/{database}?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false"
        self.client = pymongo.MongoClient(conn)

    def insert(self, collection, data):
        try:
            result = self.client[self.database][collection].insert_one(data)
            return result.inserted_id
        except Exception as e:
            print(f"Error creating document: {e}")
            return None

    def insert_many(self, collection, data_list):
        try:
            result = self.client[self.database][collection].insert_many(data_list)
            return result.inserted_ids
        except Exception as e:
            print(f"Error creating documents: {e}")
            return []

    def find(self, collection, command="find_many", sort=None, query=None):
        try:
            if command not in ["find_one", "find_many"]:
                raise ValueError("Invalid command. Must be one of ['find_one', 'find_many']")

            cursor = self.client[self.database][collection]

            if sort:
                sort_params = [(sort_item["column_name"], pymongo.ASCENDING if sort_item["ascending"] else pymongo.DESCENDING) for sort_item in sort]
                cursor = cursor.sort(sort_params)

            if query:
                if command == "find_one":
                    result = cursor.find_one(query)
                    return result if result else {}
                else:
                    result = cursor.find(query)
                    return list(result)
            else:
                return []

        except Exception as e:
            print(f"Error reading documents: {e}")
            return []

    def update_one(self, collection, filter, update_data):
        try:
            result = self.client[self.database][collection].update_one(
                filter, update_data
            )
            return result.matched_count
        except Exception as e:
            print(f"Error updating document: {e}")
            return 0

    def update_many(self, collection, filter, update_data):
        try:
            result = self.client[self.database][collection].update_many(
                filter, update_data
            )
            return result.modified_count
        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

    def delete_one(self, collection, filter):
        try:
            result = self.client[self.database][collection].delete_one(filter)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting document: {e}")
            return 0

    def delete_many(self, collection, filter):
        try:
            result = self.client[self.database][collection].delete_many(filter)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0

def build_dynamic_query():
    query_filters = []
    while True:
        column = input("Enter column name: ").strip()
        if column.lower() == "done":
            break
        operator = input("Enter operator: ").strip()
        value = input("Enter value: ").strip()
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass 
        query_filters.append({column: {operator: value}})
    return {"$and": query_filters}

def main():
    username = "MyDB"
    password = "Ayush123"
    instance_endpoint = "docdb-2023-12-16-04-06-01.cznhzxmc5c04.ap-northeast-1.docdb.amazonaws.com"

    client = DocDbClient(username, password, instance_endpoint)

    query_filters = build_dynamic_query()
    query_command = "find_many"
    
    query_params = {
        "command": query_command, 
        "query": query_filters,
    }

    print("Query Parameters: ", query_params)
    documents = client.find("myCollection", **query_params)
    for doc in documents:
        print(f"Document: {doc}")

if __name__ == "__main__":
    main()
