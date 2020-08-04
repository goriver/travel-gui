from exception import DuplicateException, RecordNotFoundException
from store import MembershipStore
from domain import TravelEntity, ClubEntity,BoardEntity
# import uuid
# import time
from random import *
# from domain 


class CommunityService:
    # 커뮤니티 내 회원 등록(회원가입시), 회원 수정, 회원 탈퇴 기능 수행
    db = MembershipStore() # 글로벌은 옳지 않다. 그러나 앱에서 사용하는 거라서 쓴다. 여유 있을 때 추가
    
    def is_exist(self,email):
        result = self.db.select_by_email(email) # community 는 email로 본다.
        return result


    # 커뮤니티 회원 등록 : email 존재여부 체크
    def register(self, travel_entity):
        result = self.is_exist(travel_entity.email)
        if not bool(result):
            self.db.insert_community(travel_entity)
            return travel_entity.email+" 등록되었습니다."
        else:
            try:
                raise DuplicateException("죄송합니다.")  
            except DuplicateException as error:
                return str(error)

    #커뮤니티 회원 정보 수정
    def entity_update(self,email, nickname, phonenumber):
        result=self.is_exist(email)
        if bool(result): # not bool이 아닌 email이 있다면~
            self.db.update_community(email, nickname, phonenumber)
            return email+"님 수정되었습니다."
        else:
            try:
                raise RecordNotFoundException("error")
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #커뮤니티 회원 삭제
    def entity_remove(self,email):
        result = self.is_exist(email)
        if bool(result):
            self.db.delete_community(email)
            return email+" 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException("error")
            except RecordNotFoundException as removeError:
                return str(removeError)
    # db창은 community를 나가면 close함
    def close(self):
        self.db.close()

    # 로그인
    def login(self,email,password):
        result = self.is_exist(email)
        if bool(result):
            tmp_message = self.db.select_pw(email)
            message = tmp_message[0]
            # print(message['password'])
            if message['password'] == password:
                return "로그인 성공"
            else:
                return "pw 오류"
        else:
            try:
                raise RecordNotFoundException("error")
            except RecordNotFoundException as error:
                return str(error)

    def club_list_by_email(self, email):
        result = self.is_exist(email)
        if bool(result):
            result = self.db.view_club_by_e(email)
            print(result)
            return result
        else:
            try:
                raise RecordNotFoundException("error")
            except RecordNotFoundException as error:
                return str(error)
    # view로 접근하기 위한 함수
    def to_view(self,club_name ):
        result = self.db.view(club_name)
        if bool(result):
            return result
        else:
            try:
                raise RecordNotFoundException("error가 발생했습니다.")
            except RecordNotFoundException as error:
                return str(error)



# 클럽 클래스
# # 클럽 등록(insert), 클럽 탈퇴, 클럽 생성(made) -> 일반+모두
# 클럽 관리(클럽 리스트 전체 보기, 클럽 address별 전화번호부) 기능 수행 
#           -> 클럽 관리자만(gui로 entry 받아서 입장할 클럽과email이 같은 경우 열기 아니면 error)
                 
class ClubService:
    db = MembershipStore()
    
    def is_exist(self, club_name):
        # messagebox던 simpledialog창을 띄워 email입력하게함
        result =ClubService.db.select_by_club(club_name)
        return result

    # 클럽 등록하기
    def register(self,club_entity):
        result =self.is_exist(club_entity.club_name)
        print(result)
        if bool(result):
            ClubService.db.insert_club(club_entity)
            return club_entity.club_name+" 등록되었습니다."
            # else:
                # return prod_entity.price+"는 불가능해요. 숫자형식(int)으로 적어주세요"
        else:
            try:
                raise DuplicateException(club_entity.club_name)  
            except DuplicateException as error:
                return str(error)
    # 클럽 가입하기
    def join_club_member(self,club_entity):
        result =self.is_exist(club_entity.club_name)
        print(result)
        if not bool(result):
            ClubService.db.insert_club(club_entity)
            return club_entity.club_name+" 등록되었습니다."
        else:
            try:
                raise DuplicateException("error")  
            except DuplicateException as error:
                return str(error)

    # 클럽 리스트 목록
    def get_all_club(self):
        return self.db.select_all_club()

    #각클럽별 회원목록(멤버쉽)
    def get_all_entity(self, club_name):
        result=self.is_exist(club_name)
        if bool(result): # not bool이 아닌 email이 있다면~
            return result
        else:
            try:
                raise RecordNotFoundException(club_name)
            except RecordNotFoundException as updateError:
                return str(updateError)


    #클럽 정보 수정
    def entity_update(self,club_entity):
        result=self.is_exist(club_entity.club_name)
        if bool(result): # not bool이 아닌 email이 있다면~
            self.db.update_club(club_entity)
            return club_entity.club_name+"이 수정되었습니다."
        else:
            try:
                raise RecordNotFoundException(club_entity.club_name)
            except RecordNotFoundException as updateError:
                return str(updateError)
    
    #클럽 삭제 only by manager
    def entity_remove(self,manager_email):
        result = self.is_exist(manager_email)
        if bool(result):
            self.db.delete_by_email(manager_email)
            return manager_email+"매니저님 해당 클럽이 삭제 되었습니다."
        else:
            try:
                raise RecordNotFoundException(manager_email)
            except RecordNotFoundException as removeError:
                return str(removeError)
    # info로 검색하기
    # ★여기
    def get_by_info(self, club_info):
        result = self.db.select_by_info(club_info)
        if bool(result):
            return result
        else:
            try:
                raise RecordNotFoundException(club_info)
            except RecordNotFoundException as removeError:
                return str(removeError)

class BoardService:
    db = MembershipStore()
    
    def is_exist(self, member_email):
        # messagebox던 simpledialog창을 띄워 email입력하게함
        club_names =BoardService.db.view_club_by_e(member_email)
        # clubservice맞음!!!!
        return club_names

    # 게시글 등록하기
    def register(self,board_entity):
        result = self.is_exist(board_entity.member_email)
        if bool(result):
            BoardService.db.insert_text(board_entity)
            return board_entity.member_email+"님 게시글이 등록되었습니다."
        else:
            try:
                raise RecordNotFoundException(board_entity.member_email)  
            except RecordNotFoundException as removeError:
                return str(removeError)

    def get_all_board(self, club_name):
        result = BoardService.db.board_view_manager(club_name)
        # 클럽명 입력시 있는 클럽이라면 매니저 이메이 포함된 데이터들을 반환한다.
        if bool(result):
            return BoardService.db.show_board(club_name)
        else:
            try:
                raise RecordNotFoundException(club_name)  
            except RecordNotFoundException as removeError:
                return str(removeError)

    #클럽 삭제 only by manager
    def board_remove(self,id,email, club_name):
        # 가입하고 작성한 글이 여러개일 경우 다 날라간다. 해결점 생각해보기
        # 속편하게 sql쿼리 날리기로 하였다.
        # uuid로 id값을 부여하고, 해당 클럽내 title로 uuid를 찾는다.
        # club테이블에서 club name으로 모든 정보를 가지고 온다.
        club = ClubService()
        result = club.is_exist(club_name)
        print(str(result))
        if bool(result):
            return BoardService.db.delete_board(email,id, club_name)
        else:
            try:
                raise RecordNotFoundException(club_name)  
            except RecordNotFoundException as removeError:
                return str(removeError)

    def board_view_all(self, club_name):
        result = BoardService.db.board_view_manager(club_name)
        # 클럽명 입력시 있는 클럽이라면 매니저 이메이 포함된 데이터들을 반환한다.
        if bool(result):
            return BoardService.db.board_view_all(club_name)
        else:
            try:
                raise RecordNotFoundException(club_name)  
            except RecordNotFoundException as removeError:
                return str(removeError)

