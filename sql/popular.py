import csv
import pymysql


insert = ' INSERT INTO titanic.passengers(p_class, p_name, p_sex, p_age, p_sib_sp, p_parch, p_ticket, p_fare, p_cabin, embarked) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '

def oneline_csv(csv_path):
  with open(csv_path, encoding='utf-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
      line_correct = []

      for index, item in enumerate(line):
          if item == "":  # Se estiver vazio, transforma em None
              line_correct.append(None)
          elif index == 2 or index == 7: 
            # passa para a proxima iteração se o item for o nome
            line_correct.append(item)
            continue
          else:
              try:
                  
                  # Converte para int ou float, se possível
                  if "." in item:  # Se tiver ponto, tenta converter para float
                      item = float(item)
                  else:
                      item = int(item)
              except ValueError:
                  pass
              
              line_correct.append(item)

      yield line_correct

# Conectar ao banco
connection = pymysql.connect(
    host="127.0.0.1",  # ou IP do servidor
    user="root", # seu usuario no mysql
    password="!am2007", # a senha do usuario
    database="titanic", # o banco de dados, obs: crie ele antes rodando o aquivo commands.sql
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor  # Retorna os resultados como dicionários
)



for index, line in  enumerate(oneline_csv('./datas.csv')):
  line.pop(0)
  
  # usa a conexão para execultar querys
  with connection.cursor() as cursor:
    cursor.execute(insert, line)
    connection.commit()
    print(f'Linha {index} inserida!!!')
  