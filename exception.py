class DuplicateException(Exception):
    def __init__(self,message):
        super().__init__(message+" 존재하는 정보입니다.")


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message+" 존재하지 않습니다.")