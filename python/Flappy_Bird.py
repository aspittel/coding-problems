
#Ali Spittel
#Final Lab
#based on flappy birds
#also based loosly on pizza panic lab
#OPEN LAUNCHSCREEN FIRST

#Import needed programs and initialize screen
from livewires import games, color
import random
games.init(screen_width=640, screen_height = 600, fps = 100)

#create an animated bird with three different wing positions. Repeats indefinitely
#found images online and then edited them to make them change

class Bird(games.Animation):
    images = ["Bird1.png",
              "Bird2.png",
              "Bird3.png"]
    def __init__(self):
        super(Bird,self).__init__(images = Bird.images,
                                  x = 300,
                                  y = 300,
                                  dy = 7,
                                  n_repeats = 0,
                                  repeat_interval = 8
                                   )
        self.score = games.Text(value = 0, size = 100, color = color.red,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        #various sounds that come on at various points when interaction occurs
        self.chirp = games.load_sound("Bird.Chirp.mp3")
        self.crash = games.load_sound("swisher.mp3")
        self.ding = games.load_sound("coin.mp3")
        self.time = 2
        self.message = None
    #update bird to fly up or down depending on up or down arrow
    def update(self):
        if games.keyboard.is_pressed(games.K_UP):
            self.dy = -7
            self.chirp.play()
        elif games.keyboard.is_pressed(games.K_DOWN):
            self.dy = 7
            self.chirp.play()
        self.new_score()

    #get points for staying alive
    def new_score(self):
        if self.time == 0:
            self.score.value += 1
            self.time +=2
        else:
            self.time-=1
        self.die_bird()

    #if the bird goes off screen, the bird stops existing
    #and the game goes to the game over screen    
    def die_bird(self):
        if self.top < 0 or self.top > 800:
            self.crash.play()
            self.destroy()
            self.end_message()
        self.die_again_bird()

    #if bird crashes into ground or into a tube it also dies    
    def die_again_bird(self):        
        for bird in self.overlapping_sprites:
            self.crash.play()
            self.destroy()
            self.end_message()
    #change the end message depending on how well the player does
    def end_message(self):
        if int(self.score.value) >= 100:
            self.message = "Amazing Job! Score:  "+ str(self.score.value)
        elif 100>int(self.score.value)>=50:
            self.message = "Good Job! Score: " + str(self.score.value)
        elif 50 >int(self.score.value)>= 25:
            self.message = "You are getting closer! Score:  " + str(self.score.value)
        else:
            self.message = "Try again! Score:  " + str(self.score.value)
        self.end_game()

    #if die; end message and close the screen
    def end_game(self):
        end_message = games.Message(value = self.message,
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 1 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


# create a moving screen bottom that endlessly rotates so it looks like the whole screen is moving
class Screen_Bottom(games.Sprite):
    image = games.load_image("grass.jpeg")
    def __init__(self,x):
        super(Screen_Bottom, self).__init__(image = Screen_Bottom.image,
                                            bottom = games.screen.height,
                                            x = x,
                                            dx = -4)
    #move the bottom
    def update(self):
        if self.right < 0:
            self.left = 640

#create endless tubes once one goes off screen, also make it rotate at same pace as ground
class Tube(games.Sprite):
    image = games.load_image("tube.jpeg")
    def __init__(self, top):
        super(Tube, self).__init__(image = Tube.image,
                                   top = top,
                                   x = 640,
                                   dx = -4)
        
    #delete the tube once it goes off screen
    #increase score if bird gets past the tube
    def update(self):
        if self.right < 0:
            self.destroy()
            New_Tube()
        
#create the tube with a random height so that
#outside class so its easier to create and add a new one
def New_Tube():
    y_var = random.randrange(300, 550)
    tube = Tube(top = y_var)
    games.screen.add(tube)
    
        
def main():
    #add a background of clouds
    background = games.load_image("cloud.jpeg", transparent = False)
    games.screen.background = background

    #add the bird
    bird = Bird()
    games.screen.add(bird)

    #add four grasses that overlap so that there aren't any gaps.
    grass = Screen_Bottom(x = 0)
    games.screen.add(grass)
    grass1 = Screen_Bottom(x = 200)
    games.screen.add(grass1)
    grass2 = Screen_Bottom(x = 500)
    games.screen.add(grass2)
    grass3 = Screen_Bottom(x = 800)
    games.screen.add(grass3)

    #add the initial tube with a random height
    tube = Tube(top = random.randrange(300,550))
    games.screen.add(tube)

    #kick it off!
    games.mouse.is_visible = True
    games.screen.event_grab = True
    games.screen.mainloop()

main()
