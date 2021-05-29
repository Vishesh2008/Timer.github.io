
import time
num_secs = input("Enter the countdown seconds: ")

def timer(num_secs):
    while num_secs:
        mins,secs = divmod(num_secs,60)

        count ="{:02d}:{:02d}".format(mins,secs)
        print(count, end ="\r")
        time.sleep(1)

        num_secs = num_secs-1

    print("Time is up!")
timer(int(num_secs))
