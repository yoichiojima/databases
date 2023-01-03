from redis_client import RedisClient

r = RedisClient()

def test_reprentation():
    print(f"\nrepresentation: {r}\n")

def test_redis_client_with_str():
    print(f"\nsetting a str and getting it back\n{'=' * 50}")
    r.set("foo", "bar")
    data_taken_back = r.get("foo")

    print(data_taken_back, type(data_taken_back))

    assert data_taken_back == "bar"
    assert isinstance(data_taken_back, str)
    

def test_redis_client_with_list():
    print(f"\nsetting a list and getting it back \n{'=' * 50}")
    r.set("foo", ["bar", "baz"])
    data_taken_back = r.get("foo")

    print(data_taken_back, type(data_taken_back))

    assert data_taken_back == ["bar", "baz"]
    assert isinstance(data_taken_back, list)


def test_redis_client_with_dict():
    print(f"\nsetting a dict and getting it back \n{'=' * 50}")
    r.set("foo", {"bar": "baz"})
    data_taken_back = r.get("foo")

    print(data_taken_back, type(data_taken_back))

    assert data_taken_back == {"bar": "baz"}
    assert isinstance(data_taken_back, dict)