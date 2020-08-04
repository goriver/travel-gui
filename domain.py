
class TravelEntity:
    #생성자정의 : member variable - name, age, email, major 초기화
    def __init__(self, email, password, nickname, phonenumber, birthday , address):
        self.email=email
        self.password=password
        self.nickname = nickname
        self.phonenumber=phonenumber
        self.birthday=birthday
        self.address=address
    # enroll_date는 코드의 entity로는 포함되지 않으며 sql의 insert시에만 추가됨

    #email정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, email):
        if(self.email == email):
            return True
        else:
            return False

    def __str__(self):
        return " {0} : {1} : {2} : {3} : {4} : {5} ".format(self.email, self.password, self.nickname, self.phonenumber, self.birthday , self.address ) 


    #toJson   : Entity -> json 변환 
    #fromJson : jons -> Entity 변환

class ClubEntity:
    def __init__(self, club_name, club_info, manager_email, member_email, member_roll): # phone을 foriegn 키로 가져온다.
        # self.uid = uuid.uuid4() # primary key값 생성을 위한 random한 uuid 생성
        self.club_name=club_name
        self.club_info=club_info
        self.manager_email = manager_email
        self.member_email = member_email
        self.member_roll = member_roll # 관리자만 관리자라고만 뜬다. 나머지는 default이다.

    # enroll_date는 코드의 entity로는 포함되지 않으며 sql의 insert시에만 추가됨

    #member_email 정보가 같은 경우 같은 객체로 재정의
    def __eq__(self, member_email):
        if(self.member_email == member_email):
            return True
        else:
            return False

    def __str__(self):
        return "{0} : {1} : {2} : {3} : {4} ".format( self.club_name, self.club_info, self.manager_email, self.member_email,self.member_roll )

class BoardEntity:
    def __init__(self,id, title, content, member_email, manager_email, club_name): # phone을 foriegn 키로 가져온다.
        # self.uid = uuid.uuid4() # primary key값 생성을 위한 random한 uuid 생성
        self.id = id
        self.title=title
        self.content = content
        self.member_email = member_email # 10000자까지이다.
        self.manager_email = manager_email
        self.club_name = club_name
        

    # enroll_date는 코드의 entity로는 포함되지 않으며 sql의 insert시에만 추가됨

    def __str__(self):
        return "{0} : {1} : {2} : {3} : {4} : {5} ".format( self.id ,self.title, self.content, self.member_email, self.manager_email, self.club_name )
    

