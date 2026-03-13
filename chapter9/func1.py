#WRP to greet user With Good Morning, Good Afternoon, Good Evening based on time of day 

import datetime
current_time = datetime.datetime.now().time()
if current_time < datetime.time(12):
    print("Good Morning!")
elif current_time < datetime.time(18):
    print("Good Afternoon!")
else:
    print("Good Evening!")  
    
def greet():
    name = input("Enter your name: ")
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        print(f"Good Morning {name}!")
    elif current_time < datetime.time(18):
        print(f"Good Afternoon {name}!")
    else:
        print(f"Good Evening {name}!")
    # return greet()
    print("Have a nice day!")
    
greet()