from BookM import EBook,PaperBook
from PersonM import Libralian,Student


personList = []#회원 리스트
nowUser = Student("김명준",25,"Student")  
personList.append(nowUser)
libNum = 1
tmp1 = PaperBook("나는 고양이가 좋아요","김명준","PaperBook")
tmp2 = PaperBook("나는 강아지가 좋아요","김명준","PaperBook")
tmp3 = PaperBook("나는 햄스터가 좋아요","김명준","PaperBook")
LibBooks = [] #현재 도서관 도서
LibBooks.append(tmp1)
LibBooks.append(tmp2)
LibBooks.append(tmp3)



print("안녕하세요. 도서관리 프로그램입니다.")
print("아래 해당 목록 중 원하는 서비스 번호를 입력해주세요 ")
print("(1) 회원 등록 ")
print("(2) 회원 로그인")
print("(3) 프로그램 종료 ")
actNum = int(input(" 사용하고자 하는 서비스 번호 : "))
start = True
while(start):
    while(actNum != 3):
        if actNum == 1:
            print("회원 등록을 입력하셨습니다.")
            userName = input(" 사용하고자 하는 회원님의 이름을 설정해주세요 : ")
            userAge = int(input(" 회원님의 나이를 입력해주세요 : "))
            userRole = input(" 회원님의 역할(Libralian,Student)을 설정해주세요 : ")
        if userRole == "Student":
            p1 = Student(userName,userAge,userRole)
            p1.get_role()
            personList.append(p1)
            print("회원 등록에 성공하였습니다!")
        if userRole == "Libralian":
            p1 = Libralian(userName,userAge,userRole)
            p1.get_role()
            personList.append(p1)
            print("회원 등록에 성공하였습니다!")
        elif actNum == 2:
            print("회원 로그인을 입력하셨습니다.")
            userName = input(" 사용하고자 하는 회원님의 이름을 설정해주세요 : ")
            for tmpUser in personList:
                if tmpUser.get_name() == userName:
                    nowUser = tmpUser
                    print("로그인에 성공하였습니다!")
                if nowUser.get_role() == "Student":
                    libNum = 0
                if nowUser.get_role() == "Libralian":
                    libNum = -1
                break
        elif actNum == 3:
            print("프로그램을 종료합니다.")
            start = False
        
    # 학생일 경우 
    while(libNum == 0 ):  
        print("원하시는 서비스 번호를 입력해주세요")
        print("(1) My도서대출 내용 조회")
        print("(2) 도서관 도서 목록 조회")
        print("(3) 도서 대출")
        print("(4) 도서 반납")
        print("(5) 프로그램 뒤로가기")
        actNum = int(input(" 번호 입력 : "))
        if actNum == 5 :
            print("프로그램을 종료합니다.")
            break
        
        if actNum == 1 :
            print(" (1) My도서대출 내용 조회를 선택하셨습니다. ")
            print("현재 회원님의 대출현황을 조회합니다.")
            for tmp in nowUser.books:
                tmp.show_book()
        if actNum == 2 :
            print("(2) 도서관 도서 목록 조회를 선택하셨습니다.")
            print("현재 도서관 내 모든 도서를 조회합니다.")
            for i in range(len(LibBooks)):
                LibBooks[i].show_book()
            
        if actNum == 3 :
            print("(3) 도서 대출을 입력하셨습니다.")
            bookTitle = input("원하시는 책의 제목을 입력해주세요")
            for i in LibBooks:
                if i.get_title() == bookTitle and i.get_available() == True:
                    nowUser.borrow_book(i,i.get_available())
                    i.brrow_book2() # 해당 책을 False로 바꿉니다. 
                    print("도서 대출에 성공했습니다!")
        if actNum == 4 : 
            print("(4) 도서 반납을 입력하셨습니다.")
            bookName = input("원하시는 책의 제목을 입력해주세요")
            for i in LibBooks:
                if i.get_title() == bookName:
                    nowUser.return_book(i)
                    i.return_book2() #해당 책을 True로 바꿉니다.
                    print("도서 반납에 성공했습니다!")
        if actNum == 5 :
            print("(5) 프로그램 뒤로가기을 선택하셨습니다.")
            print(" 뒤로 이동합니다.")
            actNum = 0
        
        
    # 사서일 경우 
    while(libNum == -1 ): 
        print("원하시는 서비스 번호를 입력해주세요")
        print("(1) 도서 추가")
        print("(2) 도서관 도서 목록 조회")
        print("(3) 프로그램 뒤로가기")
        actNum = int(input(" 번호 입력 : "))
        if actNum == 3:
            print("(3) 프로그램 뒤로가기를 선택하셨습니다.")
            print("뒤로 이동합니다.")
            break
        
        if actNum == 1 :
            print(" (1) 도서 추가를 선택하셨습니다. ")
            print("도서의 제목, 작가이름, 책의 종류를 입력해주세요.")
            bookName = input("제목 :")
            bookAuthor = input("작가 이름 : ")
            bookCategory = input("책 종류 : ")
            if bookCategory == "EBook":
                newBook = EBook(bookName,bookAuthor,bookCategory)
                nowUser.save_book(LibBooks,newBook)
            if bookCategory == "PaperBook":
                newBook = EBook(bookName,bookAuthor,bookCategory)
                nowUser.save_book(LibBooks,newBook)
        
        if actNum == 2 :
            print("(2) 도서관 도서 목록 조회를 선택하셨습니다.")
            print("현재 도서관 내 모든 도서를 조회합니다.")
            for i in range(len(LibBooks)):
                LibBooks[i].show_book()
