import MySQLdb

config = {
    'user': 'root',
    'passwd': '',
    'host': '127.0.0.1',
    'db': 'noe'
}

conn = MySQLdb.connect(**config)

cursor = conn.cursor()

query = "SELECT * FROM MGRCP WHERE (NOT(LEFT(ERN, 1) BETWEEN '1' AND '5' OR LENGTH(ERN) = 9)) AND NOT (ERN = '0037793301' AND EC = 'POM0177');"
cursor.execute(query)

result = cursor.fetchall()

cursor.close()
conn.close()


html_content = """
<html>
<head>
    <title>Script mayssa</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>id</th>
            <th>msc</th>
            <th>ATYPE</th>
            <th>AREA</th>
            <th>EC</th>
            <th>ERN</th>
            <th>ERIND</th>
            <th>CTYPE</th>
            <th>ACET</th>
            <th>dt_create</th>
        </tr>
"""

for row in result:
    html_content += "<tr>"
    for value in row:
        html_content += "<td>{}</td>".format(value)
    html_content += "</tr>"

html_content += """
    </table>
</body>
</html>
"""

with open('resultat.html', 'w') as f:
    f.write(html_content)



