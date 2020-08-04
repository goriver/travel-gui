# use travel;


# CREATE TABLE club (
# -- 	uid varchar(50) not null,
# 	club_name varchar(20) NOT NULL,
# 	club_info varchar(100) NOT NULL,
# 	manager_email varchar(50) NOT NULL,
# 	member_email varchar(50) NOT NULL,
# 	member_roll varchar(30) NOT NULL
# 	) 

# DESC club;
# ALTER TABLE club CONVERT TO CHARSET utf8;

# -- ALTER TABLE club 
# -- FOREIGN KEY (member_email);

# SELECT * from club;
# -- 
# -- 
# -- 
# -- DROP VIEW view_data ;
# -- DROP TABLE community ;
# -- 


# CREATE TABLE community (
# 	email varchar(30) PRIMARY KEY,
# 	password varchar(20) NOT NULL,
# 	nickname varchar(15) NOT NULL,
# 	phonenumber varchar(20) NOT NULL, #
# 	birthday DATE NOT NULL,
# 	address varchar(30) NOT NULL);

# ALTER TABLE community CONVERT TO CHARSET utf8;
# DESC community;
# -- 
# -- 

# SELECT * from community;


# SELECT * from club;

# -- 
# -- INSERT INTO community(email,password,nickname,phonenumber,birthday,address) 
# -- VALUES ("kkkk@g~", "1234", "GOGO","0101461646", 19970302, "서울" );
# -- 
# -- 
# -- 
# -- SELECT club_name 
# -- FROM community AS co join club AS cl
# -- on co.email = cl.member_email
# -- WHERE co.email ="kkkk@g~" ;
# -- -- WHERE co.club_name = "제주like i
# -- 
# -- 
# -- 
# -- SELECT club_name 
# -- FROM club 
# -- WHERE club_info LIKE '%제주%';
# -- 
# -- SELECT password FROM community WHERE email="kkkk@g~";



# CREATE VIEW views_data AS 
# SELECT * 
# FROM club AS cl inner join community AS co 
# ON  cl.member_email = co.email;

# select * from views_data ;

# -- drop table board ;

# CREATE TABLE board (
# 	id varchar(50) NOT NULL,
# 	title varchar(50) NOT NULL,
# 	content varchar(3000) NOT NULL,
# 	member_email varchar(30) NOT NULL,
# 	manager_email varchar(30) NOT NULL,
# 	club_name varchar(30) NOT NULL,
# 	PRIMARY KEY(id)
# 	);

# ALTER TABLE board CONVERT TO CHARSET utf8;
# DESC board;

# SELECT * from board;

# -- drop view board_view ;

# -- CREATE VIEW board_view AS 
# -- SELECT b.title, b.text,b.member_email,b.manager_email,b.club_name, b.date
# -- FROM board AS b INNER JOIN `club` AS cl
# -- ON  cl.club_name= "; 

# -- create view baoard_view as 
# -- select *
# -- from board as b inner join club as cl
# -- on b.club_name = cl.club_name; 
# -- 
# -- 
# -- SELECT * from club;
# -- SELECT * from board ;
# -- 
# -- SELECT title,text,member_email,date
# -- FROM board WHERE club_name = "강원도 감자 무봤나?"
# -- 
# -- DELETE FROM board WHERE id=<function uuid4 at 0x03672DA8>;                                                                                                                                                                                                                            ;
# -- SELECT * FROM club WHERE club_name="jejumany";

# -- SELECT * from baoard_view;


# create view board_view as 
# select  cl.member_roll, b.club_name, b.title,b.content, b.manager_email , b.member_email 
# from board as b inner join club as cl
# on b.club_name = cl.club_name;

# -- ALTER TABLE board_view CONVERT TO CHARSET utf8;
# DESC board_view;

# SELECT * from board_view;

