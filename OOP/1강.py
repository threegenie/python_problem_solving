# 클래스, 함수, 캐릭터, 랜덤

# 파이썬 OOP에서 클래스란 무엇인지 설명해보시오.
# [클래스 강의1] : 변수와 리스트를 사용하여 캐릭터 정보를 저장하고 출력해보시오.


# [1] : 변수
print( '[ 변수를 사용한 캐릭터 정보 출력 ]' )
person1_name = '홍길동'
person1_age = 20
person1_power = 7  #--- 파워는 1~9 사이에서 랜덤으로 결정 --;;

person2_name = '이순신'
person2_age = 30
person2_power = 9

print( f'귀하가 선택하신 {person1_name} 캐릭터의 나이는 {person1_age}살이고 파워는 레벨 {person1_power} 입니다.' )
print( f'귀하가 선택하신 {person2_name} 캐릭터의 나이는 {person2_age}살이고 파워는 레벨 {person2_power} 입니다.' )
print( '-' * 140 )


# [2] : 리스트 또는 딕셔너리
# 딕셔너리 타입을 사용하면 리스트 보다는 더 효율적으로, 더 체계적으로 데이터 핸들링을 할 수는 있다.
print( '[ 리스트를 사용한 캐릭터 정보 출력 ]' )
person1 = [ '홍길동', 20, 7 ]
person2 = [ '이순신', 30, 9 ]

print( f'귀하가 선택하신 {person1[0]} 캐릭터의 나이는 {person1[1]}살이고 파워는 레벨 {person1[2]} 입니다.' )
print( f'귀하가 선택하신 {person2[0]} 캐릭터의 나이는 {person2[1]}살이고 파워는 레벨 {person2[2]} 입니다.' )
print( '-' * 140 )
