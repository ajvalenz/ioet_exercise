# ioet_exercise

the following README file purpose is to explain a programming excercise as part of a recruitment process

# Excercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

# Solution 

As explain  previously we recive a txt file with which we can obtain the information of every employee .
After reading the file , it is important to store this information to work with it and show the OUTPUT. 
that been said asuming each line of the file will always have a name followed by the schedule of that employee, the best way to store this information is by creating a dictionary where the key is the name of each employee and the schedule the value.

Once the file is fully read ,we need to compare the schedule of every employee with every coworker on the same day and if the time frames are the same or the met at the office over a fraction of time then they have coincided.

To compare the schedule , the string value obtain from the dictionary is converted to a daytime object depending on the format (in this case %H:%M) 
Once the schedules are compared , the name of the coworker is added to a list to make sure we dont repeat cowerks to compare .

# Flow chart 

# Instructions to compile

For this excercise it is necesary to have python 3 installed 

To run the exercise , use the cmd and the commands ls and cd to show and move around  oyur directories until you are on the directory with the py file 

Once there ,use the command py or python followed by the name of the file to run it as shown in the picture bellow

![image](https://user-images.githubusercontent.com/67160144/169714763-50ed1761-05b2-49c6-b525-a99e0c1d173c.png)




