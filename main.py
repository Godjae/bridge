import random
print("오징어 게임에 참가하셨습니다")
print("이번 게임은 다리 건너기 입니다")
#오른쪽일까 왼쪽일까
print("오른쪽 왼쪽 중에 선택 하세요")
#1번은 왼쪽 2번은 오른쪽
print("1번은 왼쪽 2번은 오른쪽")
# blist=[1,1,2,1,1,2,2,2,1,2]
# 총 10칸의 다리가 있다.
blist=[]
# 다리 리스트가 고정이네? 무작위로 다리의 정보를 나타내자
for i in range(10):
    blist.append(random.randint(1,2)) #blist에 1,2랜덤으로추가
# print(blist)
lr_dict = {1:"왼쪽", 2:"오른쪽"} #1은 왼쪽점프 2는 오른쪽점프
# print(lr_dict)
# 왼쪽인지 오른쪽인지만 맞추면 살수있고 틀리면 죽는다
# 최종 10칸까지 다가면 승리
# 중간에 틀리면 탈락, 게임오버
# 다리의 갯수만큼 반복
life=0
while life<5:
    for i,v in enumerate(blist): #i:인덱스(0~9) v:값(1,2)
        num=int(input("선택하세요(숫자만): ")) #무조건 숫자만취급!
        print("{}번으로 점프".format(num))
        #내가 선택하는 것에 따라 살고 죽는다!

        if v==num:
            print("{}번 다리 통과".format(i+1))
            if i==len(blist)-1:
                print("살았다! 다음 관문으로 넘어갑니다")
                break
        else:
            print("낙사")
            print("게임오버")
            life=life+1
            print("목숨{}개 소모".format(life))
            break
    if life==5:
        print("게임오버")