import datetime
class Book: #기본으로 제목, 저자, 빌리기가 가능한가에 대한 값을 갖습니다.
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.available = True
        self.d = datetime.datetime.now()
    
    #대출 가능여부 반환합니다.
    def check_book(self): 
        return self.available
    #책을 빌렸기 때문에 대출 일자를 저장 및 대출 가능여부를 False로 저장합니다. 
    def borrow_book2(self):
        self.d = datetime.datetime.now()
        self.available = False
        print("반납 일정은 ",self.d.year,'년 ', self.d.month,'월 ',self.d.day + 7,' 일입니다.')
    #책을 반납했기 때문에 대출 가능으로 변환합니다.
    def return_book2(self):
        self.d = datetime.datetime.now()
        self.available = True    
    
        
class EBook(Book):
    def __init__(self, title, author, category):
        super().__init__(title, author)
        self.category = category
    
     # 책의 제목과 저자, 카테고리, 대출가능여부를 보여줍니다. 
    def get_book(self): 
        print("제목 :"+ self.title)
        print("저자 : " + self.author)
        print("책 분류" + self.category)
        if self.available == True :
            print("현재 도서는 대출이 가능합니다.")
        else : 
            print("현재 도서는 이미 대출 상태입니다.")
            
class PaperBook(Book):
    def __init__(self, title, author, category):
        super().__init__(title, author)
        self.category = category
        
     # 책의 제목과 저자, 카테고리, 대출가능여부를 보여줍니다. 
    def get_book(self):
        print("제목 :"+ self.title)
        print("저자 : " + self.author)
        print("책 분류" + self.category)
        if self.available == True :
            print("현재 도서는 대출이 가능합니다.")
        else : 
            print("현재 도서는 이미 대출 상태입니다.")
    
    # 제목 불러오기
    def get_title(self):
        return self.title
    # 대출가능 불러오기
    def get_available(self):
        return self.available            
    