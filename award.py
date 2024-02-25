"""
Prompt the user to input swimming time in minutes and store it in swim_time as an integer
Prompt the user to input cycling time in minutes and store it in cycle_time as an integer
Prompt the user to input running time in minutes and store it in run_time as an integer
Calculate the total_time by adding swim_time, cycle_time, and run_time
Display the total_time in minutes as "Total time is [total_time] minutes."

If total_time is greater than 110:
    - Display "Total time is more than 10 minutes off the qualifying time. No award."
Else if total_time is greater than 105:
    - Display "Total time is within 10 minutes of qualifying time. Award Provincial Scroll."
Else if total_time is greater than 100:
    - Display "Total time is within 5 minutes of qualifying time. Award Provincial Half Colours."
Otherwise:
    - Display "Total time is within the qualifying time. Award Provincial Colours."

"""
swim_time = int(input("Please enter swimming time in minutes: "))
cycle_time = int(input("Please enter cycling time in minutes: "))
run_time = int(input("Please enter running time in minutes: "))
total_time = swim_time + cycle_time + run_time
print("Total time is " + str(total_time) + " minutes.")
if total_time > 110:
    print("Total time is more than 10 minutes off the qualifying time. No award.")
elif total_time > 105:
    print("Total time is within 10 minutes of qualifying time. Award Provincial Scroll.") 
elif total_time > 100:
    print("Total time is within 5 minutes of qualifying time. Award Provincial Half Colours.") 
else:
    print("Total time is within the qualifying time. Award Provincial Colours.")