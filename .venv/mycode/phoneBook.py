from easygui import * 
import sys

records = [
    dict([('LastName', 'Иванов'),    ('FirstName', 'Иван'),     ('MiddleName', "Иванович"),    ('phone','(222)-111-3434')]),
    dict([('LastName', 'Петров'),    ('FirstName', 'Петр'),     ('MiddleName', "Иванович"),    ('phone','(222)-222-3434')]),
    dict([('LastName', 'Сидоров'),   ('FirstName', 'Спиридон'), ('MiddleName', "Иванович"),    ('phone','(222)-333-3434')]),
    dict([('LastName', 'Степанова'), ('FirstName', 'Светлана'), ('MiddleName', "Ивановна"),    ('phone','(222)-444-3434')]),
    dict([('LastName', 'Живенькая'), ('FirstName', 'Ольга'),    ('MiddleName', "Григорьевна"), ('phone','(222)-555-3434')]),
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
    print('удаляем '+person)
    name = person.split(' ')[0]  
    del records[findIndexInRecord(person)]

def editPerson(person):
    print('редактируем'+person) 

def searchBook():
    msg ="Выберите из списка"
    title = "Телефонная Книга"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        msgbox("Ваш выбор: {}".format(choice), "Survey Result")
        return
    
def searchBookRetrun():
    msg ="Выберите из списка"
    title = "Телефонная Книга"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return      
        return choice

def addBook():
    title = "Новая Запись"
    msg = "Заполните все поля"
    fieldNames = ["Фамилия", "Имя", "ОТчество", "Телефон"]
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
    msg ="Выберите из списка для удаления"
    title = "Телефонная Книга"
    getPeople(records)
    choices =  getPeople(records)   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        result = ccbox("Удаляем : {}".format(choice), "Будет удален")
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
    title = "Редактировать Запись"
    msg = "Заполните все поля"
    fieldNames = ["Фамилия", "Имя", "ОТчество", "Телефон"]
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
    msg ="Добро пожаловать в телефонную книгу !"
    choices = ["Искать","Добавить","Редактировать","Удалить","Выход"]
    reply = buttonbox(msg,  choices=choices)
    match reply:
        case "Искать":
            print('Искать')
            searchBook()
        case "Добавить":
            print('Добавить')
            addBook()
        case "Редактировать":
            print('Редактировать')
            editBook()
        case "Удалить":
            print('Удалить')
            deleteBook()
        case _:
            print('Выход')           
    return reply        

while 1:
   reply = mainWindow()
   if reply == 'Выход':  sys.exit(0)      



