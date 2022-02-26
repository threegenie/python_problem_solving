# 전달받은 문자열에서 임의의 문자 하나를 화면에 출력하는 코드를 구현하시오. 

# 이 문제는 random 모듈내 choice() 함수의 사용법을 아는지를 묻는 문제이다.

 # [1] : random.choice() # random.choice() 함수는 매개변수로 시퀀스 자료형을 받는다. 
 
 # 시퀀스 자료형 --> 리스트, 튜플, range, 문자열 --> 여기에서 랜덤으로 하나의 요소를 뽑아 반환. 
 # 빈 리스트 --> X 
 
 import random 
 
 a = random.choice( 'koreaKOREA' ) 
 print( '[1]', a ) 
 
 b = random.choice( 'korea KOREA' ) 
 print( '[2]', b ) 
 
 c = random.choice( [ 'k', 'o', 'r', 'e', 'a', '', 'K', 'O', 'R', 'E', 'A' ] ) 
print( '[3]', c ) 

d = random.choice( [] ) 
#--- Err --;; 
print( d )
