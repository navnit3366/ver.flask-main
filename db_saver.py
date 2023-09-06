#db관련
import sqlite3

def save_db():
    #db저장
    conn = sqlite3.connect("datebase.db")   # 저장할 DB파일 이름
    curs = conn.cursor()
    try:
        curs.execute("CREATE TABLE jobs (enterprise TEXT, enterprise_num TEXT, sector TEXT, employee TEXT, sales TEXT, address TEXT, weblink TEXT, introduce TEXT, work TEXT)")  #9
    except Exception as e:
        print('db error:', e)
    
    reader = open('jobs.csv', 'rt', encoding='utf-8-sig') # CSV파일 읽기모드로 열기
    # reader=csv.reader(open('jobs.csv', 'r'), delimiter=',', quotechar='"')
    for row in reader:
        a=row.split("$")
        # to_db = [index, (a[1]), (a[2]), (a[3]), (a[4]), (a[5]), (a[6]), (a[7]), (a[8]), (a[9]))]
        if len(a)==9:
            curs.execute("INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?,?)", (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]))
    # conn.commit()  #커밋 (쌓아둔 명령 실행)
    # conn.close()
    return conn

def select_all():
    #db결과 반환
    ret = []
    try:
        db = save_db()
        c = db.cursor()
        c.execute('SELECT * FROM jobs')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

# db keyword검색
def search_keyword(input):
    list2 = select_all()
    indexs=[]
    keyword = input
    for column in list2:
        # print(list(column))
        for arr in column:
            if keyword in arr:
                indexs.append(list(column))
    return indexs

    # indexs.append(list(s for s in column if keyword in s))
    # indexs.append(i for i in range(len(column)) if keyword in column[i])
# flutten(indexs)
# new_indexs = [v for v in indexs if v] #검색결과들만 가져와짐
# 검색결과와 같은 인덱스의 배열들이 가져와져야...