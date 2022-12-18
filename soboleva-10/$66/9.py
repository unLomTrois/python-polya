"""
Соболева ПКС-1
Напишите функцию, которая определяет, сколько раз входит в символьную строку заданное слово.
"""

text = input("введите строку: ")
substr = input("введите подстроку: ")
# count, i = 0, text.find(substr)


def findsubstr(text: str, substr):
    return text.count(substr)


print(findsubstr(text, substr))
