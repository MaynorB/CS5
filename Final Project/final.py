Web VPython 3.2
# billiards.py
#https://www.glowscript.org/#/user/eambrizlazo/folder/MyPrograms/program/billiards.py

scene.bind('keyup', keyup_fun)     # Function for key presses
scene.background = 0.8*vec(84/255, 55/255, 134/255)
scene.title = "BILLIARDS"
scene.width = 960                     # Make the 3D canvas larger
scene.height = 480
scene.caption = "Press SPACE to shoot, R to reset cue ball, Use camera, Change Strength >"
scene.camera.pos = vec(0,8,-16)
scene.camera.axis = vec(0,-6,6)
def S(s):
    print("Strength of shot is", s.value)
    return s.value
s = slider( bind=S, min = 5, max =35, step = 1)
scene.append_to_caption('\n\n')
# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"

        
lamp = local_light(pos=vector(0,10,10),
                      color=color.yellow)
        
lamp = local_light(pos=vector(0,-10,10),
                      color=color.red)
            
cue_stick = cylinder(texture = textures.wood,
            pos = vec(12, 0, -9),
            axis = vec(0, 0, 1),
            size = vec(16, .5,.5),
            color = vec(207/255, 191/255, 181/255)   
            )
cue_stick2 = cylinder(texture = textures.wood,
            pos = vec(14, 0, -9),
            axis = vec(0, 0, 1),
            size = vec(16, .5,.5),
            color = vec(227/255, 211/255, 201/255)   
            )


ground = box(texture={'file':textures.rough,
        'bumpmap':bumpmaps.rough}, size = vec(18, 1, 36),
             pos = vec(0, -1, 0),
             color = vec(39/255,107/255,64/255))
             
pocketA =cylinder(pos = vec(-9, -0.999999, -18),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)
            
pocketB =cylinder(pos = vec(-9, -0.999999, 0),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)
            
pocketC =cylinder(pos = vec(-9, -0.99999, 18),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)
            
pocketD =cylinder(pos = vec(9, -0.99999999, -18),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)
            
pocketE =cylinder(pos = vec(9, -0.99, 0),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)

pocketF =cylinder(pos = vec(9, -0.99, 18),
            axis = vec(0, 1, 0),
            radius = 1.5,
            color = color.black)

# Create six walls, also boxes
#
wallA = box(texture = textures.wood,
            pos = vec(0, -1, 18),
            axis = vec(1, 0, 0),
            size = vec(16, 2, 1),
            color = vec(77/255, 51/255, 41/255)   
            )
wallB = box(texture = textures.wood,
            pos = vec(9, -1, -9),
            axis = vec(0, 0, 1),
            size = vec(15, 2, 1),
            color = vec(77/255, 51/255, 41/255)      
            )
            
wallC = box(texture = textures.wood,
            pos = vec(9, -1, 9),
            axis = vec(0, 0, 1),
            size = vec(15, 2, 1),
            color = vec(77/255, 51/255, 41/255)    
            )
wallD = box(texture = textures.wood,
            pos = vec(-9, -1, 9),
            axis = vec(0, 0, 1),
            size = vec(16, 2, 1),
            color = vec(77/255, 51/255, 41/255)   
            )
wallE = box(texture = textures.wood,
            pos = vec(-9, -1, -9),
            axis = vec(0, 0, 1),
            size = vec(15, 2, 1),
            color = vec(77/255, 51/255, 41/255)      
            )
            
wallF = box(texture = textures.wood,
            pos = vec(0, -1, -18),
            axis = vec(1, 0, 0),
            size = vec(15, 2, 1),
            color = vec(77/255, 51/255, 41/255)   
            )

# Create a ball that we will be able to control

def make_ball(ball_number, ball_color, stripe, starting_position, starting_vel):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vec(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    ball_body = sphere(size =vec(1,1,1),
                        pos = vec(0,0,0),
                        color = ball_color
                        )
    circle = sphere(size = 0.7*vec(1,1,1),
                        pos = vec(0,0,.2),
                        color = color.white
                        )
    
    number = text(pos = vec(-0.15,0,.5),
                        height = 0.25,
                        text = ball_number,
                        color = color.black
                        )
    if stripe == True:
        stripe = ring(axis = vec(0,1,0),
                        pos = vec(0,0,0),
                        radius = 0.2,
                        thickness = 0.32,
                        color = ball_color)
                        
        ball_body.color = color.white
    else:
        stripe = sphere(size = 0.1*vec(1,1,1))

    # Make a list to "fuse" with a compound
    #
    ball_objects = [ball_body, circle, number, stripe]

    # Now, we create a compound--we'll name it com_alien:
    #
    com_ball = compound(ball_objects,
                         pos = starting_position
                         )
    com_ball.vel = starting_vel    # Set the initial velocity
    return com_ball
#
cue_ball = sphere(size = vec(1, 1, 1),
                  pos = vec(0, 0, -8),
                  color = color.white
                  )
cue_ball.vel = vec(0, 0, 0)

#SOLIDS

solidBallOne = make_ball(ball_number = 1, ball_color = color.orange, 
                starting_position = vec(0, 0, -1), starting_vel = vec(0, 0, 0))
                
solidBallTwo = make_ball(ball_number = 2, ball_color = color.blue, 
                starting_position = vec(2, 0, 3), starting_vel = vec(0, 0, 0))

solidBallThree = make_ball(ball_number = 3, ball_color = color.red, 
                starting_position = vec(-1.5, 0, 2), starting_vel = vec(0, 0, 0))
                
solidBallFour = make_ball(ball_number = 4, ball_color = color.purple, 
                starting_position = vec(-1, 0, 1), starting_vel = vec(0, 0, 0))
                
solidBallFive = make_ball(ball_number = 5, ball_color = vec(1, 140/255, 0), 
                starting_position = vec(1, 0, 1), starting_vel = vec(0, 0, 0))
            
solidBallSix = make_ball(ball_number = 6, ball_color = vec(1/255, 50/255, 32/255), 
                starting_position = vec(1, 0, 3), starting_vel = vec(0, 0, 0))
                
solidBallSeven = make_ball(ball_number = 7, ball_color = vec(128/255, 0, 0), 
                starting_position = vec(-0.5, 0, 2), starting_vel = vec(0, 0, 0))
                
solidBallEight = make_ball(ball_number = 8, ball_color = color.black, 
                starting_position = vec(0, 0, 1), starting_vel = vec(0, 0, 0))
                
#STRIPES
                
stripedBallNine = make_ball(ball_number = 9, ball_color = color.orange, stripe = True, 
                starting_position = vec(0.5, 0, 2), starting_vel = vec(0, 0, 0))
                
stripedBallTen = make_ball(ball_number = 10, ball_color = color.blue, stripe = True, 
                starting_position = vec(-2, 0, 3), starting_vel = vec(0, 0, 0))
                
stripedBallEleven = make_ball(ball_number = 11, ball_color = color.red, stripe = True, 
                starting_position = vec(-1, 0, 3), starting_vel = vec(0, 0, 0))

stripedBallTwelve = make_ball(ball_number = 12, ball_color = color.purple, stripe = True, 
                starting_position = vec(0, 0, 3), starting_vel = vec(0, 0, 0))

stripedBallThirteen = make_ball(ball_number = 13, ball_color = vec(1, 140/255, 0), stripe = True, 
                starting_position = vec(1.5, 0, 2), starting_vel = vec(0, 0, 0))
                
stripedBallFourteen = make_ball(ball_number = 14, ball_color = vec(1/255, 50/255, 32/255), stripe = True, 
                starting_position = vec(0.5, 0, 0), starting_vel = vec(0, 0, 0))

stripedBallFifteen = make_ball(ball_number = 15, ball_color = vec(128/255, 0, 0), stripe = True, 
                starting_position = vec(-0.5, 0, 0), starting_vel = vec(0, 0, 0))
            
listOfBalls = [cue_ball, solidBallOne, solidBallTwo, solidBallThree, solidBallFour, solidBallFive, solidBallSix, solidBallSeven, solidBallEight, stripedBallNine, stripedBallTen,
stripedBallEleven, stripedBallTwelve, stripedBallThirteen, stripedBallFourteen, stripedBallFifteen]

solidBalls = [solidBallOne, solidBallTwo, solidBallThree, solidBallFour, solidBallFive, solidBallSix, solidBallSeven]
stripedBalls=[stripedBallNine, stripedBallTen,stripedBallEleven, stripedBallTwelve, stripedBallThirteen, stripedBallFourteen, stripedBallFifteen]
eight_ball = [solidBallEight]

solidBallsScored = []
stripedBallsScored = []
eight_ballScored = []
# +++ end of OBJECT_CREATION section
# +++ start of ANIMATION section

# Other constants
#
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.camera.follow(cue_ball)
# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt

#

solid_win = False
stripe_win = False
game_run = True
while game_run:

    rate(RATE)                              # Maximum number of times per second
                                            # ..that the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step
    
    for b in listOfBalls:
        b.pos = b.pos + b.vel*dt 
        b.vel = b.vel * 0.99


    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!
    
# +++ Start of COLLISIONS -- check for collisions & do the "right" thing

    for i1 in range(0, len(listOfBalls)):
        b1 = listOfBalls[i1]
        for i2 in range(i1+1, len(listOfBalls)):
            b2 = listOfBalls[i2]
            collided = spheres_collide( b1, b2 )      # check for sphere collisions!
        
    for b in listOfBalls:
        corral_collide(b)   # check for walls!
    
    for b in listOfBalls:
        stopBall(b)

    for b in listOfBalls[1:]:
        pocketFall(b, vec(0, -2, 0))
    
    pocketFall(listOfBalls[0], vec(0, 0, -8))

    for solid in solidBalls:
        if solid.pos.y < 0:
            solidBallsScored.append(solid)
            solidBalls.remove(solid)
            print("Solids has now scored", len(solidBallsScored))
            
    for stripe in stripedBalls:
        if stripe.pos.y < 0:
            stripedBallsScored.append(stripe)
            stripedBalls.remove(stripe)
            print("Stripes has now scored", len(stripedBallsScored))
            
    if eight_ball[0].pos.y < 0:
        eight_ballScored.append(eight_ball[0])
        
    if len(solidBallsScored) == 7 and len(eight_ballScored) == 1:
        solid_win = True
        game_run = False
        
    if len(stripedBallsScored) == 7 and len(eight_ballScored) == 1:
        stripe_win = True
        game_run = False
        
if solid_win:
    print("SOLIDS WINS")
if stripe_win:
    print("STRIPES WIN")

    # +++ End of COLLISIONS
# +++ Start of EVENT-HANDLING section--separate functions for
#                                keypresses

def keyup_fun(event):
    """ function called with each key pressed """
    key = chr(event.which)
    b = listOfBalls[0]          # let b be the initial object in LoB
    shot = norm(vec(scene.forward.x,0,scene.forward.z))
    shot.mag = s.value  # "strength" of keypress
    if b.vel = vec(0, 0, 0):
        if key in " ":
            b.vel = b.vel + shot #Shoot with forward direction and determined magnitude
        if key in "Rr":
            b.pos = vec(0,0,-8)

# +++ End of EVENT-HANDLING section
# +++ Other functions can go here...

def stopBall(ball):
    if abs(ball.vel.x) < 0.2 and abs(ball.vel.z) < 0.2:
        ball.vel = vec(0,0,0)

def spheres_collide( sphere1, sphere2 ):
    """ takes two inputs, sphere1 and sphere2
        (1) checks for a collision (centers within DISTANCE of each other)
        (2) if colliding,
            (2a) undo the last time step's motion
            (2b) compute the new velocities of the two spheres
            (2c) assign those new velocities
        (3) returns True if they collided; False otherwise
        both sphere1 and sphere2 need a .pos field and a .vel field!
    """
    DISTANCE = 1.0   # collision-check distance
    s1 = sphere1
    s2 = sphere2  # simpler!
    diff = s1.pos - s2.pos  # vector between the two
    if mag( diff ) < DISTANCE:
        # vector perpendicular to the diff vector
        dtan = rotate( diff, radians(90), vector(0,1,0))
        # get the two velocities
        v1 = s1.vel; v2 = s2.vel
        # undo the last time step
        s1.pos -= v1*dt; s2.pos -= v2*dt
        # find the radial and tangent parts of each 
        v1_rad = proj(v1, diff); v1_tan = proj(v1, dtan)
        v2_rad = proj(v2, -diff); v2_tan = proj(v2, dtan)
        # swap the radials and keep the tangents
        s1.vel =  v2_rad + v1_tan
        s2.vel =  v1_rad + v2_tan
        return True   # did collide
    else:
        return False  # did not collide
        
def corral_collide( ball ):
    """ corral collisions! 
            ball must have a .vel field and a .pos field
    """
    # if the ball hits wallA
    if ball.pos.z > wallA.pos.z: # hit - check for z
        ball.pos.z = wallA.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity
        
    if ball.pos.z < wallF.pos.z: # hit - check for z
        ball.pos.z = wallF.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity


    # if the ball hits wallB
    if ball.pos.x > wallB.pos.x: # hit - check for x
        ball.pos.x = wallB.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
        
    # if the ball hits wallF
    if ball.pos.x > wallC.pos.x: # hit - check for z
        ball.pos.x = wallF.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the z velocity

    # if the ball hits wallG
    if ball.pos.x < wallD.pos.x: # hit - check for x
        ball.pos.x = wallD.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
        
    if ball.pos.x < wallE.pos.x: # hit - check for x
        ball.pos.x = wallE.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity

def pocketFall(ball, tp):
    """Detects if an object ball is within one of the 6 boundaries of pockets and positions it at the bottom of the board
    """
#PocketA
    if ball.pos.x <= -7 and ball.pos.z <= -16:
        ball.pos = tp
        ball.vel = vec(0, 0, 0)
#PocketB
    if ball.pos.x <= -7 and -0.5<ball.pos.z<0.5: 
        ball.pos = tp
        ball.vel = vec(0, 0, 0)  
#PocketC
    if ball.pos.x <= -7 and ball.pos.z >= 16: 
        ball.pos = tp 
        ball.vel = vec(0, 0, 0) 
#PocketD
    if ball.pos.x >= 7 and ball.pos.z <= -16: # hit - check for z
        ball.pos = tp
        ball.vel = vec(0, 0, 0)        # reverse the z velocity
#PocketE
    if ball.pos.x >= 7 and -0.5<ball.pos.z<0.5: # hit - check for z
        ball.pos = tp
        ball.vel = vec(0, 0, 0)        # reverse the z velocity
#PocketF
    if ball.pos.x >= 7 and ball.pos.z >= 16: # hit - check for z
        ball.pos = tp
        ball.vel = vec(0, 0, 0)        # reverse the z velocity
    