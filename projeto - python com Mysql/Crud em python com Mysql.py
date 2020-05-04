import MySQLdb

host = "localhost"
user = "app_pythonMy"
password = "403751"
db = "escola_aluno"
port = 3306


con = MySQLdb.connect(host, user, password, db, port)

# gerar dados em modo dicionario
#MySQLdb.cursors.DictCursor
c = con.cursor()

def select (fields, tables, where = None):
    global c

    query = " SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where
    c.execute(query)
    return c.fetchall()
"""
result = select("nome,cpf","alunos")
print(result)
"""
def insert(values, table, fields = None):
    global c, con

    query = " INSERT " + table
    if(fields):
        query = query + "("+ fields + ")"
    query = query + " VALUES " + "," .join(["(" + v + ")" for v in values])
    c.execute(query)
    con.commit()
   
"""
values = ["DEFAULT,'Fulano', '2001-01-01','Rua Raimundo Clovis 15','Quixada', 'CE', '65189345621'"]
insert(values,"alunos")
print(select("*","alunos"))
"""
def update(sets, table, where = None):
    global c, con

    query = " UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'"  for field, value in sets.items()])
    if(where):
        query = query + " WHERE " + where
    c.execute(query)
    con.commit()
#date({"nome": "Karol"},"alunos","id_aluno = 6")


def delete(table, where):

    query = " DELETE FROM " + table + " WHERE " + where
    c.execute(query)
    con.commit()

delete("alunos","id_aluno = 6")
print(select("*","alunos"))
