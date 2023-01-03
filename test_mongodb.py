from mongodb import MongoDB

mongo = MongoDB().client
db = mongo.test

def init():
    db.test.delete_many({"status": "Inserted."})

def test_insert_one():
    init()
    print(f"\ntest_insert_one\n{'=' * 50}\n")
    db.test.insert_one({"status": "Inserted."})
    assert len(list(db.test.find())) == 1
    db.test.delete_one({"status": "Inserted."})

def test_insert_many():
    init()
    print(f"\ntest_insert_many\n{'=' * 50}\n")
    db.test.insert_many([{"status": "Inserted."} for _ in range(10)])
    assert len(list(db.test.find())) == 10
    db.test.delete_many({"status": "Inserted."})

def test_delete_many():
    init()
    print(f"\ntest_delete_many\n{'=' * 50}\n")
    db.test.insert_many([{"status": "Inserted."} for _ in range(10)])
    db.test.delete_many({"status": "Inserted."})
    assert len(list(db.test.find())) == 0