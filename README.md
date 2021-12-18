https://pysparktutorials.wordpress.com/string-functions/

http://h2database.com/html/functions.html

https://stevestedman.com/2015/05/tsql-join-types-poster-version-4-1/

https://www.javatpoint.com/mysql-tutorial

https://github.com/spark-examples/pyspark-examples

https://towardsdatascience.com/scalable-efficient-big-data-analytics-machine-learning-pipeline-architecture-on-cloud-4d59efc092b5

https://colab.research.google.com/drive/1R_-d7l0gZSdaNbe-ImYHVRtAWoIeEbnv?authuser=1#scrollTo=d3KnhXzwASUQ

https://docs.microsoft.com/en-us/azure/data-factory/lab-data-flow-data-share

https://ajaytech.co/python-challenges/
# This is interview importent question as duing live intevriew

                                    <<<<<<<<<< All the importent question >>>>>>>>>>>>>  

1-How to swap the value?
   
   <<<<a=10 b=20     a,b=b,a>>>>

2-Find the occurance in in given string ?

3-Find the second largest value given in list?

4-What is the difference in between the list and tuple ?

5-Find the occurance in the bethout using count and counter and regex ?

6-What is the list, dict string,tuple and it operation?

7-What is largest value in the list?

8-What is class and method and instance ?

9-What is the inheritance and polymorphisam?

10-Give one example 

11-What is the palaindrom ?


##HOW  TO CONNECT DATA BASE WITH PYTHON

pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="yusername",
      passwd="password",
      database="database_name"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")    

mycursor.execute("SHOW TABLES")

mycursor.execute("INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')")  

mydb.commit() # Use this command after insert, update, delete commands


