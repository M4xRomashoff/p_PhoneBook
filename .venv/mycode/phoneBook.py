from easygui import * 
import sys
import mysql.connector
from mysql.connector import connect, Error

dbName = 'phonebook.phonenumbers'


def addRecordDB(values):

    insert_query =  """
    INSERT INTO """+ dbName + """ (firstName, lastName, middleName, phone)
    VALUES   (" """+ values[0]+""" ", " """+ values[1] + """ ", " """ + values[2] + """ " , " """ +values [3] + """ ")
    """

    try:
        with connect(
            host="localhost",
            user="root",
            password="Twenty22!",
        ) as connection:                   
            with connection.cursor() as cursor:
                cursor.execute(insert_query)
                connection.commit()
    except Error as e:
        print(e)

def getPeopleDB():
    people = []
    query =  """
    SELECT * FROM """+ dbName + """;"""   
    try:
        with connect(
            host="localhost",
            user="root",
            password="Twenty22!",
        ) as connection:                 
            with connection.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.fetchall()
            print(result) 
            for person in result:
                people.append(person[1]+' '+person[2]+' '+person[3]+' '+person[4])  
            print(people) 
            return people    
    except Error as e:
        print(e)

    return people

def deleteBookDB():
    msg ="???????? ?? ?????? ??? ????????"
    title = "?????????? ?????"
    choices = getPeopleDB()  
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        result = ccbox("??????? : {}".format(choice), "????? ??????")
        if(result): 

            deletePersonDB(choice) 
            return
        else:  
            print('cancelled',choice, result)
            return

def deletePersonDB(person):   


    print("deletePersonDB(person):", person)
   
    query0 =  """
    SET SQL_SAFE_UPDATES = 0;"""

    query1 =  """
  
    DELETE FROM """+ dbName +\
    """ WHERE firstName = '"""+ person.split(' ')[0] +\
    """' AND lastName = '"""  + person.split(' ')[1] + \
    """' AND middleName = '"""+ person.split(' ')[2] + """';"""

    query2 =  """   
    SET SQL_SAFE_UPDATES = 1;"""


    print(query1)
    query1.replace("'", '"')

    try:
        with connect(
            host="localhost",
            user="root",
            password="Twenty22!",
        ) as connection:                 
            with connection.cursor() as cursor:
                 cursor.execute(query0)
                 cursor.execute(query1)
                 connection.commit()
                 cursor.execute(query2)
               
                #  result = cursor.fetchall()          
    except Error as e:
        print(e)

    return
    
def editRecordDB(old_items, newItems):

    print(old_items)
    print(newItems)

 
    query0 =  """
    SET SQL_SAFE_UPDATES = 0;"""

    query1 =  """
  
    UPDATE """+ dbName +\
    """ SET lastName = " """+ newItems[0] +\
    """ " , firstName = " """+ newItems[1] +\
    """ " , middleName = " """+ newItems[2] +\
    """ " , phone = " """+ newItems[3] +\
    """ " WHERE firstName = " """+ old_items[0] +\
    """ " AND lastName = " """  + old_items[1] + \
    """ " AND middleName = " """+ old_items[2] + """ ";"""

    query2 =  """   
    SET SQL_SAFE_UPDATES = 1;"""


    print(query1)

    try:
        with connect(
            host="localhost",
            user="root",
            password="Twenty22!",
        ) as connection:                 
            with connection.cursor() as cursor:
                #  cursor.execute(query0)
                 cursor.execute(query1)
                 connection.commit()
                #  cursor.execute(query2)
               
                #  result = cursor.fetchall()          
    except Error as e:
        print(e)

    return



# records = [
#     dict([('LastName', 'Иванов'),    ('FirstName', 'Иван'),     ('MiddleName', "Иванович"),    ('phone','(222)-111-3434')]),
#     dict([('LastName', 'Петров'),    ('FirstName', 'Петр'),     ('MiddleName', "Иванович"),    ('phone','(222)-222-3434')]),
#     dict([('LastName', 'Сидоров'),   ('FirstName', 'Спиридон'), ('MiddleName', "Иванович"),    ('phone','(222)-333-3434')]),
#     dict([('LastName', 'Степанова'), ('FirstName', 'Светлана'), ('MiddleName', "Ивановна"),    ('phone','(222)-444-3434')]),
#     dict([('LastName', 'Живенькая'), ('FirstName', 'Ольга'),    ('MiddleName', "Григорьевна"), ('phone','(222)-555-3434')]),
# ]

# def findIndexInRecord(person):
#     index = 0
#     for item in records:
#         print(item['LastName'],'  ', person.split(' ')[0])

#         if (item['LastName'] == person.split(' ')[0] and
#             item['FirstName'] == person.split(' ')[1] and
#             item['MiddleName'] == person.split(' ')[2] and
#             item['phone'] == person.split(' ')[3]
#             ): return index
#         index +=1
#     return -1   
 
# def addRecord(items):
#     records.append(dict([('LastName', items[0]),    
#                          ('FirstName', items[1]),     
#                          ('MiddleName',items[2]),    
#                          ('phone',items[3])]))

# def editRecord(old_items, newItems):

#     recIndex = findIndexInRecord(old_items)
#     records[recIndex]['LastName']=newItems[0]
#     records[recIndex]['FirstName']=newItems[1]
#     records[recIndex]['MiddleName']=newItems[2]
#     records[recIndex]['phone']=newItems[3]
    
    

def getPeople(listOfRecord):
    people = []
    for person in listOfRecord:       
        people.append(person['LastName']+' '+person['FirstName']+' '+person['MiddleName']+' '+person['phone'])
    return people


def editPerson(person):
    print('редактируем'+person) 

def searchBook():
    msg ="Выберите из списка"
    title = "Телефонная Книга"
   
    choices =  getPeopleDB()   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        msgbox("Ваш выбор: {}".format(choice), "Survey Result")
        return
    
def searchBookRetrun():
    msg ="Выберите из списка"
    title = "Телефонная Книга"
    choices =  getPeopleDB() 
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
   
    addRecordDB(fieldValues)  
    return 

def deleteBook():
    msg ="Выберите из списка для удаления"
    title = "Телефонная Книга"
    choices =  getPeopleDB()   
    while 1:
        choice = choicebox(msg, title, choices)
        if choice is None:
           return
        result = ccbox("Удаляем : {}".format(choice), "Будет удален")
        if(result): 
            deletePersonDB(choice) 
            return
        else:  
            print('cancelled',choice, result)
            return

def editBook():
    person = searchBookRetrun()
    print(person)
    person = " ".join(person.split())
    personItems = person.split(' ')
    print( personItems)
    title = "Редактировать Запись"
    msg = "Заполните все поля"
    fieldNames = ["Фамилия", "Имя", "Отчество", "Телефон"]   
    fieldValues = multenterbox(msg, title, fieldNames, personItems)  
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
    editRecordDB(personItems, fieldValues)  
    return 


def mainWindow():
    msg ="Добро пожаловать в телефонную книгу !"
    choices = ["Искать","Добавить","Редактировать","Удалить","Выход"]
    reply = buttonbox(msg,  choices=choices)
    match reply:
        case "Искать":          
            searchBook()
        case "Добавить":         
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
