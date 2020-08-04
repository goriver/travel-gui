import pymysql.cursors
import random

class MembershipStore:
    connection = None
  
    #db연결
    def __init__(self):
        MembershipStore.connection = pymysql.connect(host='localhost',
                            port= 3306, #으로 함
                            user='aiadmin',
                            password='password',
                            db='travel',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)
    #db 연결 종료
    def close(self):
        MembershipStore.connection.close()

    # 커뮤니티 가입시 db 추가
    def insert_community(self,community_entity):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql = ("INSERT INTO `community` (`email`, `password`, `nickname`, `phonenumber`, `birthday`, `address`) \
                    VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (community_entity.email, community_entity.password, community_entity.nickname, community_entity.phonenumber, community_entity.birthday, community_entity.address))
                MembershipStore.connection.commit()
        finally:
            pass

    # club 생성 및 가입시 db 추가
    def insert_club(self, club_entity):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql = ("INSERT INTO `club` (`club_name`, `club_info`, `manager_email`,`member_email`, `member_roll`) \
                    VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (club_entity.club_name, club_entity.club_info, club_entity.manager_email,club_entity.member_email, club_entity.member_roll))
                MembershipStore.connection.commit()
        finally:
            pass

# =====================================================================
# ==========관리자 view 만들기 =========================================

    # view 만들기 # 한꺼번에 다 가지고 와서 돌려야한다. 
    # select all했을 때도 이걸로 모든 데이터 가지고 와서 dic형태로 나눌 예정이다. 
    # cursor가 2개 이상일 경우 error가 발생
    # club에 가입한 사람의 database는 이것으로 값을 처리한다.
    # view에도 update할 수 있으나, 여기서 할 경우 값을 다시 나눠서 갖는 것이 힘들다. 따라서 update의 경우 gui를 register 함수와 비슷한 곳에 위치시켜 해결한다.
    
    # 관리자의 view페이지를 보여준다.
    # views_data로 원하는 정보를 select하여 보여주는 역할을 수행할 예정이다.

    # already_view는 이미 db에서 만들어 놓은 뷰이다
    # 다시 생성할 경우 error가 발생하기 때문에 아래의 방법으로 뷰를 생성하고 이후 여러곳에 
    # select 구문을 활용하여 원하는 정보를 가져올 예정이다.

    # inner join은 겹치는 정보만 가져온다
    # full outer join은 겹치지 않는 정보도 가져오고 해당 컬럼에 정보가 없을 경우 null값으로 처리한다.
    # 여기서는 클럽에 가입하지 않은 사람의 경우 클럽장이 커뮤니티 사람의 정보를 조회하면 안된다.
    # 따라서 inner join으로 처리한다.
    # ★ 클럽명에 따라서 변경하기
# =====================================================================
    def already_view(self):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql =("CREATE VIEW `views_data` AS \
                        SELECT * \
                        FROM `club` AS cl inner join `community` AS co \
                        ON  cl.`member_email`= co.`email` ")
                cursor.execute(sql)
        finally:
            pass

    def view(self,club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT `member_email`, `member_roll`, `phonenumber`,`birthday`, `address` \
                     FROM `views_data` WHERE `club_name` = %s")
                cursor.execute(sql, (club_name ))
                result = cursor.fetchall() # 각 
                # CommunityStore.connection.commit()
                return result
        finally:
            pass

    # 클럽명을 입력받아서 각 클럽에 소속된 회원 정보 출력하기
    # INNER JOIN으로 가져옴
    def view_club(self):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql =("SELECT * \
                    FROM `club` AS cl join `community` AS co \
                    ON co.`email` = cl.`member_email`")
                # 이 경우 출력값은 각 클럽이 가지고 있는 MEMBEREMAIL을 바탕으로
                # MEMBER들의 정보를 가져온다
                # 이것으로 전화번호 열람할 수 있다.
                cursor.execute(sql)
                result = cursor.fetchall() # 각
                return result
        finally:
            pass
    # 이메일을 받아서 해당 클럽에 가입한 이메일인지 확인
    # 해당 클럽에 이메일이 있다면, club_name을 반환한다.
    # 뷰가 아닌데 헷갈려서 변수명을 잘못줬다. 시간 있을 때 고치기
    def view_club_by_e(self, email):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql =(" SELECT `club_name` \
                        FROM  `club` as cl JOIN `community` AS co\
                        ON  cl.`member_email`= co.`email`\
                        WHERE cl.`member_email` =%s")
                cursor.execute(sql, email)
                result = cursor.fetchall() # 각
                # print(result)
                return result
        finally:
            pass


    # 커뮤니티 회원 수정
    def update_community(self, email, nickname, phonenumber):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql = ("UPDATE `community` SET  `nickname`=%s, `phonenumber`=%s WHERE `email`=%s")
                cursor.execute(sql, (nickname, phonenumber, email))
                # travel_entity에는 모든 데이터를 받아오되, 원하는 것만 뽑아오기
                MembershipStore.connection.commit()
        finally:
            pass
    
    # 클럽 정보 수정
    # (`club_name`, `club_info`, `manager_email`,`member_email`, `member_roll`) \
    def update_club(self, club_entity):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("UPDATE `club` SET  `club_name`=%s, `club_info`=%s, `member_roll`=%s WHERE `member_email`=%s")
                cursor.execute(sql, (club_entity.club_name, club_entity.club_info, club_entity.member_roll, club_entity.member_email))
                MembershipStore.connection.commit()
        finally:
            pass
    
    # 커뮤니티 전체 리스트
    def select_all_community(self):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT * FROM `community`")
                cursor.execute(sql)
                result = cursor.fetchall() # select한 값은 patch로 불러올 수 있다
        finally:
            pass
        return result
        
    # 커뮤니티 email에  따른 pw 조회
    def select_pw(self, email):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT `password` FROM `community` WHERE `email`=%s")
                cursor.execute(sql,email)
                result = cursor.fetchall() # select한 값은 patch로 불러올 수 있다.
        finally:
            pass
        return result

    # 클럽 전체 리스트(회원은 조회 x )
    # 검색용 list 뿌릴 목적으로 작성함
    def select_all_club(self):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql =( "SELECT DISTINCT `club_name`,`club_info`,`manager_email` FROM `club`")
                cursor.execute(sql)
                result = cursor.fetchall() # select한 값은 patch로 불러올 수 있다.  
        finally:
            pass
        return result

    # primary 값(email)으로 데이터 검색하기
    def select_by_email(self, email):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = "SELECT * FROM `community` WHERE `email`=%s"
                cursor.execute(sql, email)
                result = cursor.fetchall() # select한 값은 patch로 불러올 수 있다.
                print(result)
        finally:
            pass
        return result

    
    # 같은 사람이 중복하여 club에 들어오는 것을 방지하기 위하여도 이용됨
    def select_by_club(self,club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql ="SELECT * FROM `club` WHERE `club_name` =%s"
                cursor.execute(sql, club_name)
                result = cursor.fetchall() # select한 값은 patch로 불러올 수 있다.
        finally:
            pass
        return result

    # 커뮤니티 탈퇴
    def delete_community(self,email):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("DELETE FROM `community` WHERE `email`=%s")
                cursor.execute(sql, (email))
                MembershipStore.connection.commit()
        finally:
            pass

    # 클럽 삭제
    def delete_by_email(self,manager_email):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("DELETE FROM `club` WHERE `manager_email`=%s")
                cursor.execute(sql, (manager_email))
                # AIStore.connection.commit() # insert update delete만 commit 함
                MembershipStore.connection.commit()
        finally:
            pass

    # 클럽 내 info 로 검색하기
    def select_by_info(self, club_info):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT `club_name` FROM `club` WHERE `club_info` LIKE %s")
                cursor.execute(sql, ('%{0}%'.format(club_info)))
                # AIStore.connection.commit() # insert update delete만 commit 함
                result = cursor.fetchall()
        finally:
            pass
        return result
# =============================================================================================================
# 1. 클럽명대로 게시글을 불러오는 view 생성 후 tree만들기
#       INNER JOIN으로 
# 2. 전체 게시글을 insert하는 table에 글 작성시 내용 추가하기(club_entity로)
# 3. view에서 클럽 manager확인 후 manager이름이면 삭제할수 있게 하기
# 4. view에서 작성자 email이면 수정, 삭제할 수 있게하기
# 
# =============================================================================================================
    # 게시글 추가
    def insert_text(self, board_entity):
        
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                # id,title,content,member_email,manager_email,club_name
                #
                sql = ("INSERT INTO `board` (`id`, `title`, `content`,`member_email`,`manager_email`,`club_name`)  VALUES (%s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (board_entity.id, board_entity.title , board_entity.content ,board_entity.member_email , board_entity.manager_email, board_entity.club_name))
                MembershipStore.connection.commit()
        finally:
            pass
    
    # 게시글 클럽별 view 생성
    # primary값인 인덱스 생성한다.
    def board_view(self, club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                # Create a new record
                sql =("create view `board_view` as \
                        select  cl.`member_roll`, b.`club_name`, b.`title,b.content`,  b.`manager_email` , b.`member_email` \
                        from `board` as b inner join `club` as cl\
                        on b.`club_name` = cl.`club_name`")
                cursor.execute(sql)
                result= cursor.fetchall()
                return result
        finally:
            pass
    # board_view에서 manager확인하기
    def board_view_manager(self,club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT `member_email` \
                     FROM `board_view` WHERE `club_name` = %s")
                cursor.execute(sql, (club_name ))
                result = cursor.fetchall() # 각 
                # CommunityStore.connection.commit()
                return result
        finally:
            pass
    def board_view_all(self, club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT * \
                     FROM `board_view` WHERE `club_name` = %s")
                cursor.execute(sql, (club_name ))
                result = cursor.fetchall() # 각 
                # CommunityStore.connection.commit()
                return result
        finally:
            pass
    
    # tree로 띄울 제목 내용 date 반환하기
    def show_board(self,club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("SELECT `id`, `content`,`title`,`member_email` \
                     FROM `board` WHERE `club_name` = %s ")
                cursor.execute(sql, club_name)
                result = cursor.fetchall() # 각 
                # CommunityStore.connection.commit()
                return result
        finally:
            pass

    def delete_board(self, email,id, club_name):
        try:
            with MembershipStore.connection.cursor() as cursor:
                sql = ("DELETE FROM `board` WHERE `member_email`=%s and `id`=%s and `club_name`=%s")
                cursor.execute(sql,(email, id, club_name))
                # AIStore.connection.commit() # insert update delete만 commit 함
                MembershipStore.connection.commit()
                return "삭제되었습니다"
        finally:
            pass
 






 