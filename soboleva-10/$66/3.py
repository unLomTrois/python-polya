"""
Соболева ПКС-1
Ввести адрес файла и «разобрать» его на части, разделенные знаком '/'. Каждую часть 
вывести в отдельной строке.
"""

text = input("введите адрес файла: ")
for part in text.split("/"):
    print(part)
