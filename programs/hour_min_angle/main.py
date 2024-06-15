#this program requests a time which is in the format of hh:mm or hour:minutes
#it computes the angle between the clock hands at that time
# e.g.
# Enter the time : 5:30
# The time 5:30 has an angle of 30.0 degrees between the clock's hands.
class Clock:
    
    def __init__(self):
        self.time = input("Enter the time : ")
        list = self.time.split(':') # a list of two strings obtained by spliting input hh:mm
        self.h = int(list[0]) # conversing string into int
        self.m = int(list[1]) # conversing string into int
        if self.m > 59 or self.h > 12: 
            print("minutes should not be more than 59 and hour should not be more than 12")
            exit(0) # exit the program if the minutes and hours are beyond 59 and 12

        self.hours = dict() # to make a dictionary
        for a in range(1,13): # adding keys (1-12) with values (5,10,15,...60)
            self.hours[a] = a*5

    def angle(self): # function of caluclulating degrees
        self.hm = self.hours[self.h] # e.g. if h is 2, hm will be 10 (transforming hours into minutes, hm)
        if self.hm > self.m: # if the minutes in the hour is more than the original minutes, m
            self.degree = float((self.hm - self.m)*6) # the angle is the subtraction of m from hm
        elif self.hm < (self.m):# if the minutes in the hour is less than the original minutes, m
            self.degree = float((self.m - self.hm)*6) # the angle is the subtraction of hm from m
        else:
            self.degree = 0
        if self.degree > 180: # if the degree is more than 180
            self.degree = 360 - self.degree # subtract it from 360

    def display(self): # funciton for displaying output
        print("The time {0} has an angle of {1} degrees between the clock's hands.".format(self.time,self.degree))

a = Clock()
a.angle()
a.display()




