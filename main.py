import sqlite3

con = sqlite3.connect('KJF.sqlite')
cur = con.cursor()
#cur.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name")
#"SELECT name FROM testament WHERE name='Antigo Testamento'"
busca = str(input('Digite o Livro'))
for row in cur.execute(f"SELECT text FROM verse WHERE book_id={busca}"):
    text = row[0]
    print(row)
con.close()
"""
('table', 'book', 'book', 2, 'CREATE TABLE "book" (\n\t"id"\tINTEGER,\n\t"book_reference_id"\tINTEGER,\n\t"testament_reference_id"\tINTEGER,\n\t"name"\tTEXT\n)')
('table', 'metadata', 'metadata', 3, 'CREATE TABLE "metadata" (\n\t"key"\tTEXT,\n\t"value"\tTEXT\n)')
('table', 'testament', 'testament', 4, 'CREATE TABLE "testament" (\n\t"id"\tINTEGER,\n\t"name"\tTEXT\n)')
('table', 'verse', 'verse', 5, 'CREATE TABLE "verse" (\n\t"id"\tINTEGER,\n\t"book_id"\tINTEGER,\n\t"chapter"\tINTEGER,\n\t"verse"\tINTEGER,\n\t"text"\tTEXT\n)')
(31102, 66, 22, 21, 'A graça de nosso Senhor Jesus Cristo esteja com todos vós. Amém.')
"""