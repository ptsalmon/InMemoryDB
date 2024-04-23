class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction_in_progress = False
        self.transaction_data = {}

    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in progress")
        self.transaction_in_progress = True
        self.transaction_data = self.data.copy()

    def put(self, key, value):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_data[key] = value

    def get(self, key):
        return self.transaction_data.get(key)

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.data = self.transaction_data.copy()
        self.transaction_in_progress = False

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_in_progress = False
        self.transaction_data = {}

if __name__ == "__main__":
    inmemoryDB = InMemoryDB()
    
    print("get A:")
    print(inmemoryDB.get("A"))
    print("\nput A 5:")
    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print("Error:", e)

    print("\nbegin_transaction:")
    print(inmemoryDB.begin_transaction())
    print("\nput A 5:")
    print(inmemoryDB.put("A", 5))
    
    print("\nget A:")
    print(inmemoryDB.get("A"))
    
    print("\nput A 6:")
    print(inmemoryDB.put("A", 6))
    
    print("\ncommit")
    print(inmemoryDB.commit())
    
    print("\nget A:")
    print(inmemoryDB.get("A"))
    
    print("\ncommit:")
    try:
        inmemoryDB.commit()
    except Exception as e:
        print("Error:", e)
        
    print("\nrollback")
    try:
        inmemoryDB.rollback()
    except Exception as e:
        print("Error:", e)
        
    print("\nget B:")
    print(inmemoryDB.get("B"))
    
    print("\nbegin_transaction:")
    print(inmemoryDB.begin_transaction())
    
    print("\nput B 10:")
    print(inmemoryDB.put("B", 10))
    
    print("\nrollback:")
    print(inmemoryDB.rollback())
    
    print("\nget B:")
    print(inmemoryDB.get("B"))
    
        
        
    
    
    
