from easygui import * 
import sys

records = [
    dict([('LastName', '??????'),    ('FirstName', '????'),     ('MiddleName', "????????"),    ('phone','(222)-111-3434')]),
    dict([('LastName', '??????'),    ('FirstName', '????'),     ('MiddleName', "????????"),    ('phone','(222)-222-3434')]),
    dict([('LastName', '???????'),   ('FirstName', '????????'), ('MiddleName', "????????"),    ('phone','(222)-333-3434')]),
    dict([('LastName', '?????????'), ('FirstName', '????????'), ('MiddleName', "????????"),    ('phone','(222)-444-3434')]),
    dict([('LastName', '?????????'), ('FirstName', '?????'),    ('MiddleName', "???????????"), ('phone','(222)-555-3434')]),
]

def findIndexInRecord(person):
    index = 0
    for item in records:
        print(item['LastName'],'  ', person.split(' ')[0])

        if (item['LastName'] == person.split(' ')[0] and
            item['FirstName'] == person.split(' ')[1] and
            item['MiddleName'] == person.split(' ')[2] and
            item['phone'] == person.split(' ')[3]
            ): return index
        index +=1
    return -1   
 
def addRecord(items):
    records.append(dict([('LastName', items[0]),    
                         ('FirstName', items[1]),     
                         ('MiddleName',items[2]),    
                         ('phone',items[3])]))

def editRecord(old_items, newItems):

    recIndex = findIndexInRecord(old_items)
    records[recIndex]['LastName']=newItems[0]
    records[recIndex]['FirstName']=newItems[1]
    records[recIndex]['MiddleName']=newItems[2]
    records[recIndex]['phone']=newItems[3]
    
    

def getPeople(listOfRecord):
    people = []
    for person in listOfRecord:       
        people.append(person['LastName']+' '+person['FirstName']+' '+person['MiddleName']+' '+person['phone'])
    return people

def deletePerson(person):
    print('??????? '+person)
    name = person.split(' ')[0]  
    del records[findIndexInRecord(person)]

def editPerson(person):
    print('???????????'+person) 

def searchBook():
    msg ="???????? ?? ??????"
    title = "?????????? ?????"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        msgbox("??? ?????: {}".format(choice), "Survey Result")
        return
    
def searchBookRetrun():
    msg ="???????? ?? ??????"
    title = "?????????? ?????"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return      
        return choice

def addBook():
    title = "????? ??????"
    msg = "????????? ??? ????"
    fieldNames = ["???????", "???", "????????", "???????"]
    fieldValues = multenterbox(msg, title, fieldNames)  
    if fieldValues is None:
        return
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            return # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            return
    print("Reply was:{}".format(fieldValues)) 
    addRecord(fieldValues)  
    return 

def deleteBook():
    msg ="???????? ?? ?????? ??? ????????"
    title = "?????????? ?????"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        result = ccbox("??????? : {}".format(choice), "????? ??????")
        if(result): 
            deletePerson(choice) 
            return
        else:  
            print('cancelled',choice, result)
            return

def editBook():
    person = searchBookRetrun()
    print(person)
    personItems = person.split(' ')
    title = "????????????? ??????"
    msg = "????????? ??? ????"
    fieldNames = ["???????", "???", "????????", "???????"]
    oldNames = person.split(' ')
    fieldValues = multenterbox(msg, title, fieldNames, oldNames)  
    if fieldValues is None:
        sys.exit(0)
    while 1:
        errmsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errmsg += "{} is a required field.\n\n".format(name)
        if errmsg == "":
            break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    print("Reply was:{}".format(fieldValues)) 
    editRecord(person, fieldValues)  
    return 


def mainWindow():
    msg ="????? ?????????? ? ?????????? ????? !"
    choices = ["??????","????????","?????????????","???????","?????"]
    reply = buttonbox(msg,  choices=choices)
    match reply:
        case "??????":
            print('??????')
            searchBook()
        case "????????":
            print('????????')
            addBook()
        case "?????????????":
            print('?????????????')
            editBook()
        case "???????":
            print('???????')
            deleteBook()
        case _:
            print('?????')           
    return reply        

while 1:
   reply = mainWindow()
   if reply == '?????':  sys.exit(0)      



