'''
Name: Jesse Moyer
Date: 02/23/22

This program will take in the number of seconds 
and convert that to HH:MM:SS

Step 1: input # of seconds
Step 2: convert seconds to minutes and hours
Step 3:print out HH:MM:SS from inputed seconds

'''

def convert_sec_to_hrs(seconds):
    hours = seconds // 3600
    return hours

def convert_sec_to_min(seconds):
    minutes = seconds // 60
    return minutes

def main():
    seconds = int(input("Please enter the number of seconds: "))

    hours = convert_sec_to_hrs(seconds)
    minutes = convert_sec_to_min(seconds - (hours*3600))

    #3661 seconds = 01:01:01 / 1:1:1
    print(f"The time format of {seconds} seconds is: {hours}:{minutes}:{seconds%60}")
    pass 

main()