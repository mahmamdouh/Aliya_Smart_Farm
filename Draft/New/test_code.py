from DHT_Module import DHT_Update_10_min


while True:
    print("=======================================")
    temp= DHT_Update_10_min()
    print("temprate")
    print(temp)
