
import prozeduren
# ---------- gui user interaction   ------
import PySimpleGUI as sg
layout = [
            [sg.Text(' For values not known / not relevant, enter: - \n \n For values to be queried, enter: ? \n \n')],
            [sg.Text('Kapitel', size=(15, 1)), sg.InputText('-')],
            [sg.Text('KapitelÜberschrift', size=(15, 1)), sg.InputText('-')],
            [sg.Text('TYP', size=(15, 1)), sg.InputText('-')],
            [sg.Text('IQP_TYP', size=(15, 1)), sg.InputText('-')],
            [sg.Text('Kunde', size=(15, 1)), sg.InputText('-')],
            [sg.Text('PRJ_TYP', size=(15, 1)), sg.InputText('-')],
            [sg.Text('Baustein', size=(15, 1)), sg.InputText('-')],
            [sg.Submit(), sg.Cancel()]
            ]

window = sg.Window('Database Query').Layout(layout)
button, values = window.Read()

print(button, values)

window.close()

# ---- creating basic python database elements ----
from sqlalchemy import create_engine, Table, Column, String, MetaData, select
engine = create_engine('postgresql+psycopg2://postgres:Sharing@123@localhost:5432/movedb')
metadata = MetaData()

# ----------- loading tables for pythonic way queries  -----------
tblAngebotsListe = Table('tblAngebotsListe', metadata, autoload=True, autoload_with=engine)
tblPRJ_TYP = Table('tblPRJ_TYP', metadata, autoload=True, autoload_with=engine)

metadata.create_all(engine)

# ---------- connecting to database ------
connection = engine.connect()

#----- creating queries in sql way  ---------
# select Baustein from tblBaustein where IQP_TYP = Agil and Typ = Content and Kapitel = 3.4 ( 7  in database )
# s_sql = ''' select "Baustein" from public."tblBaustein" where "Typ" = 'Content' and "IQP_TYP" = 'Agil' and "Kapitel" = '7' '''
global s_sql
queryValidFlag = 0

def queryBaustein():
    s_sql = ''' select "{0}" from public."newTable" where "Typ" = '{1}' and "IQP_TYP" = '{2}' and "KapitelNr" = '{3}' '''.format(Baustein_input, TYP_input, IQP_TYP_input, Kapitel_input)
    queryValidFlag = 1

# ---------- assigning from gui to code   ------

Kapitel_input = values[0]
if Kapitel_input == "?":
    Kapitel_input = "Kapitel"

KapitelÜberschrift_input = values[1]
if KapitelÜberschrift_input == "?":
    KapitelÜberschrift_input = "KapitelÜberschrift"


TYP_input = values[2]
if TYP_input == "?":
    TYP_input = "TYP"


IQP_TYP_input = values[3]
if IQP_TYP_input == "?":
    IQP_TYP_input = "IQP_TYP"


Kunde_input = values[4]
if Kunde_input == "?":
    Kunde_input = "Kunde"


PRJ_TYP_input = values[5]
if PRJ_TYP_input == "?":
    PRJ_TYP_input = "PRJ_TYP"


Baustein_input = values[6]
if Baustein_input == "?":
    Baustein_input = "Baustein"
    queryBaustein()
# ----- creating queries in pythonic way  ---------
s_python = select([tblPRJ_TYP])



# ---- how queries look in sql -----
# print(str(s_sql))

# ----- executing queries on database ----
# rp = connection.execute(s_python)

if queryValidFlag == 0:
    prozeduren.guiReturn("nothing to show")
else:
    rp = connection.execute(s_sql)
    prozeduren.guiReturn(results_list[0][0])  # for baustein single statement



#---- fetiching results -----
results_list = rp.fetchall()


# ---------- returning query to gui
# def guiReturn(para0):
#     layout = [
#             [sg.Text(para0)],
#             [sg.Ok()]
#             ]
#
#     window = sg.Window('Database Query result').Layout(layout)
#     button, values = window.Read()
#
#     window.close()

# ---------- working extra on delivered results ------
# print ( results_list)
# for i in results_list:
#     for j in i:
#         if PRJ_TYP_input == j:
#             print("project typ number is:", i[0])







