# Django_MySql_CRUD_APP

<p align = "center">
  
![table](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/fc2c6c14-baf9-407b-9e74-80cca24a2164) 

</p>


# Objective
Use Django framework and MySQL to create a CRUD (Create, Read, Update, Delete) APP.

# What will be created?
An app that will be able to create an employee object and store the
employee details into a database (MySQL Database).
The employee details will be able to be modified 
and the employee will be able to be deleted.

<p align = "center">
 
<h2>Form where employee details can be entered</h2>
<h3>Click Submit to create employee object in the database</h3>

 ![details](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/3ce993b6-294f-4c9a-839b-46331a635472)
 </p>

<p>
  <h3>Employee object has been created.</h3>
  
  ![empobj](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/9ddeba10-32cf-483a-8721-b39ff71e65d1)
</p>

<p> 
  <h2>Employee object is also stored in MySQL database. Keep in mind that MySQL databse is using the names assigned in the models.py file</h2>

  <h2>Names assigned in in the models.py</h2>
  
  ![sqlnames](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/43edd868-3abc-412b-8f3f-9329301ea6ab)

  <h3>Employee stored in MySQL database</h3>
  
  ![mysqldata](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/422241a7-35ad-495e-837e-73e4c4eb0897) 
</p>
 
  




# Create a database in MySQL  
Two ways to create a database: (For this project the database name will be <b>djangomysqlcrudapp</b>)
<p>
1) Create a database using MySQL Workbench by clicking on the circled logo.

  ![database2](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/5624871b-da29-4590-ac75-6a4ea7e7dc51)

</p>
<p>
2) Create a database using MySQL Command Line Client. Type <b>create database djangomysqlcrudapp;</b>
  
![createDatabase](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/68daac99-d015-4c89-9d15-ca494b73fad0)
</p>

# Set Up MySQL database in Django   
<p>
  Change the Django default database (sqlite3) to MySQL databse in the <b>settings.py</b> file.
  
  ![database](https://github.com/GabrielMacJr/Django_MySql_CRUD_APP/assets/110753469/53a51c9a-84b5-4559-917e-e6a001efef4a)

</p>


