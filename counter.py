def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    sender_day = []
    days_dict= dict()

    with open(file_name, 'r') as user_file:
        local_file = user_file.readlines()

    for line in local_file:
        if line.startswith('From '):
            sender_day.append(line.split(' ')[2])
    for key in sender_day:
        days_dict[key] = days_dict.get(key,0) +1
    print(days_dict)



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
