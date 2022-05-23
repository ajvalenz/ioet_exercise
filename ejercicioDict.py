import datetime
import time

completeSchedule = {}


def fileReader(file_name):
    document = open(file_name, 'r')
    employee = document.readline()

    while employee:  # read all lines until the end of line is found
        schedules = employee.split('=')[1].split('\n')[0].split(',')#splitting the schedule from an employee and taking the new line character out
        name = employee.split('=')[0]  # obtaining the name of the employee
        completeSchedule[name] = schedules  # creating a key and value for the dictionary
        employee = document.readline()
    document.close()
    print("Reading File ...")
    time.sleep(1)
    # print(completeSchedule)
    return completeSchedule


def comparingHours(completeSchedule):
    completedEmployees = []  # list of employees that were reviewed
    for employee, scheduledWork in completeSchedule.items(): #Takes one employee with his/her schedule
        for coworker, scheduleCoworker in completeSchedule.items(): #takes a coworker with his /her schedule
            pairs = 0 # number of times together
            if employee != coworker: #checks its not the same employee
                if (coworker not in completedEmployees): #
                    for hourWork in scheduledWork:
                        dayWork = hourWork[0:2]
                        timeWork = hourWork[2:]
                        startEmployee = datetime.datetime.strptime(timeWork.split('-')[0].replace(" ", ''),'%H:%M').time() #creates a datetime object for the check in
                        endEmployee = datetime.datetime.strptime(timeWork.split('-')[1].replace(" ", ''),'%H:%M').time() #creates a datetime object for the check out
                        for hourCoworker in scheduleCoworker:
                            dayCoworker = hourCoworker[0:2]
                            timeCoworker = hourCoworker[2:]
                            startCoworker = datetime.datetime.strptime(timeCoworker.split('-')[0].replace(" ", ''),'%H:%M').time() #creates a datetime object for the check in (coworker)
                            endCoworker = datetime.datetime.strptime(timeCoworker.split('-')[1].replace(" ", ''),'%H:%M').time() #creates a datetime object for the check out(coworker)
                            if dayWork == dayCoworker:
                                if (startEmployee <= startCoworker and endEmployee >= startCoworker):
                                    pairs += 1
                                elif (startCoworker <= startEmployee and endCoworker >= startCoworker):
                                    pairs += 1
                                elif (startEmployee <= endCoworker and endEmployee >= endCoworker):
                                    pairs += 1
                                elif (startCoworker <= endEmployee and endCoworker >= endEmployee):
                                    pairs += 1
                    completedEmployees.append(employee) #adds employee already checked
                    print(employee, '-', coworker, ': ', pairs) #prints output


fileReader('employee.txt')
comparingHours(completeSchedule)
