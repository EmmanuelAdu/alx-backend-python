seed = __import__('seed')

def stream_user_ages():
    """ A generator to yield user ages one by one
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row['age']
    
    connection.close()


def calculate_average_age():
    """ Calculate the average age using the stream_user_ages generator
    """
    total_age = 0
    count_age = 0
    for age in stream_user_ages():
        total_age += age
        count_age +=1
    

    if count_age == 0:
        print("No users in dataset")
        return
    
    average = total_age / count_age
    print(f"Average age of users: {average:.2f}")

