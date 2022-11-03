import pygame 
import sys
from tkinter import *
from tkinter import messagebox as msg

pygame.init()

#rgb색깔
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
button_true= False #스페이스키로 진행 할수있게 할건가?
phase = 0
scene = 0
size1 = [800,500]
love= 30
team =0
score =0
#사진관련
screen = pygame.display.set_mode(size1)
pygame.display.set_caption("두근!두근! 수뭉이와 데이트")

#시작화면 
Start_img = pygame.image.load("시작화면.png")
Start_img = pygame.transform.scale(Start_img, (800,500))
screen.blit(Start_img,(0,0))


#한누리관 배경
HN_img = pygame.image.load("한누리관.jpg")
HN_img = pygame.transform.scale(HN_img, (800,500))
#고백장소
final_img = pygame.image.load("고백장소.jpg")
final_img = pygame.transform.scale(final_img, (800,500))
#카페 배경
Cf_img = pygame.image.load("카페.jpg")
Cf_img = pygame.transform.scale(Cf_img, (800,500))

#수뭉이
SM_img = pygame.image.load("수뭉이.png")
SM_img = pygame.transform.scale(SM_img, (500,500))


#대화창
box_img = pygame.image.load("그림02.jpg")
box_img = pygame.transform.scale(box_img, (750,150))

happy = pygame.image.load("해피엔딩.png")
happy = pygame.transform.scale(happy, (800,500))

bad = pygame.image.load("배드엔딩.png")
bad = pygame.transform.scale(bad, (800,500))

#이름창 
tag_img = pygame.image.load("그림02.jpg")
tag_img = pygame.transform.scale(tag_img, (150,50))
#대답
select_1 = pygame.image.load("대답1-1.jpg")
select_1 = pygame.transform.scale(select_1, (250,100))

select_2 = pygame.image.load("대답1-2.jpg")
select_2 = pygame.transform.scale(select_2, (250,100))

select_3 = pygame.image.load("대답1-3.jpg")
select_3 = pygame.transform.scale(select_3, (250,100))

select_4 = pygame.image.load("문제1.jpg")
select_4 = pygame.transform.scale(select_4, (250,100))

select_5 = pygame.image.load("문제2.jpg")
select_5 = pygame.transform.scale(select_5, (250,100))

select_6 = pygame.image.load("문제3.jpg")
select_6 = pygame.transform.scale(select_6, (250,100))

select_7 = pygame.image.load("오.jpg")
select_7 = pygame.transform.scale(select_7, (250,100))

select_8 = pygame.image.load("엑스.jpg")
select_8 = pygame.transform.scale(select_8, (250,100))


word ='아이고 머리 아퍼....'
talker='주인공'

#텍스트 관련코드
font = pygame.font.Font('MapleStory Bold.ttf',30)
font2 = pygame.font.Font('MapleStory Bold.ttf',40)
font3 = pygame.font.SysFont(None,30)
text = font.render(word,True,black)
name = font2.render(talker,True,red)
loves= font.render(str(love),True,black)



pygame.display.update()




#무한 반복 상호작용 코드
play = True
while play:
    for event in pygame.event.get():
        #게임 종료 코드
        if event.type == pygame.QUIT:
            exit_ = msg.askyesno("종료창","게임을 종료하시겠습니까?")
            if exit_ == True:
                play = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and phase ==0 :
            phase = 1
 
        #게임 스타트
        if phase == 1 :        
           screen.blit(HN_img,(0,0))
           screen.blit(SM_img,(150,-30))
           screen.blit(box_img,(25,340))
           screen.blit(tag_img,(30,290))
           screen.blit(text,(55,360))
           screen.blit(name,(55,293))

           button_true = True
        elif phase == 2:        
               screen.blit(Cf_img,(0,0))
               screen.blit(SM_img,(150,-30))
               screen.blit(box_img,(25,340))
               screen.blit(tag_img,(30,290))
               screen.blit(text,(55,360))
               screen.blit(name,(55,293))
               button_true = True

        elif phase == 3:        
               screen.blit(final_img,(0,0))
               screen.blit(SM_img,(150,-30))
               screen.blit(box_img,(25,340))
               screen.blit(tag_img,(30,290))
               screen.blit(text,(55,360))
               screen.blit(name,(55,293))
               button_true = True
        #if True:
     #     screen.blit(loves,(50,10))
      #    loves= font.render(str(love),True,white)
     #     pygame.display.update()
#특이케이스 질문 1
        if scene == 16 :
              button_true= False
              screen.blit(select_1,(10,170))
              screen.blit(select_2,(280,170))   
              screen.blit(select_3,(550,170))   
              pygame.display.update()
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_z:
                       scene = 17
                       word ='교수님께 얘기해보는건 어떨까요 선배?'
                       button_true=True
                       love = love+20
                       print(love)
                       pygame.display.update()
                   elif event.key == pygame.K_x:
                          scene = 17
                          word ='조원들을 설득하는건 어떨까요?'
                          button_true=True
                          screen.blit(loves,(700,20))  
                          love = love + 20
                          pygame.display.update()
                   elif event.key == pygame.K_c:
                          scene = 17
                          word ='힘들지만 혼자하시는건 어떨까요..'
                          button_true=True
                          love = love
                          pygame.display.update()
#특이케이스 1번문제
        if scene == 35 :

              screen.blit(select_4,(10,170))
              screen.blit(select_5,(280,170))   
              screen.blit(select_6,(550,170))   
              pygame.display.update()
              button_true= False  
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_z:
                       scene = 36
                       word ='흠 이런 문제야 쉽지!'
                       button_true=True
                       score = score +1
                       pygame.display.update()
                   elif event.key == pygame.K_x:
                          scene = 36
                          word ='어라 이거였나??'
                          button_true=True
                          pygame.display.update()
                   elif event.key == pygame.K_c:
                          scene = 36
                          word ='어라 이거였나???'
                          button_true=True
                          pygame.display.update()
#2번문제
        if scene == 40 :

              screen.blit(select_7,(100,170))
              screen.blit(select_8,(400,170))     
              pygame.display.update()
              button_true= False  
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_z:
                       scene = 41
                       word ='흠 이런 문제야 쉽지!'
                       button_true=True
                       score = score +1
                       pygame.display.update()
                   elif event.key == pygame.K_x:
                          scene = 41
                          word ='어라 이거였나??'
                          button_true=True
                          pygame.display.update()
#3번 문제
        if scene == 44 :

              screen.blit(select_7,(100,170))
              screen.blit(select_8,(400,170))     
              pygame.display.update()
              button_true= False  
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_z:
                       scene = 45
                       word ='흠 이런 문제야 쉽지!'
                       button_true=True
                       score = score +1
                       pygame.display.update()
                   elif event.key == pygame.K_x:
                          scene = 45
                          word ='어라 이거였나??'
                          button_true=True
                          pygame.display.update()
#엔딩
        if scene >57:
            if love >= 100:
                screen.blit(happy,(0,0))
                pygame.display.update()
            else:
                screen.blit(bad,(0,0))
                pygame.display.update()
        pygame.display.update()

#키로 진행
        if event.type == pygame.KEYDOWN   and  button_true  == True:
            if event.key == pygame.K_SPACE  or event.key == pygame.K_RIGHT:
                scene = scene + 1
                pygame.display.update()
        if event.type == pygame.KEYDOWN   and  button_true  == True:
            if event.key == pygame.K_LEFT:
                scene = scene - 1
                pygame.display.update()

#노가다 파트
        if scene == 1:
            word ='헉!! 정신을 차려보니 내가 상명대공대생???'
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 2:
         
            screen.blit(box_img,(25,340))
            word ='안녕 인공아 여기서 멍하니 뭐해??'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            screen.blit(text,(55,360))
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 3:
            word ='(저분은 상명대 전설의 128학번 수뭉선배??)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 4:
            word ='(모든 선배님들의 관심을 한몸에 받고있는 씹인사 선배다)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 5:
            word = '(그리고 또한 나의 짝사랑 상대이기도 하다)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 6:
            word = '아 잠깐 멍떄렸네요 ㅎㅎ... 곧 수업들어가야죠'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 7:
            word = '갑자기 수업얘기를 들으니 선배의 표정이 안좋아진다'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 8:
            word = '(왜 인지 물어봐야겠다)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 9:
            word = '선배 무슨 안 좋은 일 있으세요?'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 10:
            word = '인공아 너도 알고리즘 수업 듣지?'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 11:
            word = '그럼요!'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 12:
            word = '(킹갓제네렐충무공갓성기교수님의 상명공대생의 필수전공!)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 13:
            word = '사실 알고리즘 팀플을 하는데...'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 14:
            word = '같은 팀 얘들이 팀플은 안하고 원신이라는 게임만 하더라고...'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 15:
            word = '별로 친하지도 않아서 어떻게 해야될까?'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 17:
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 18:
            word = "그래야 될것같네 도움이 된거 같아"
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 19:
            word = "혹시 내일  카공할래?? 시험도 얼마 안 남았잖아"
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 20:
            word = "(공부는 별로지만 수뭉선배와 함께라면!!)"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 21:
            word = "카공 좋죠 내일 수업끝나고 뵈요!"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 22:
            word = " 그래 내일 봐! "
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()


#두번째 날
        elif scene == 23:
            phase = 2
            word = "(그렇게 다음날 우리는 카페로갔다) "
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()

        elif scene == 24:
            word = "시험기간이라 그런지 사람이 많네 "
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 25:
            word = "그러게요 "
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 26:
            word = "자 그럼 시험도 얼마 안 남았는데 바로할까? "
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
            
        elif scene == 27:
            word = "(30분뒤.........) "
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 28:
            word = "인공아 넌 무슨 공부해??"
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update() 
        elif scene == 29:
            word = "파이썬 공부하고있어요"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update() 
        elif scene == 30:
            word = "파이썬 공부하고있어요"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 31:
            word = "오 나돈데 혹시 작년 문제  풀어줄수있어?"
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 32:
            word = "그럼요 저 코딩 고인물이에요(허세)"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        
        elif scene == 33:
            word = "자 그럼 어디 풀어볼까?"
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()

        elif scene == 34:
            word = "1번문제: 파이썬은 @@지향언어이다 "
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,red)
            pygame.display.update()

        elif scene == 36:
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,blue)
            pygame.display.update()
          
        elif scene == 37:
            if score ==1:
                word = ' 제법이군....'
            elif score ==0:
                    word = ' 그런것도 모르다니....'
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,red)
            pygame.display.update()

        elif scene == 38:
            word = '(시험지가 말을??일단 계속해서 풀어보자)'
            talker ='수뭉이'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()


        elif scene == 39:
            word = "2번문제: 파이썬은 인터프리터언어이다 OX "
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,red)
            pygame.display.update()

        elif scene == 41:
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()


        elif scene == 42:
            word = '바로 다음문제다!!!'
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,red)
            pygame.display.update()


        elif scene == 43:
            word = "파이썬은 1991년에 발표되었다OX"
            talker ='시험지'
            name = font2.render(talker,True,green)
            text = font.render(word,True,red)
            pygame.display.update()


        elif scene == 45:
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()


        elif scene == 46:
            if score ==3:
                word = '와 너 되게 잘한다'
                love = love+50
                score= score +1
            else:
                word = '괜찮아 실수할수있지'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()


        elif scene == 47:
            if score ==3:
                word = "에이 별거아니에요"
                text = font.render(word,True,black)
            else:
                word ='으 쪽팔려' 
                text = font.render(word,True,blue)
            talker ='주인공'
            name = font2.render(talker,True,red)
  
            pygame.display.update()

        elif scene == 48:
            word = '난 뇌섹남이 좋더라'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 49:
            if score == 3:
                word = "(이거 그린라이튼가???)"
                talker ='주인공'
                name = font2.render(talker,True,red)
                text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 50:
            word = '벌써 통근시간이네 이제 그만 나가자'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 51:
            phase =3
            word = '으 벌써 깜깜하다....'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 52:
            word = '(지금이라도 선배님께 내맘을 털어 놓아야겠어!!)'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,blue)
            pygame.display.update()
        elif scene == 53:
            word = '선배'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
        elif scene == 54:
            word = '응??'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()

        elif scene == 55:
            word = '사실 저 선배 좋아해요'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()
            
        elif scene == 56:
            if love >= 100:
                        word = '그럼 오늘부터 1일인거다'
                        ending = 0
            else:
                word = '미안 우리 그냥 친구사이로 있자...'
            talker ='수뭉이'
            name = font2.render(talker,True,blue)
            text = font.render(word,True,black)
            pygame.display.update()


        elif scene == 57:
            if love >= 100:
                        word = '눈나라고 불러도되요?'
                        ending = 0
            else:
                word = 'ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ'
            talker ='주인공'
            name = font2.render(talker,True,red)
            text = font.render(word,True,black)
            pygame.display.update()

            
              
           
      

      



