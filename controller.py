import service


class CommunityController:

    def register(self, travel_entity):
        #email valid check - regular express사용  email형식 체크
        if travel_entity.email == "" or len(travel_entity.email) ==0 :
            return "회원가입 형식에 어긋납니다."
        else:
            bm = service.CommunityService()
            message = bm.register(travel_entity)
            return message

    def get_login(self, email, password):
        bm = service.CommunityService()
        message = bm.login(email, password)
        print(message)
        return message 

    def update_controller(self,email, nickname, phonenumber):
        if email == "" or len(email) ==0 :
            return "값이 다 안채워졌습니다."
        else:
            bm = service.CommunityService()
            message = bm.entity_update(email,nickname,phonenumber)
            return message
    # 커뮤니티 탈퇴
    def delete_controller(self, email):
        if str(email) == "" or len(str(email)) == 0 :
            return "이메일 형식이 잘못되었습니다."
        else:
            bm = service.CommunityService()
            message = bm.entity_remove(email)
            return message
    
    def close(self):
        bm = service.CommunityService()
        bm.close()

    # 이메일로 커뮤니티 조회
    def select_community_by_email(self, email):
        if str(email) == "" or len(str(email)) == 0 :
            return False
        else:
            bm = service.CommunityService()
            message = bm.club_list_by_email(email)
            return message

    # 인사이트 페이지
    def for_insight(self,club_name ):
        bm = service.CommunityService()
        result = bm.to_view(club_name)
        return result


class ClubController:
    # community와 club을 나누어서 함수를 작성해야한다.
    # def __init__(self):
    #   super().__init__()


    def register_club(self, club_entity):
        if club_entity.club_name == "" or len(club_entity.club_name) ==0 :
            return "클럽 생성 규칙에 어긋납니다."
        else:
            bm = service.ClubService()
            message = bm.register(club_entity)
            #view select
            return message
    def join_club(self, club_entity):
        if club_entity.club_name == "" or len(club_entity.club_name) ==0 :
            return "클럽 생성 규칙에 어긋납니다."
        else:
            bm = service.ClubService()
            message = bm.join_club_member(club_entity)
            #view select
            return message

    # --- 클럽 등록, 목록에 쓰임
    def get_all_entity_club(self):
        bm = service.ClubService()
        listed = bm.get_all_club()
        return listed

    def update_controller(self,club_entity):
        if club_entity.prod_num == "" or len(club_entity.prod_num) ==0 :
       
            return "클럽 생성 규칙에 어긋납니다."
        else:
      
            bm = service.ClubService()
            message = bm.entity_update(club_entity)
            #view select
            return message
    
    def delete_controller(self, manager_email):
        if str(manager_email) == "" or len(str(manager_email)) == 0 :
            return  "클럽 생성 규칙에 어긋납니다."
        else:
            bm = service.ClubService()
            message = bm.entity_remove(manager_email)
            return message

    # club 명에 따른 멤버쉽 고객 확인하기
    def get_entity_controller(self,club_name):
        if str(club_name) == "" or len(str(club_name)) == 0 :
            return "클럽 생성 규칙이 잘못되었습니다."        
        else:
            bm = service.ClubService()
            entity = bm.get_all_entity(club_name) # 클럽별 멤버십 = entity
            if entity != None :
                return entity
            else:
                return "존재하지 않습니다."


    def search_club(self,club_name):
        selected = []
        # ★수정하기
        bm = service.ClubService()
        club_show = bm.get_all_club()
        for club in club_show:
            if club['club_name']==club_name:
                selected.append(club["club_info"])
                continue
            else:
                selected.append("--null--")
        return selected

    def get_clubinfo(self,club_info):
        selected = []
        if str(club_info) == "" or len(str(club_info)) == 0 :
            selected.append("--null--" )       
        elif bool(str(club_info)):
            bm = service.ClubService()
            entity = bm.get_by_info(club_info)
            if entity != None :
                selected.append(entity) # 여기까지 클럽 info로 클럽 명을 가지고 옴
            else:
                selected.append("추천 클럽이 존재하지 않습니다.")
        return selected



class BoardController:
    # board의 isexist는 
    def is_exist(self, club_name):
        if str(club_name) == "" or len(str(club_name)) ==0 :
            return "클럽명 규칙에 어긋납니다."
        else:
            bm = service.ClubService()
            club_find_name = bm.is_exist(club_name)
            return club_find_name
        

    def register_board(self, board_entity):

        if board_entity.club_name == "" or len(board_entity.club_name) ==0 :
            return "클럽명 규칙에 어긋납니다."
        else:
            bm = service.BoardService()
            message = bm.register(board_entity)
            #view select
            return message

    def get_all_board(self,club_name):
        bm = service.BoardService()
        listed = bm.get_all_board(club_name)
        return listed
    
    def delete_board(self, id, email,club_name):
        # email로 받아서 입력한 이메일이 관리자 or 작성자 email일 경우 진행
        bm = service.BoardService()
        message = bm.board_remove(id,email,club_name)
        return message

    def board_view_all(self, club_name):
        if club_name == "" or len(club_name) ==0 :
            return "클럽명 규칙에 어긋납니다."
        else:
            bm = service.BoardService()
            message = bm.board_view_all(club_name)
            #view select
            return message