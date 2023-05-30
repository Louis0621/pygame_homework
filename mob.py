import pygame
import random

#兩滴血移動慢
class MobTank:
    def __init__(self, speed):
        self.files = ['tank.png', 'tank_1.png']
        self.width = 240
        self.height = 375
        self.y=685
        self.x=1150
        self.scale=0.3
        self.move=0 #移動速度
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed #速度等級
        #建立雙屬性
        self.element_1=Element(self.x+7)
        self.element_2=Element(self.x+37)
        #中彈兩次判斷
        self.hp=2

    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image

    def update(self, game_window):
        animation=0
        #行走動畫
        if (self.time()-self.init_anim_tick)%900<450:
            animation=0
        else:
            animation=1
        #向前移動距離
        if self.time()-self.recent_move_tick>=50:
            self.move+=1.5+0.3*self.speed #速度公式
            self.recent_move_tick=self.time()
        character_img = self.get_img(animation)
        scaled_img = pygame.transform.scale(character_img, (int(self.width * self.scale), int(self.height * self.scale)))
        game_window.blit(scaled_img, (self.x-self.move, self.y))
        #移動雙屬性標示
        if self.hp==2:
            self.element_1.update(game_window, self.move)
        self.element_2.update(game_window, self.move)
    #被攻擊
    def under_attack(self, element):
        if self.hp==2:
            if self.element_1.get_element()==element:
               self.hp-=1
        else: 
            if self.element_2.get_element()==element:
                return True

    def time(self):
        return int(pygame.time.get_ticks())
#普通怪物
class MobAlien:
    def __init__(self, speed):
        self.files = ['alien.png', 'alien_1.png']
        self.width = 165
        self.height = 315
        self.y=700
        self.x=1150
        self.scale=0.3
        self.move=0 #移動速度
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed
        self.element=Element(self.x+15)#建立屬性

    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image

    def update(self, game_window):
        #行走動畫
        if (self.time()-self.init_anim_tick)%800<400:
            animation=0
        else:
            animation=1
        #向前移動距離
        if self.time()-self.recent_move_tick>=50:
            self.move+=2.5+0.3*self.speed #速度公式
            self.recent_move_tick=self.time()
        character_img = self.get_img(animation)
        scaled_img = pygame.transform.scale(character_img, (int(self.width * self.scale), int(self.height * self.scale)))
        game_window.blit(scaled_img, (self.x-self.move, self.y))
        self.element.update(game_window, self.move)#移動屬性標示
    #被攻擊
    def under_attack(self, element):
        if element==self.element.get_element():
            return True
        else:
            return False
    
    def time(self):
        return int(pygame.time.get_ticks())
#移動快速
class MobSpider:
    def __init__(self, speed):
        self.files = ['spider.png', 'spider_1.png']
        self.width = 165
        self.height = 315
        self.y=702
        self.x=1150
        self.scale=0.3
        self.move=0 #移動速度
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed
        self.element=Element(self.x+5)#建立屬性

    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image

    def update(self, game_window):
        #行走動畫
        if (self.time()-self.init_anim_tick)%600<300:
            animation=0
        else:
            animation=1
        #向前移動距離
        if self.time()-self.recent_move_tick>=50:
            self.move+=3+0.5*self.speed #速度公式
            self.recent_move_tick=self.time()
        character_img = self.get_img(animation)
        scaled_img = pygame.transform.scale(character_img, (int(self.width * self.scale), int(self.height * self.scale)))
        game_window.blit(scaled_img, (self.x-self.move, self.y))
        self.element.update(game_window, self.move)#移動屬性標示  
    #被攻擊
    def under_attack(self, element):
        if element==self.element.get_element():
            return True
        else:
            return False
    
    def time(self):
        return int(pygame.time.get_ticks())

class Element:
    def __init__(self, x):
        self.files=['metal_element.png', 'wind_element.png' , 'fire_element.png' , 'light_element.png']
        self.width = 264
        self.height = 195
        self.y=650
        self.x=x
        self.scale=0.1
        #隨機選擇屬性
        rand=random.randint(1,10)
        if rand<=2:
            self.index=0
        elif rand<=5:
            self.index=1
        elif rand<=7:
            self.index=2
        else:
            self.index=3
    
    def get_element(self):
        return self.index
    
    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image
    
    def update(self, game_window, move):
        character_img = self.get_img(self.index)
        scaled_img = pygame.transform.scale(character_img, (int(self.width * self.scale), int(self.height * self.scale)))
        game_window.blit(scaled_img, (self.x-move, self.y))
    
#怪物管理
class MobManager:
    def __init__(self, game_window):
        self.moblist=[]
        self.game_window=game_window
    #招喚怪物
    def spawn(self, level):
        rand=random.randint(1,10)
        if rand<=4:
            self.moblist.append(MobAlien(level))
        elif rand<=7:
            self.moblist.append(MobSpider(level))
        else:
            self.moblist.append(MobTank(level))
    #呼叫怪物更新
    def update(self):
        for i in self.moblist:
            i.update(self.game_window)
    #以對應元素攻擊最前方怪物
    def attack(self, element):
        if len(self.moblist)!=0:
            nearest_move=self.moblist[0].move
            nearest=self.moblist[0]
            for i in self.moblist:
                if i.move>nearest_move:
                    nearest_move=i.move
                    nearest=i
            if nearest.under_attack(element)==True:
               self.moblist.remove(nearest)

#READ ME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#這段下面的程式碼是我測試用的可以不理他或刪掉 或是把註解拿掉看範例測試
#你那邊先建立一個MobManager的物件 傳入game_window
#在遊戲執行迴圈裡塞MobManager的update去更新角色移動
#然後MobManager的spawn(怪物速度等級)就能隨機招喚一種怪物 不同怪物比例目前是定值 可以看要不要隨等級變動
#怪物裡的速度公式也都要再配合你開槍速度甚麼的做平衡
#開槍用MobManager的attack(屬性) 我是設0~3 照你FB傳的順序



"""pygame.init()

WINDOW_SIZE = (1200, 800)

BACKGROUND_IMAGE = "background.png"

game_window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("The shooting game")

# Load the background image and scale it to fit the window
background_image = pygame.image.load(BACKGROUND_IMAGE)
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)


running=True

manager=MobManager(game_window)

manager.spawn(1)
manager.spawn(2)
manager.spawn(3)
manager.spawn(4)
manager.spawn(5)
recent=0
gun=0
while running:
    game_window.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    manager.update()
    #四種槍枝輪流開槍(測試用)
    if pygame.time.get_ticks()-recent>=1000:
        recent=pygame.time.get_ticks()
        manager.attack(gun)
        gun+=1
        if gun>3:
            gun=0
    pygame.display.update()
pygame.quit()"""
