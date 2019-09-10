import pymysql

connect = pymysql.connect(
            host='129.204.212.126',
            port=3306,
            user='root',
            password='520lzj',
            db='doubiyang',
            charset='utf8'
        )

source = '打发十分'
film_name = '幅度萨芬'
title = '乐'
print(title)
real_url = 'https://www.baidu.com'
conn = connect.cursor()
conn.execute("insert into film values('%s','%s','%s','%s')" % (source, film_name, title, real_url))
connect.commit()
conn.close()
connect.close()


