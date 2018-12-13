import sys
import os
import re
import datetime

def computeEvents(inputFile):
    file = open(os.path.join(os.path.dirname(__file__), inputFile), "+r")
    fileContents = file.read().splitlines()
    file.close()

    # read in events and sort by dateTime
    events = []
    guards = {}
    minuteMostFrequentlySlept = 0
    countOfMinuteMostFrequentlySlept = 0
    selectedGuard = 0
    for line in fileContents:
        events.append(eventObject(line))
    events.sort(key=lambda x: x.dateTime)    
    for event in events:
        action = event.action
        if(action == "begins"):
            try:
               guard = guards[event.guard]
            except:
               guard = guardObject(event.guard)
               guards[event.guard] = guard
        if(action == "asleep"):
            guard.sleeps(event.min)
        if(action == "wakes"):
            guard.awakes(event.min)
            if(countOfMinuteMostFrequentlySlept < guard.countOfMostlyFrequencySleptMinute):
                countOfMinuteMostFrequentlySlept = guard.countOfMostlyFrequencySleptMinute
                minuteMostFrequentlySlept = guard.minuteMostFrequentlyAsleep
                selectedGuard = guard.guardNumber


    selection = selectedGuard * guards[selectedGuard].getMinuteMostFrequentlyAsleep()
    print(selection)
    return selection

class guardObject():
    def __init__(self,guardNumber):
        self.guardNumber = guardNumber
        self.sleepStart = 0
        self.minuteMostFrequentlyAsleep = 0
        self.countOfMostlyFrequencySleptMinute = 0
        self.minutesWhenAsleep = [0] * 60

    def sleeps(self,min):
        self.sleepStart = min

    def awakes(self,min):
        for minutes in range(self.sleepStart, min):
            self.minutesWhenAsleep[minutes]+=1
            self.minuteMostFrequentlyAsleep = sorted(range(len(self.minutesWhenAsleep)), key=lambda k: self.minutesWhenAsleep[k])[-1]
            self.countOfMostlyFrequencySleptMinute = self.minutesWhenAsleep[self.minuteMostFrequentlyAsleep]

    def getMinuteMostFrequentlyAsleep(self):
        return self.minuteMostFrequentlyAsleep

class eventObject():


    def __init__(self, eventString):
        self.dateTime = self.getDateTime(eventString)
        self.date = self.getDate(eventString)
        self.hour = int(self.getHour(eventString))
        self.min = int(self.getMin(eventString))
        self.guard = int(self.getGuard(eventString))
        self.action = self.getAction(eventString)

    def getDateTime(self,string):
        matchObj = re.match('.*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', string, re.M|re.I)
        return matchObj.group(1);

    def getDate(self,string):
        matchObj = re.match('.*(\d{2}-\d{2})', string, re.M|re.I)
        return matchObj.group(1);

    def getHour(self,string):
        matchObj = re.match('.*(\d{2}):\d{2}', string, re.M|re.I)
        return matchObj.group(1);

    def getMin(self,string):
        matchObj = re.match('.*\d{2}:(\d{2})', string, re.M|re.I)
        return matchObj.group(1);

    def getGuard(self,string):
        matchObj = re.match('.*#(\d+)', string, re.M|re.I)
        if matchObj is None:
            return False    
        return matchObj.group(1)
        

    def getAction(self,string):
        for actionRegex in ['.*falls (\w+)','.*(\w{5}) up','.*(\w{6}) shift']:
            action = self.runActionRegex(string, actionRegex)
            if(action):
                return action
        return False        

    def runActionRegex(self,string, regex):
        matchObj = re.match(regex, string, re.M|re.I)
        if (matchObj is None):
            return False
        return matchObj.group(1)    

    


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    computeEvents(*sys.argv[1:])