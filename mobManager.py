import pygame
import random

#兩滴血移動慢
class MobTank:
    def __init__(self, speed):
        self.files = ['tank.png', 'tank_1.png']
        self.width = 240
        self.height = 375
        self.y=585
        self.x=1150
        self.scale=0.3
        self.move=0 #移動距離
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed #速度等級
        self.damage=20 #碰到主角的傷害
        #建立雙屬性
        self.element_1=Element(self.x+7, 550)
        self.element_2=Element(self.x+37, 550)
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
        self.y=600
        self.x=1150
        self.scale=0.3
        self.move=0 #移動距離
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed
        self.damage=35 #碰到主角的傷害
        self.element=Element(self.x+15, 550)#建立屬性

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
        self.y=602
        self.x=1150
        self.scale=0.3
        self.move=0 #移動距離
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed
        self.damage=30 #碰到主角的傷害
        self.element=Element(self.x+5, 550)#建立屬性

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
#魔王 
class Boss:
    def __init__(self, speed):
        self.files = ['Boss.png', 'Boss_1.png']
        self.width = 165
        self.height = 315
        self.y=470
        self.x=1150
        self.scale=6
        self.move=0 #移動距離
        self.recent_move_tick=self.time()
        self.init_anim_tick=self.time()
        self.speed=speed
        self.damage=9999 #碰到主角的傷害
        #建立多個屬性
        self.element=[]
        for i in range(12):
            self.element.append(Element(self.x, 430))
        
    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image
     
    def update(self, game_window):
        #行走動畫
        if (self.time()-self.init_anim_tick)%1200<600:
            animation=0
        else:
            animation=1
        if(animation==0):
            self.y=488
        else:
            self.y=471
        #向前移動距離
        if self.time()-self.recent_move_tick>=50:
            self.move+=1+0.2*self.speed #速度公式
            self.recent_move_tick=self.time()
        character_img = self.get_img(animation)
        scaled_img = pygame.transform.scale(character_img, (int(self.width * self.scale), int(self.height * self.scale)))
        game_window.blit(scaled_img, (self.x-self.move, self.y))
        count=12-len(self.element)
        #移動多個屬性標示
        for i in self.element:
            i.update(game_window, self.move+120-30*count)
            count+=1
            
    #被攻擊
    def under_attack(self, element):
        if element==self.element[0].get_element():
            self.element.pop(0)
        else:
            return False
        if len(self.element)==0:
            return True
        
    def time(self):
        return int(pygame.time.get_ticks())

class Element:
    def __init__(self, x, y):
        self.files=['metal_element.png', 'wind_element.png' , 'fire_element.png' , 'light_element.png']
        self.width = 264
        self.height = 195
        self.y=y
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
    #招喚boss
    def spawn_boss(self, level):
        self.moblist.append(Boss(level))
    #呼叫怪物更新與造成玩家傷害
    def update(self):
        damage=0
        for i in self.moblist:
            i.update(self.game_window)
            if 1200-i.move <= 100:
                damage+=i.damage
                self.moblist.remove(i)
        return damage
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