from Quizz import File
import os

ruta = os.path.dirname(os.path.realpath(__file__))
# archivos = ["catalog.csv", "complete.csv"]
archivos = ["quiz_1.csv", "quiz_2.csv", "quiz_3.csv", "quiz_4.csv",'quiz_5.csv']
file = File.File(ruta, 'nico', archivos, ".csv")
file.join_csv()

