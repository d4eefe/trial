import htmap as ht

if __name__ == "__main__":
    future = ht.load("test-1")

    for result in future:
        print(result)
