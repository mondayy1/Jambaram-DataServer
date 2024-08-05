import psycopg2
import json

with open('secrets.json') as f:
    secrets = json.loads(f.read())

db = psycopg2.connect(host=secrets['DB']['host'],
                      dbname=secrets['DB']['dbname'],
                      user=secrets['DB']['user'],
                      password=secrets['DB']['password'],
                      port=secrets['DB']['port'])
cursor = db.cursor()

def db_insert_comb(comb, win, score):
    tables = ['alltime_best_comb_win', 'alltime_best_comb_score', 'today_best_comb_win', 'today_best_comb_score']

    for i, table in enumerate(tables):
        cursor.execute(f'SELECT * FROM {table}')
        row = cursor.fetchall()
        col = win if i % 2 == 0 else score

        if len(row) == 0: #empty
            cursor.execute(f'INSERT INTO {table} VALUES (%s, {col})', (comb,))
        else: #exsits
            value = row[0][1]
            if col > value: #update
                cursor.execute(f'DELETE FROM {table} WHERE champions = %s', (row[0][0],))
                cursor.execute(f'INSERT INTO {table} VALUES (%s, {col})', (comb,))

        db.commit()

def db_get_comb(type, time):
    table = time + '_best_comb_' + type

    cursor.execute(f'SELECT * FROM {table};')
    row = cursor.fetchall()

    if len(row) == 0:
        return [-1], 0
    else:
        return row[0][0], row[0][1]