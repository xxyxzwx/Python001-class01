import pandas as pd
#1. SELECT * FROM data;
print(data)

#2. SELECT * FROM data LIMIT 10;
#表头算0行，对应mysql里建表的字段名
print(data[0:11])
 
#3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])
 
#4. SELECT COUNT(id) FROM data;
print(data['id'].count())
 
#5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[( data['id']<1000 ) & ( df['age']>30 )])
 
#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(table1.groupby('id').agg({'order_id':'count'}))
 
#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(table1, table2, on = 'id'))
 
#8. SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([table1,table2]).drop_duplicates())
 
#9. DELETE FROM table1 WHERE id=10;
tabel1.drop(10)
 
#10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop('column_name', axis=1)