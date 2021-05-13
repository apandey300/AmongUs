## This program is a recreation of the Game of Among Us.
## Author: Akanksha Pandey

##Creates the rooms that crewmates will travel to to complete task
class Room:
    def __init__(self, name): 
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
        
    def __repr__(self): 
        return "Room(name: {})".format(self.name)

##Tasks that crewmates will have to complete
class Task:
    def __init__(self,name,isCompleted=False):
        self.name = name
        self.isCompleted = isCompleted
        
    def __repr__(self):
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)
    
    def __eq__(self, other):
       return (self.name, self.isCompleted) == (other.name,other.isCompleted)
##vote who to eliminate from the game
    def vote(self,amongUsObj):
        for crewmate in amongUsObj.crewmates:
            if self.name != crewmate.name and self.name[0] == crewmate.name[0] and crewmate.isAlive == True:
                return crewmate.name
        for impostor in amongUsObj.imposters:
            if self.name != impostor.name and self.name[0] == impostor.name[0] and impostor.isAlive == True:
                return impostor.name

##used to call meeting if crewmate stumbles upon elminated crewmate's body       
    def callMeeting(self, amongUs):
        votes = 0
        voteDict = {}
        voters = amongUs.imposters + amongUs.crewmates
        for member in voters:
            return member.vote(amongUs)
##creating all the crewmates that will be present in the game       
class Crewmate:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.tasksDone = 0

    def __repr__(self):  
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other):
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)
    
    def doTask(self,other):
        if other.isCompleted == False:
            other.isCompleted == True
            return self.tasksDone + 1
        else:
            return "Nothing to do here."

    def vote(self, amongUsObj):
        for crewmate in amongUsObj.crewmates:
            if self.name[0] == crewmate.name[0] and self.name != crewmate.name and crewmate.isAlive == True:
                return crewmate
        for impostor in amongUsObj.impostors:
            if self.name[0] == impostor.name[0] and self.name != impostor.name and impostor.isAlive == True:
                return impostor
          
    def callMeeting(self,amongUsObj):
        for member1 in amongUsObj.crewmates:
            return member1.vote(amongUsObj)
        for member2 in amongUsObj.impostors:
            return member2.vote(amongUsObj)

        for member1 in amongUsObj.impostors:
                mostVotedMember = Impostor
        for member2 in amongUsObj.crewmates:
                mostVotedMember = Crewmate
        voteDict = {}
        voters = amongUsObj.impostors + amongUsObj.crewmates
        for member in voters:
            voteDict[member] = 0
        if member in (amongUsObj.crewmates or amongUsObj.impostors):
            member.name.vote(amongUsObj)
            

            
        if type(mostVotedMember) == Impostor:
            mostVotedMember.isAlive = False
            return "{} was An Impostor".format(mostVotedMember.name)
        elif type(mostVotedMember) == Crewmate:
            mostVotedMember.isAlive = False
            return " {} was not An Impostor.".format(mostVotedMember.name)
                
##creating a hidden imposter within the game   
class Impostor:
    def __init__(self, name,color, accessories= ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.eliminateCount = 0
        
    def __repr__(self): 
        return "Impostor(name: {}, color: {})".format(self.name, self.color)
    
    def __str__(self):
        return "My name is {} and I'm an impostor.".format(self.name)
    
    def eliminate(self,amongUsObj):
        if isinstance(amongUsObj,Impostor):
            return "They're on your team -_-"
        else:
            amongUsObj.isAlive = False
            self.eliminateCount += 1
    
    def vote(self, amongUsObj):
        for player in amongUsObj.crewmates:
            if self.name[0] == player.name[0] and self.name != player.name and player.isAlive == True:
                return player
        for player2 in amongUsObj.imposters:
            if self.name[0] == player2.name[0] and self.name != player2.name and player2.isAlive == True:
                return player2
                
    def __eq__(self, other):
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.rooms = {}
        self.crewmates = []
        self.impostors = []
        
    def gameOver(self):
        if len(self.crewmates) == 0:
            return "Defeat! All crewmates have been elminated."
        elif len(self.impostors) == 0:
            return "Victory! All impostors have been eliminated."
        else:
            return "Game is not over yet."

    
    def registerPlayer(self,object1):
        if len(self.crewmates)+ len(self.impostors) == self.maxPlayers:
            return "Lobby is full."
        for playerObject in self.crewmates: 
            if object1.name == playerObject.name:
                return "Player with name: {} exists.".format(playerObject.name)
        for playerObject1 in self.impostors:
            if object1.name == playerObject1.impostors:
                return "Player with name: {} exists.".format(playerObject1.name)
        else:
            if type(object1) == Crewmate:
                self.crewmates.append(object1)
            elif type(object1) == Impostor:
                self.impostors.append(object1)
                
    def registerTask(self,task,room):
        for roomtask in self.rooms.values():
            if task in roomtask:
                return "This task has already been registered."
        else:
            if room.name not in self.rooms.keys():
                    self.rooms[room.name] = []
            if task not in self.rooms[room.name]:
                    self.rooms[room.name].append(task)
                 
    def __repr__(self):
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)