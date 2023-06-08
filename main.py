import pygame,sys,pymunk #imports



pygame.display.set_caption('Apple Physics Simulator')
Icon = pygame.image.load('red_apple.png')
pygame.display.set_icon(Icon)



def create_apple(space, pos): #the properties for the apples
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape #to generate the shape


def draw_apples(apples): #to generate and draw the apples
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(apple_surface, apple_rect)


    '''
    The arguments consist of:
    - Mass (weight);
    - Inertia (resistance to movement);
    - body_type (what body type we want, ex: STATIC, DYNAMIC, KINEMATIC)
     ''' 


def static_ball(space, pos): #the properties for the static balls
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape #to generate the shape


def draw_static_ball(balls): #to generate and draw the static balls
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        ball_circle = static_ball_surface.get_rect(center = (pos_x, pos_y))
        screen.blit(static_ball_surface, ball_circle)


pygame.init()
screen = pygame.display.set_mode((800, 800)) #display surface
clock = pygame.time.Clock() #game clock
space = pymunk.Space() #The physics, which is already pre-made by Pymunk
space.gravity = (0, 300) #the strength in which the apple falls
apple_surface = pygame.image.load('red_apple.png')
static_ball_surface = pygame.image.load('orang_circle.png')

apples = [] #list for creating apples

balls = [] #list for creating the colliders (balls)


while True: #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

        if event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()

            if (left):
                apples.append(create_apple(space, event.pos)) #if LMB DOWN then, it will add "apples" to a list which draws the appple
            elif(middle):
                print("MIDKEY")
            elif(right):
                balls.append(static_ball(space, event.pos)) #if RMB DOWN then, it will ad "balls" to a list which draws the balls

                '''

                used to detect which type of "MOUSEBUTTONDOWN" is clicked

                '''
    

    screen.fill((227, 227, 227)) #background color
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50) #To update the Pymunk while Pygame is updating
    pygame.display.update()
    clock.tick(120) #FPS = 120