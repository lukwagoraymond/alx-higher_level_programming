# 0x0E. SQL - More queries 

## Resources:books:
Read or watch:
* [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
* [MySQL constraints](https://zetcode.com/mysql/constraints/)
* [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
* [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A)
* [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg)
* [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
* [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
* [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
* [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
* [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
* [SQL Style Guide](https://www.sqlstyle.guide)
* [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
---
Extra resources around relational database model design:
* [Design](https://www.guru99.com/database-design.html)
* [Normalization](https://www.guru99.com/database-normalization.html)
* [ER Modeling](https://www.guru99.com/er-modeling.html)
---
---
## Learning Objectives:bulb:
What you should learn from this project:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

---

### [0. My privileges!](./0-privileges.sql)
* Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).


### [1. Root user](./1-create_user.sql)
* Write a script that creates the MySQL server user user_0d_1. 


### [2. Read user](./2-create_read_user.sql)
* Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 


### [3. Always a name](./3-force_name.sql)
* Write a script that creates the table force_name on your MySQL server.


### [4. ID can't be null](./4-never_empty.sql)
* Write a script that creates the table id_not_null on your MySQL server.


### [5. Unique ID](./5-unique_id.sql)
* Write a script that creates the table unique_id on your MySQL server.


### [6. States table](./6-states.sql)
* Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.


### [7. Cities table](./7-cities.sql)
* Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.


### [8. Cities of California](./8-cities_of_california_subquery.sql)
* Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.


### [9. Cities by States](./9-cities_by_state_join.sql)
* Write a script that lists all cities contained in the database hbtn_0d_usa.


### [10. Genre ID by show](./10-genre_id_by_show.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download


### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)
* Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)


### [12. No genre](./12-no_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)


### [13. Number of shows by genre](./13-count_shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)


### [14. My genres](./14-my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)


### [15. Only Comedy](./15-comedy_only.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)


### [16. List shows and genres](./16-shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)


### [17. Not my genre](./100-not_my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)


### [18. No Comedy tonight!](./101-not_a_comedy.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)


### [19. Rotten tomatoes](./102-rating_shows.sql)
* Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download


### [20. Best genre](./103-rating_genres.sql)
* Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)


---

## Author
* **Raymond Lukwago** - [lukwago](https://github.com/lukwagoraymond)
