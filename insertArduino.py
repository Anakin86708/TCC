import mysql.connector
#python3-mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="estacao"
)
mycursor = mydb.cursor()


pagina = "dados.html"

with open(pagina, "r") as entrada:
    string = entrada.readline()
    umidadeDHTs, temperaturaDHTs, temperaturaBMPs, pressaoBMPs, alturaBMPs= string.split(";")
    umidadeDHT = float(umidadeDHTs)
    temperaturaDHT = float(temperaturaDHTs)
    temperaturaBMP = float(temperaturaBMPs)
    pressaoBMP = float(pressaoBMPs)
    alturaBMP = float(alturaBMPs)


sql = "INSERT INTO dados (umidadeDHT, temperaturaDHT, temperaturaBMP, pressaoBMP, alturaBMP) VALUES (%s, %s, %s, %s, %s)"
val = (umidadeDHT, temperaturaDHT, temperaturaBMP, pressaoBMP, alturaBMP)
mycursor.execute(sql, val)


sql = "UPDATE dados SET data = NOW() WHERE id = LAST_INSERT_ID();"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")