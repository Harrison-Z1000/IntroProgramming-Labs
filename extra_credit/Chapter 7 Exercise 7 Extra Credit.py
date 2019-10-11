# Introduction to Programming
# Author: Harrison Zheng
# Date: 10/11/19
# This program calculates the amount that a babysitter earns in a babysitting period.


def main():
    print("This program calculates the amount that a babysitter earned in a babysitting period.")
    startTime = input("Enter the starting time in the format of 'HH:MM AM/PM': ")
    endTime = input("Enter the ending time in the format of 'HH:MM AM/PM': ")
    militaryStartTime = convertStartTimeToMilitary(startTime)
    militaryEndTime = convertEndTimeToMilitary(endTime)
    totalHoursWorked = totalHours(militaryStartTime, militaryEndTime)
    hoursWorkedAfterNine = hoursAfterNine(militaryStartTime, militaryEndTime)
    totalAmountEarned = ((totalHoursWorked - hoursWorkedAfterNine) * 2.50) + (hoursWorkedAfterNine * 1.75)  # Since
    # the rate of pay changes for any hours worked after 9 PM, those hours need to be subtracted from the total in
    # the babysitting period.
    print("The babysitter earned $", round(totalAmountEarned, 2))  # Money is usually expressed with two decimal places.


def convertStartTimeToMilitary(startTime):  # Converts the time that the babysitting period started at from standard
    # into military time
    if startTime[6] == "A" and startTime[:2] == "12":
        return "00" + startTime[2:5]
    elif startTime[6] == "A" and startTime[:2] != "12":
        return startTime[:5]
    elif startTime[6] == "P" and startTime[:2] == "12":
        return startTime[:5]
    else:
        return str(int(startTime[:2]) + 12) + startTime[2:5]


def convertEndTimeToMilitary(endTime):  # Converts the time that the babysitting period ended at from standard
    # into military time
    if endTime[6] == "A" and endTime[:2] == "12":
        return "00" + endTime[2:5]
    elif endTime[6] == "A" and endTime[:2] != "12":
        return endTime[:5]
    elif endTime[6] == "P" and endTime[:2] == "12":
        return endTime[:5]
    else:
        return str(int(endTime[:2]) + 12) + endTime[2:5]


def totalHours(militaryStartTime, militaryEndTime):  # Calculates the precise number of hours that a babysitter
    # worked in a period based on when their shift started and ended
    startHour = int(militaryStartTime[:2])
    endHour = int(militaryEndTime[:2])
    startMinute = int(militaryStartTime[3:5])
    minutesTillNextHour = 60 - startMinute
    hoursToMinutes = (endHour - (startHour + 1)) * 60
    minutesTillEndTime = int(militaryEndTime[3:5])
    return (minutesTillNextHour + hoursToMinutes + minutesTillEndTime) / 60


def hoursAfterNine(militaryStartTime, militaryEndTime):  # Calculates the precise number of hours that a babysitter
    # worked after 9:00 PM
    if int(militaryStartTime[:2]) < 21 < int(militaryEndTime[:2]):
        hoursConverted = (int(militaryEndTime[:2]) - 21) * 60
        minutesTillEndTime = int(militaryEndTime[3:5])
        return (hoursConverted + minutesTillEndTime) / 60
    elif int(militaryStartTime[:2]) >= 21:
        startHour = int(militaryStartTime[:2])
        endHour = int(militaryEndTime[:2])
        startMinute = int(militaryStartTime[3:5])
        minutesTillNextHour = 60 - startMinute
        hoursToMinutes = (endHour - (startHour + 1)) * 60
        minutesTillEndTime = int(militaryEndTime[3:5])
        return (minutesTillNextHour + hoursToMinutes + minutesTillEndTime) / 60
    else:
        return 0


main()
