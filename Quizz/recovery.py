# import csv
# import os
#
#
# class File:
#
#     def __init__(self, path, name, files, extension):
#         self.path = path
#         self.name = name
#         self.files = files
#         self.extension = extension
#         self.headers = []
#         self.data = []
#         self.flag = False
#
#     def join_csv(self):
#         try:
#             for self.file in self.files:
#                 file_handler = open(f"{self.file}", 'r')
#                 self.data.append(file_handler)
#                 self.headers.append(file_handler.readline().strip())
#
#             with open(self.name + self.extension, 'w') as file_handler:
#                 headers = ",".join(self.headers)
#                 file_handler.write(f"{headers}\n")
#
#                 while not self.flag:
#                     fila = []
#                     for handle in self.data:
#                         dato = handle.readline()
#                         if dato:
#                             print(dato)
#                             fila.append(dato.strip())
#                         else:
#                             self.flag = True
#                             print(f" El Archivo {self.name}{self.extension} se ha creado con exito")
#
#                             break
#                     if not self.flag:
#                         result = ",".join(fila)
#                         file_handler.write(f"{result}\n")
#
#         except FileNotFoundError:
#             print("No encontro los archivos")

# ['Rank', 'First Name', 'Last Name', 'Attempt #', 'Accuracy', 'Score'],
import csv

list = [["RN", "Name", "GRADES"],
        [1, 'ABC', 'A'],
        [2, 'TUV', 'B'],
        [3, 'XYZ', 'C']]
with open('studentgrades.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
    writer.writerows(list)