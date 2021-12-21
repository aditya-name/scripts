import PySimpleGUI as sg
# ---------- returning query to gui
def guiReturn(para0):
    layout = [
            [sg.Text(para0)],
            [sg.Ok()]
            ]

    window = sg.Window('Database Query result').Layout(layout)
    button, values = window.Read()

    window.close()

# ---------- working extra on delivered results ------
# print ( results_list)
# for i in results_list:
#     for j in i:
#         if PRJ_TYP_input == j:
#             print("project typ number is:", i[0])







