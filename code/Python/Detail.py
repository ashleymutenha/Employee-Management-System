
class Details:
    def __init__(self,cur,con):
        self.cur =cur
        self.con =con
        self.people = {"Username":"","DOB":"","Gender":"","Email":"","Location":""}
        self.counter =0
        self.placeholder ="khlj"
        self.lastItem = self.getDetails().index(self.getDetails()[-1])
        self.final =[]
        self.personDetails=[]
      
    def getDetails(self):#Fetching Details from Database
        self.details=[]
        self.cur.execute("SELECT * FROM credentials")
        for i in self.cur:
            for e in i:
                self.details.append(e)
        return self.details

    def login(self,name):
        is_member =self.getDetails().count(name)
        if is_member==1:
            return name 
        else:
            return "No Name"


    def insertDetails(self):
            #Extracting Details for the first user
            allPeople =self.getDetails()[0:self.lastItem]
            lastpoint = len(self.people)
            peopleList = self.getDetails()[0:lastpoint]
            for i in self.people:
                for e in peopleList:
                    if len(self.people[i])==0:
                        if len(e)==0:
                            self.people.__setitem__(i,self.placeholder)
                            peopleList.remove(e)
                        else:
                            self.people.__setitem__(i,e)
                            peopleList.remove(e)

            #If there are other users 
            if len (allPeople)>len(self.people):
                startpoint =len(self.people)
                self.newPeople = self.getDetails()[startpoint:self.lastItem+1]
                self.final =[]
                loop = round(self.lastItem/startpoint)-1
                while self.counter!=loop:
                    person = self.people.copy()
                    for i in person:
                        person[i]=""
                    for i in person:
                        for e in self.newPeople:
                            if len(person[i])==0:
                                if len(e)==0:
                                    person.__setitem__(i,self.placeholder)
                                    self.newPeople.remove(e)
                                else:
                                    person.__setitem__(i,e)
                                    self.newPeople.remove(e)
                    self.counter+=1
                    self.final.append(person)
            else:
                pass
            self.final.insert(0,self.people)

            for i in self.final:
                if i==self.placeholder:
                    i=""
                    
            return(self.final)

    def addPeople(self,name,dob,gender,email,location):#adding users to db
        self.cur.execute("INSERT INTO credentials VALUES(%s,%s,%s,%s,%s)",(name,dob,gender,email,location))
        self.con.commit()

    def deleteUsers(self,name):
        self.cur.execute("DELETE FROM credentials WHERE username =%s",(name))
        self.con.commit()



