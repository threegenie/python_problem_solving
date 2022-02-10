# # 5강

# 아래 코드의 결과로 출력되는 것을 말해보시오.
# 이 문제는 클래스 사용법과 클래스내 메서드 작성법에 대해서 아는지를 묻는 문제이다.


# [1] : 클래스 생성
# ----------------------------------------
class Pet:
        # 짖다
        def bark_dog(self):
                print( '멍멍~' )
        def bark_cat(self):
                print( '야옹~야옹~' )
        def bark_hamster(self):
                print( '찍찍~' )
# ----------------------------------------


# [2] : 클래스 사용
p1 = Pet()
p1.bark_dog()

p2 = Pet()
p2.bark_cat()
p2.bark_dog()

p3 = Pet()
p3.bark_hamster()


# # 6강

# 이름과 나이를 전달받아 객체를 생성하는 Person 클래스를 만들고 객체 정보를 출력하시오.
# 정보를 생성하는 메서드명 --> create_info()
# 정보를 출력하는 메서드명 --> print_info()


# [1] : 클래스 생성
print( '[ 클래스를 사용한 캐릭터 생성 및 정보 출력 ]' )
# --------------------------------------------
class Person:
        
        # 정보 생성
        def create_info( self, name, age ):
                self.name = name
                self.age = age
                
        # 정보 출력
        def print_info( self ):
                print( '-' * 33 )
                print( 'Name : ', self.name )
                print( 'Age : ', self.age )
                # print( '-' * 33 )
# --------------------------------------------


# [2] : 클래스 사용
p1 = Person()
p1.create_info( '홍길동', 20  )
p1.print_info()

p2 = Person()
p2.create_info( '강감찬', 40 )
p2.print_info()

p3 = Person()
p3.create_info( '을지문덕', 30 )
p3.print_info()

