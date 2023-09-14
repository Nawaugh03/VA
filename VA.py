#import speech_recognition as sr
#import pyttsx3
#import openai
#from DatabaseManager import DBmanager as dbm
#from collections import deque
#import speech_recognition as sr
#import pyttsx3
import time
#import datetime
#import logging 
#import json
#import webbrowser
import random
#import os
import math
#import random
import tkinter as tk
"""
class VirtualAssistant: 
    def __init__(self):
        self.__info=None
        #self.apikey="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"
        #openai.api_key=self.apikey
        self.__engine = pyttsx3.init()
        voices=self.__engine.getProperty('voices')
        self.__engine.setProperty('rate',130)
        selected_voice =voices[1]
        self.__engine.setProperty('voice', selected_voice.id)
        self.__Memory=deque()
        self.GetIdentity()
        #self.online()

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-US")
            print(f"User: {query}")
            return query
        except Exception as e:
            print(e)
            return None
    
    def speak(self,text):
        self.__engine.say(text)
        self.__engine.runAndWait()
    def fetchAIresponse(self, input):
        response = openai.Completion.create(engine="text-davinci-002", prompt=input,max_tokens=100)
        generated_text=response['choices'][0]['text']
        return generated_text
    
    def GetIdentity(self):
        json_file="VA.json"
        data=""
        with open(json_file,'r')as file:
            data=json.load(file)
        self.__info=data
    def SayHello(self):
        self.speak("Hello, how are you?")
    def SayGoodBye(self):
        self.speak("Goodbye! Have a great day!")
    def PlaylistOption(self):
        Playlist=self.GetPlaylist()
        self.speak("Playing a random video off of playlist")
        random_url=random.choice(Playlist)
        webbrowser.open(random_url)

    def online(self):
        self.speak(f"Hello... my name is {self.GetName()} and I'm your virtual assistant. How can I help you today?")
        time=datetime.datetime.now().strftime("%b %d, %Y %H:%M")
        Message=f"it is currently {time}"
        self.speak(Message)
        while True:
            user_input = self.listen()
            if user_input:
                if "hello" in user_input.lower():
                    self.SayHello()
                elif "goodbye" in user_input.lower():
                    self.SayGoodBye()                    
                    break
                elif "play music" in user_input.lower():
                    self.PlaylistOption()
                else:
                    self.speak("Uhm I don't know what that means")
    
    def GetInfo(self):
        return self.__info
    def GetName(self):
        return self.__info.get("name")
    def GetPlaylist(self):
        return self.__info.get("music")
    def GetKeywords(self):
        return self.__info.get("keywords")
    def __del__(self):
        pass
        Report=self.__info
        with open(f"VA.json", "w")as file:
            json.dump(Report, file)
"""
class Node:
    def __init__(self, canvas,x,y,size,color,SetColors):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.Originalsize=size
        self.minimumsize=self.Originalsize-19
        self.maximumsize=self.Originalsize+10
        self.direction=1
        self.currentsize=self.minimumsize
        self.alternatecolors=SetColors
        self.color=color
        self.square=None
        self.isfloating=False
        self.ispulsing=False
        self.isidle=False
        self.increase=False
        self.isgrowing=False
        self.isspinning=False
        self.iscentered=False
        self.snowflakes=[]
        #self.spawnNodeAnimation()

    def draw(self, initialsize):
        # Draw the square on the canvas
        x1 = self.x - initialsize // 2
        y1 = self.y - initialsize // 2
        x2 = self.x + initialsize // 2
        y2 = self.y + initialsize // 2
        self.square = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color, fill=self.color)
    def floating(self,t=0, amplitude=50, step_size=0.11):
        
        y= y_center + amplitude *math.sin(t)
        self.canvas.coords(self.square, x_center-self.currentsize, y-self.currentsize, x_center + self.currentsize, y + self.currentsize)
        t+=step_size
        if(self.isfloating):
            self.canvas.after(45, self.floating,t, amplitude, step_size)

    def spinningIdle(self,spiral_radius,angle):
        global x_center, y_center
        spiral_angular_speed = 5
        spiral_radius_increment = 1
        x_spiral =x_center + int(spiral_radius * math.cos(math.radians(angle)))
        y_spiral = y_center + int(spiral_radius * math.sin(math.radians(angle)))
        canvas.coords(self.square, x_spiral - self.currentsize, y_spiral - self.currentsize, x_spiral + self.currentsize, y_spiral + self.currentsize)
        angle += spiral_angular_speed
        if (spiral_radius<200 and self.increase):
            spiral_radius += spiral_radius_increment
        elif(spiral_radius>0 and self.increase == False):
            spiral_radius -= spiral_radius_increment
        
        """
        if(self.maxIdleTime==int(time.time()-self.timer)):
            self.increase=False
            self.timer=time.time()
        if(spiral_radius==0 and self.increase is False):
            self.isidle=False
            self.timer=0
        """
        #print("is spinning")
        if(self.isspinning==True):
            #print("is spinning")
            self.canvas.after(30,self.spinningIdle,spiral_radius, angle)  
        if(spiral_radius<=0):
            self.isspinning=False
           

    def boundaryIdle(self,x_speed, y_speed):
        
        current_coords=self.canvas.coords(self.square)
        new_x1 = current_coords[0] + x_speed
        new_y1 = current_coords[1] + y_speed
        new_x2 = current_coords[2] + x_speed
        new_y2 = current_coords[3] + y_speed
        if new_x1 <= 0 or new_x2 >= self.canvas.winfo_reqwidth():
            x_speed = -x_speed  # Reverse the horizontal direction
            new_color=random.choice(self.alternatecolors)
            self.canvas.itemconfig(self.square, fill=new_color, outline=new_color)
        if new_y1 <= 0 or new_y2 >= self.canvas.winfo_reqheight():
            y_speed = -y_speed  # Reverse the vertical direction
            new_color=random.choice(self.alternatecolors)
            self.canvas.itemconfig(self.square, fill=new_color, outline=new_color)
        canvas.move(self.square,x_speed,y_speed)
        #if (self.maxIdleTime==int(time.time()-self.timer)):
        #    self.isidle=False
        #    self.setToCenter(1)
        if(self.isidle):
            canvas.after(10, self.boundaryIdle, x_speed,y_speed)
            

    def spawnNodeAnimation(self):
        self.draw(self.currentsize)
        self.canvas.after(275, self.grow_node,self.Originalsize,15)
    def setToCenter(self,steps=15):
        global x_center, y_center
        coordinates=self.canvas.coords(self.square)
        x1,y1,x2,y2=coordinates
        #print(*coordinates)
        current_centerx=(x1+x2)/2
        current_centery=(y1+y2)/2
        #print(current_centerx,current_centery)
        dx=(x_center-current_centerx)/steps
        dy=(y_center-current_centery)/steps
        #print(dx,dy)
        
        
        #canvas.coords(self.square, dx - self.currentsize, dy-self.currentsize, dx+self.currentsize, dy+self.currentsize)
        if (abs(dx) <= 0.1 and abs(dy) <= 0.1):
            return
        
    
        self.canvas.move(self.square,dx,dy)  
        self.canvas.after(steps, self.setToCenter, steps)
       
    def resetSize(self):
        if(self.Originalsize != self.currentsize):
            if(self.currentsize>self.Originalsize):
                self.currentsize-=1
            elif(self.currentsize<self.Originalsize):
                self.currentsize+=1
            self.canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
            self.canvas.after(15, self.resetSize)   
        else:
            return
    def pulsing(self,maxsize,delay):
        maxaura=maxsize
        delay=delay
        if(self.isidle): 
            if(self.isgrowing):
                self.grow_node(maxaura, delay=delay)
            else:
                self.shrink_node(self.Originalsize, delay=delay)
            self.canvas.after(delay,self.pulsing,maxsize,delay)
        
    def grow_node(self,target,delay):
        self.currentsize+=0.5
        #canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
        if self.currentsize <  target:
            canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
            self.canvas.after(delay,self.grow_node,target,delay)
        else:
            self.isgrowing=False
            return
    def shrink_node(self, target, delay):
        self.currentsize -= 0.5
        if self.currentsize > target:
            self.canvas.coords(self.square, self.x - self.currentsize, self.y - self.currentsize, self.x + self.currentsize, self.y + self.currentsize)
            self.canvas.after(delay, self.shrink_node,target,delay)
        else:
            self.isgrowing=True
            return
            
    def figureEight(self, angle, angle_increment):
        #current_coords=self.canvas.coords(self.square)
        x = self.canvas.winfo_reqwidth() // 2 + (self.canvas.winfo_reqwidth() // 3) * math.cos(angle)
        y = self.canvas.winfo_reqheight() // 2 + (self.canvas.winfo_reqheight() // 5) * math.sin(2 * angle)
        
        canvas.coords(self.square, x - self.currentsize, y - self.currentsize, x + self.currentsize, y + self.currentsize)
        
        angle += angle_increment        
        if angle >= 2 * math.pi:
            angle = 0
        if(self.isidle):
            self.canvas.after(30, self.figureEight, angle, angle_increment)
    def change_color(self, current_color, target_color, steps, current_step):

        # Convert the current color to RGB values
        current_r = int(current_color[1:3], 16)
        current_g = int(current_color[3:5], 16)
        current_b = int(current_color[5:7], 16)

        # Calculate the next intermediate color in hexadecimal format
        r1, g1, b1 = current_r, current_g, current_b
        r2, g2, b2 = int(target_color[1:3], 16), int(target_color[3:5], 16), int(target_color[5:7], 16)
        step = current_step / steps
        r = int(r1 + step * (r2 - r1))
        g = int(g1 + step * (g2 - g1))
        b = int(b1 + step * (b2 - b1))
        color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)

        # Change the square's fill color
        canvas.itemconfig(self.square, fill=color_hex, outline=color_hex)

        # Increment the step counter
        current_step += 1

        # Schedule the next color change if not finished
        if current_step <= steps:
            self.canvas.after(steps, self.change_color,current_color, target_color, steps, current_step)

    def create_snowflake(self):
        x = random.randint(0, self.canvas.winfo_reqwidth())
        y = 0
        size = random.randint(5, 10)
        snowflake = canvas.create_oval(x, y, x + size, y + size, fill='white')
        self.snowflakes.append((snowflake, x, y, size))
        
        # Schedule the next snowflake creation
        if(self.isidle):
            win.after(random.randint(10, 50), self.create_snowflake)

    # Function to move the snowflakes
    def move_snowflakes(self):
        for i in range(len(self.snowflakes)):
            snowflake, x, y, size = self.snowflakes[i]
            canvas.move(snowflake, 0, 5)  # Increase the move distance to make it faster
            _, new_y1, _, new_y2 = canvas.coords(snowflake)
            
            # Remove snowflakes that go below the canvas
            if new_y2 >= self.canvas.winfo_reqheight():
                canvas.delete(snowflake)
                self.snowflakes[i] = (None, None, None, None)
        
        # Remove empty snowflake entries
        self.snowflakes[:] = [entry for entry in self.snowflakes if entry[0] is not None]
        
        # Schedule the next move
        if (not self.snowflakes):
            return
        else:
            win.after(50, self.move_snowflakes)  # Decrease the time interval to make it more frequent
    
    def idle(self, randomcode):
        self.isidle=True
        if(randomcode==0):
            self.increase=True
            self.isspinning=True
            self.spinningIdle(0,0)
        elif(randomcode==1):
            self.boundaryIdle(3,2)
        elif(randomcode==2):
            self.isgrowing=True
            self.pulsing(maxsize=self.maximumsize+40, delay=40)
        elif(randomcode==3):
            self.figureEight(4.75,0.05)
        elif(randomcode==4):
            self.change_color(self.canvas.itemconfig(self.square, "fill")[4], "#00E1FF",30, 0)
            self.create_snowflake()
            self.move_snowflakes()
            
    
    def reset(self, randomnum):
        if(randomnum==0):
            self.increase=False
            if(self.isspinning==False):
                self.isidle=False
        if(randomnum==1):
            self.canvas.itemconfig(self.square, fill=self.color, outline=self.color)
            self.isidle=False
            self.setToCenter()
        if(randomnum==2):
            self.isidle=False
            self.resetSize()
        if(randomnum==3):
            self.isidle=False
            self.setToCenter()
        if(randomnum==4):
            self.isidle=False
            self.change_color(self.canvas.itemconfig(self.square, "fill")[4], "#FF0000",30, 0)
    

def changeBGcolor(canvas, current_color, target_color,delay, step=1, steps=1):
    # Calculate the RGB values for the next step
    r, g, b = current_color
    r_target, g_target, b_target = target_color
    r_diff, g_diff, b_diff = r_target - r, g_target - g, b_target - b

    # Calculate the new color
    r = r + step * r_diff / steps
    g = g + step * g_diff / steps
    b = b + step * b_diff / steps

    # Convert to hexadecimal color representation
    new_color = "#{:02x}{:02x}{:02x}".format(round(r), round(g), round(b))

    # Update the canvas background color
    canvas.config(bg=new_color)

    # Check if the target color is reached, if not, schedule the next step
    if new_color != "#{:02x}{:02x}{:02x}".format(*target_color):
        canvas.after(delay, changeBGcolor, canvas, (r, g, b), target_color, delay, step, steps)

def get_rgb_values(color):
    # Convert color name or color code to RGB values
    rgb_tuple = win.winfo_rgb(color)
    # Convert RGB values from a range of 0-65535 to 0-255
    rgb = [component // 256 for component in rgb_tuple]
    return rgb

def RuninBackGrounds(n):
    global startidleinverval, timer, chooseIdle, endidleinterval
    #currentBGcolor=get_rgb_values(canvas.cget("bg"))
    #target_color=[255,255,255]
    if(n is None):
        timer=time.time()
        n=Node(canvas=canvas, x=x_center, y=y_center, size=30, color="#FF0000", SetColors=["#00FF00","#0000FF","#FFFF00", "#FF9F00", "#00FFEB","#6AFF00"])
        n.spawnNodeAnimation()
        
        
        
    if(startidleinverval==int(time.time()-timer) and n.isidle is False):
        chooseIdle = random.randint(0,4)
        #print("Starting IDle")
        n.idle(chooseIdle) 
        #n.isidle=True
        endidleinterval=random.randint(50,100)
        timer=time.time()

        #timer=time.time()

    if(endidleinterval==int(time.time()-timer) and n.isidle):
        #print(chooseIdle)
        n.reset(chooseIdle)
        #print(n.isidle)
        #n.isidle=False
        timer=time.time()
    
    canvas.after(10,lambda:RuninBackGrounds(n))
if __name__ in "__main__":
    win = tk.Tk()
    win.title("Virtual Assistant")
    canvas=tk.Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight(), background="black")
    canvas.pack()
    
    x_center = canvas.winfo_reqwidth() // 2
    y_center =  canvas.winfo_reqheight() // 2
    #print(canvas.winfo_reqwidth(),canvas.winfo_reqheight())
    #print(x_center,y_center)
    n=None
    #print(currentBGcolor)
    startidleinverval=10
    endidleinterval=random.randint(50,100)
    chooseIdle=0
    #counter=0
    timer=0
    RuninBackGrounds(n)
    #win.after(5, fadetoBlack)
    win.mainloop()


