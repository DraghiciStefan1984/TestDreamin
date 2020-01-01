import threading
import time
import random


class Robot(threading.Thread):
    def run(self):
        self.change_action()
    
    def change_action(self):
        while True:
            time.sleep(20)
            self.__mine_foo()
            time.sleep(20)
            self.__mine_bar()
            time.sleep(20)
            self.__assemble_foobar()
        
    def __mine_foo(self):
        time.sleep(1)
        print('mining foo')
        Resources._foos+=1
    
    def __mine_bar(self):
        random_sleep_time=random.uniform(0.5, 2)
        time.sleep(random_sleep_time)
        print('mining bar')
        Resources._bars+=1
    
    def __assemble_foobar(self):
        time.sleep(2)
        success_rate=random.randrange(100)
        if success_rate>=70:
            if Resources._foos!=[] and Resources._bars!=[]:
                Resources._bars-=1
                Resources._foobars+=1
                print('assembling foobar')
            Resources._foos-=1
    

class RobotManager:
    _ron_cost=3
    _foo_cost=2
    
    def __init__(self):
        self.robot1=Robot()
        self.robot2=Robot()
        Resources._robots.append(self.robot1)
        Resources._robots.append(self.robot2)
        self.robot1.start()
        self.robot2.start()
        
    def sell_foobar(self):
        random_foo_amount=random.randint(2, 4)
        if random_foo_amount<=Resources._foobars:
            Resources._foobars-=random_foo_amount
            Resources._ron_amount+=random_foo_amount
            print(str(random_foo_amount)+' foobars sold')
        time.sleep(10)

            
    def buy_robot(self):
        if Resources._foos>=RobotManager._foo_cost and Resources._ron_amount>=RobotManager._ron_cost:
            robot=Robot()
            Resources._foos-=RobotManager._foo_cost
            Resources._ron_amount-=RobotManager._ron_cost
            print('robot bought')
            Resources._robots.append(robot)
            robot.start()

    
class Resources:
    _foos=0
    _bars=0
    _foobars=0
    _ron_amount=0
    _robots=[]
    

#test
robot_manager=RobotManager()
max_robot_count=42
robot_count=0
while robot_count<=max_robot_count:
    robot_manager.sell_foobar()
    robot_manager.buy_robot()
    robot_count+=1
    print(robot_count)