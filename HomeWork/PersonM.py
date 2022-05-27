class Person: #기본으로 이름, 나이, 빌린 책의 리스트를 갖습니다.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books = [] #개인 도서 대출 리스트 
        
    def get_role(self):
        return [str(self.role)]
    
    def get_name(self):
        return [str(self.name)]
        
    # 책 대출 메서드 / 책이 대출이 가능할 경우 대출리스트에 추가하고 True를 반환해줍니다. 
    def borrow_book(self,book,available):  
        if available == True :
            self.books.append(book) 
            return True
        
    # 책 반납 메서드 / 대출 리스트에서 해당 책을 삭제합니다.
    def return_book(self,book):            
        self.books.remove(book)
        print("해당 책을 반납 하였습니다.")
        print("감사합니다.")
        
    # 현재 개인이 대출 중인 책들 리스트를 반환합니다.
    def show_book(self):
        print("사용자가 현재 대출 중인 책들 입니다.")
        print("반환 일자를 넘지 않길 바라겠습니다.")
        return self.books


        
class Student(Person): #Person 상속
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role




#사서 / 사서의 경우 책을 저장할 수 있습니다.
class Libralian(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role


    #도서 저장메서드 /#lib_books리스트에 book을 저장해줍니다.
    def save_book(lib_books,book):
        lib_books.append(book)
        print("해당 내용의 책을 저장했습니다.")
