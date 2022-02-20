# 리스트 슬라이스 관련 다양한 문제들 풀어보기
# 이 문제는 리스트에서 필요한 부분을 슬라이스 하는 다양한 방법에 대해서 아는지를 묻는 문제이다.
# 리스트 슬라이스는 파이썬 프로그래밍시 약방의 감초처럼 많이 사용하는 것이다.
# 아래의 15개 문제는 자주 사용하는 것들이므로, 이 문제들만 수시로 풀어보면서 외워버리자.


# [10] : 아래의 결과는?
lst2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]
print( '[10] ---> ', lst2[1:3][1] )  #--- c


# [11] : 아래의 결과는?
print( '[11] ---> ', lst2[1:4][:] )  #--- b, c, d


# [12] : 아래의 결과는?
print( '[12] ---> ', lst2[2:6][1:-1] )  #--- [ c, d, e, f ] --> d, e


# [13] : 리스트내 요소를 모두 하나의 문자열로 출력하려면? --> abcdefghij --> join() 함수 사용.
print( '[13-1] ---> ', ''.join(lst2) )
print( '[13-2] ---> ', ', '.join(lst2) )


# [14] : 리스트내 중복 요소를 제거하려면? --> set()
ar = [ 1, 2, 3, 4, 5, 5, 5 ]
print( '[14] ---> ', list(set(ar)) )


# [15] : 아래 리스트에서 앞에(또는 뒤에) 문자 5개만 남기고 나머지 요소 모두 삭제하려면?
ar1 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]
ar2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]

del ar1[ 5 :  ]
print( '[15-1] ---> ', ar1 )  #--- a, b, c, d, e

del ar2[  : 5 ]
print( '[15-2] ---> ', ar2 )  #--- f, g, h, i, j



























