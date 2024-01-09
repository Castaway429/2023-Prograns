import time

#Time when your computer thinks time began (epoch)
print(time.ctime(10))

print(" ")

#Seconds since epoch
print(time.time())

print(" ")

#Current Time
print(time.ctime(time.time()))

print(" ")

#Also get current time
time_object = time.localtime()
print(time_object)

#Turn time object to a readable format
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)

print(" ")

#Easily Readable Version
print(local_time)

print(" ")

time_string = "20 April 2020"
time_object = time.strptime(time_string, "%d %B %Y")
print(time_object)

print(" ")

#Timer Function
#myTime = int(input("Enter the time you want in seconds: "))

#count forwards use (0, myTime)

#for x in range (myTime, 0, -1):
#    seconds = x % 60
#    minutes = int(x / 60) % 60
#    hours = int(x / 3600)
#    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #:02 pads the text to add an extra zero / not go over 2 place holders

#    time.sleep(1)

print("Times up!")

#Alarm Function
myAlarm = input("Enter your desired alarm time like this HH:MM AM: ")

alarm_object = time.strptime(myAlarm, "%I:%M %p")

print(alarm_object)