import pgzrun
import random

WIDTH = 512
HEIGHT = 512

# titlescreen
titlescreen = Actor('title-screen')
titlescreen.pos =(256, 256)

title = Actor("title")
title.pos = (248, 65)

game_state = 'title_screen'
menu_options = ["Start", "Sound On", "Quit"]
selected_option = 0  # 0 = Start, 1 = Sound On
sound_enabled = True

#game_over screen
game_over_title = Actor('game-over-title')
game_over_title.pos = (256, 80)

game_over_retry = ("Retry!")
game_over_message = ("Too greedy to be rich!")

#game_win screen
game_win_title = Actor('win-title')
game_win_title.pos = (248, 65)

# stage
background = Actor("background")
background.pos = (256, 256)

ground = Actor("ground", anchor=('center', 'top'))
ground.pos = (256, 352)

platform1 = Actor("platform1")
platform1.pos = (325, 310)

platform2 = Actor("platform2")
platform2.pos = (190, 280)

life_positions = [(136, 136), (152, 136), (168, 136)]
lives = [Actor("life", pos=pos) for pos in life_positions]

coin = Actor("coin")
coin.pos = (242, 210)

# player
player = Actor("knight-idle-1", anchor=('center', 'bottom'))
player.pos = (180, 280)
player_idle_frames = ["knight-idle-1", "knight-idle-2", "knight-idle-3", "knight-idle-4"]
player_run_frames = ["knight-run-1", "knight-run-2", "knight-run-3", "knight-run-4", "knight-run-5", "knight-run-6", "knight-run-7", "knight-run-8"]
player_idle_left_frames = ["knight-idle-left-1", "knight-idle-left-2", "knight-idle-left-3", "knight-idle-left-4"]
player_run_left_frames = ["knight-run-left-1", "knight-run-left-2", "knight-run-left-3", "knight-run-left-4", "knight-run-left-5", "knight-run-left-6", "knight-run-left-7", "knight-run-left-8"]
player_lives = 3

# enemy
enemy = Actor("slime-1")
enemy.pos = (330, 345)
enemy_frames = ["slime-1", "slime-2", "slime-3", "slime-4", "slime-5", "slime-6"]
enemy_frame = 0

enemyb = Actor("slime-1")
enemyb.pos = (190, 265)
enemyb_frames = ["slime-1", "slime-2", "slime-3", "slime-4", "slime-5", "slime-6"]
enemyb_frame = 0

# animation
current_frame = 0
animation_speed = 0.1
frame_timer = 0
enemy_frame_timer = 0
enemy_animation_speed = 0.15

# movement speed & jump settings
player_speed = 2
jump_speed = 7
gravity = 0.8
vertical_velocity = 0
is_jumping = False
on_ground = False
facing_left = False

player_state = 'idle'  # 'idle' ou 'run'

#enemy moviment
enemy_speed = 2
enemy_offset_x = 0

can_check_collision = True
can_check_input = True

#setups
def setup_playing():
    global current_frame, frame_timer, is_jumping, vertical_velocity, on_ground, player_state, facing_left, enemy_frame 
    global enemy_frame_timer, player_lives, can_check_collision, game_state, sound_enabled, lives, player, enemy

    screen.clear()
    # stage
    background = Actor("background")
    background.pos = (256, 256)

    ground = Actor("ground", anchor=('center', 'top'))
    ground.pos = (256, 352)

    platform1 = Actor("platform1")
    platform1.pos = (325, 310)

    platform2 = Actor("platform2")
    platform2.pos = (190, 280)

    life_positions = [(136, 136), (152, 136), (168, 136)]
    lives = [Actor("life", pos=pos) for pos in life_positions]

    coin = Actor("coin")
    coin.pos = (242, 210)

    # player
    player = Actor("knight-idle-1", anchor=('center', 'bottom'))
    player.pos = (180, 345)
    player_idle_frames = ["knight-idle-1", "knight-idle-2", "knight-idle-3", "knight-idle-4"]
    player_run_frames = ["knight-run-1", "knight-run-2", "knight-run-3", "knight-run-4", "knight-run-5", "knight-run-6", "knight-run-7", "knight-run-8"]
    player_idle_left_frames = ["knight-idle-left-1", "knight-idle-left-2", "knight-idle-left-3", "knight-idle-left-4"]
    player_run_left_frames = ["knight-run-left-1", "knight-run-left-2", "knight-run-left-3", "knight-run-left-4", "knight-run-left-5", "knight-run-left-6", "knight-run-left-7", "knight-run-left-8"]
    player_lives = 3

    # enemies
    enemy = Actor("slime-1")
    enemy.pos = (330, 345)
    enemy_frames = ["slime-1", "slime-2", "slime-3", "slime-4", "slime-5", "slime-6"]
    enemy_frame = 0

    enemyb = Actor("slime-1")
    enemyb.pos = (190, 265)
    enemyb_frames = ["slime-1", "slime-2", "slime-3", "slime-4", "slime-5", "slime-6"]
    enemyb_frame = 0

    # animation
    current_frame = 0
    animation_speed = 0.1
    frame_timer = 0
    enemy_frame_timer = 0
    enemy_animation_speed = 0.15

    # movement speed & jump settings
    player_speed = 2
    jump_speed = 7
    gravity = 0.8
    vertical_velocity = 0
    is_jumping = False
    on_ground = False
    facing_left = False

    player_state = 'idle'  # 'idle' ou 'run'

    #enemy moviment
    enemy_speed = 2
    enemy_offset_x = 0

    can_check_collision = True

    game_state = 'playing'
    if sound_enabled == True:
        music.play('first-stage')

def setup_title_screen():
    global selected_option, sound_enabled, game_state, menu_options
    block_input(time = 2.0)
    screen.clear()

    titlescreen = Actor('title-screen')
    titlescreen.pos =(256, 256)

    title = Actor("title")
    title.pos = (248, 65)

    game_state = 'title_screen'
    menu_options = ["Start", "Sound On", "Quit"]
    selected_option = 0  # 0 = Start, 1 = Sound On

    if sound_enabled == True:
        music.play('main-theme')

def setup_game_over():
    global game_over_title, selected_option, sound_enabled, game_state, game_over_retry, game_over_message
    block_input(time = 2.0)
    screen.clear()

    game_over_title = Actor('game-over-title')
    game_over_title.pos = (256, 80)

    game_over_retry = ("Retry!")
    game_over_message = ("Too greedy to be rich!")

    game_state = 'game_over'
    if sound_enabled == True:
        music.play('game-over')

def setup_game_win():
    global game_win_title, game_state
    block_input(time = 2.0)
    screen.clear()

    game_win_title = Actor('win-title')
    game_win_title.pos = (248, 65)

    game_state = 'game_win'
    if sound_enabled == True:
        music.play('main-theme')

#updates
def update():  
    if game_state == 'title_screen':
        update_title_screen()        
    elif game_state == 'playing':
        update_playing()
    elif game_state == 'game_over':
        update_game_over()
    elif game_state == 'game_win':
        update_game_win()
    else:
        update_title_screen()
        
def update_title_screen():
    global selected_option, sound_enabled

    # Navigate menu with arrow keys
    if keyboard.down and can_check_input:
        block_input()
        selected_option = (selected_option + 1) % len(menu_options)
    elif keyboard.up and can_check_input:
        block_input()
        selected_option = (selected_option - 1) % len(menu_options)

    # Select an option with space or enter
    if (keyboard.space or keyboard.RETURN) and can_check_input:
        block_input()
        if selected_option == 0:  # Start
        #    game_state = "playing"
            setup_playing()
        elif selected_option == 1:  # Toggle sound
            sound_enabled = not sound_enabled
            menu_options[1] = "Sound On" if sound_enabled else "Sound Off"

            if sound_enabled:
                music.play('main-theme')
            else:
                music.stop()
        elif selected_option == 2: #quit gam
            quit()

def update_game_over():
    # Check for retry input
    if (keyboard.space or keyboard.RETURN) and can_check_input:
        block_input(time = 1.5)
        setup_title_screen()

def update_game_win():
    # Check for retry input
    if (keyboard.space or keyboard.RETURN) and can_check_input:
        block_input(time = 1.5)
        setup_title_screen()   

def update_playing():
    global current_frame, frame_timer, is_jumping, vertical_velocity, on_ground, player_state, facing_left, enemy_frame 
    global enemy_frame_timer, player_lives, can_check_collision, game_state, enemyb_frame

    #moved = False

    # Left and right movement
    if keyboard.left and player.left > 128:
        #A = A - B
        player.x -= player_speed
        facing_left = True
        player_state = 'run'
        #moved = True
    elif keyboard.right and player.right < 384:
        player.x += player_speed
        facing_left = False
        player_state = 'run'
        #moved = True
    else:
        player_state = 'idle'

    # Jumping logic
    if not is_jumping and keyboard.space:
        is_jumping = True
        vertical_velocity = -jump_speed
        if sound_enabled == True:
            sounds.jump.play()

    if is_jumping:
        player.y += vertical_velocity
        vertical_velocity += gravity

        if player.y >= HEIGHT - 10:
            player.y = HEIGHT - 10
            is_jumping = False
    
    if not is_jumping:
        vertical_velocity += 1
    
    if not is_jumping and not on_ground:
        on_ground = check_collision()

    on_ground = check_collision()
    player.y += vertical_velocity

    # Update player animation
    frame_timer += animation_speed
    if frame_timer >= 1:
        frame_timer = 0
        if facing_left:
            frames = player_run_left_frames if player_state == 'run' else player_idle_left_frames
        else:
            frames = player_run_frames if player_state == 'run' else player_idle_frames
        current_frame = (current_frame + 1) % len(frames)
        player.image = frames[current_frame]

    # Update enemy animation
    enemy_frame_timer += enemy_animation_speed
    if enemy_frame_timer >= 1:
        enemy_frame_timer = 0
        enemy_frame = (enemy_frame + 1) % len(enemy_frames)
        enemy.image = enemy_frames[enemy_frame]
        enemyb_frame = (enemy_frame + 1) % len(enemy_frames)
        enemyb.image = enemy_frames[enemy_frame]
        
    
    #enemy moviment
    move_enemy()
    
     # Verificar colisão entre enemy e player
    if can_check_collision and (enemy.colliderect(player) or enemyb.colliderect(player)) and player_lives > 0:
        player_lives -= 1
        if lives:
            lives.pop()  # Remove um sprite de vida
        if sound_enabled == True:
            sounds.hurt.play()
        can_check_collision = False  # Desativa a detecção de colisão temporariamente
        clock.schedule_unique(enable_collision, 1.0)  # Reativa após 1 segundo
 
    if player_lives == 0:
        if sound_enabled == True:
            sounds.explosion.play()        
        setup_game_over()
    
    # Verificar colisao entre coin e player
    if player.colliderect(coin) and player_lives > 0:
        if sound_enabled == True:
            sounds.coin.play()
        setup_game_win()
        
def enable_collision():
    # Reativa a detecção de colisão após 1 segundo
    global can_check_collision
    can_check_collision = True

def check_collision():
    global is_jumping, vertical_velocity

    platforms = [ground, platform1, platform2]
    on_ground = False

    for platform in platforms:
        # Verifica colisão apenas se o jogador está caindo
        if player.colliderect(platform) and vertical_velocity >= 0:
            # Garante que o jogador está vindo de cima da plataforma
            if player.y < platform.y:
                # Ajuste: posiciona o jogador 16 pixels acima da plataforma
                player.y = platform.y - 8
                vertical_velocity = 1
                is_jumping = False
                on_ground = True
                break

    # Verificação de colisão com o chão (ajuste para player.y = 365)
    if not on_ground and player.y >= ground.y:
        player.y = ground.y
        vertical_velocity = 0
        is_jumping = False
        on_ground = True

    return on_ground

def move_enemy():
    global enemyb_direction, enemy_direction

    # Initialize enemyb direction if not set
    if 'enemyb_direction' not in globals():
        enemyb_direction = 1  # 1 means moving right, -1 means moving left

    # Initialize enemy direction if not set
    if 'enemy_direction' not in globals():
        enemy_direction = -1  # -1 means moving left, 1 means moving right

    # Define movement boundaries for enemy
    start_x = 136
    end_x = 378
    speed = 1  # Slow movement speed for enemy

    # Update enemy's position
    enemy.x += speed * enemy_direction

    # Reverse direction if boundaries are hit for enemy
    if enemy.x >= end_x and enemy_direction == 1:
        enemy_direction = -1
    elif enemy.x <= start_x and enemy_direction == -1:
        enemy_direction = 1

    # Define movement boundaries for enemyb
    start_x_b = 167
    end_x_b = 214
    speed_b = 1  # Slow movement speed for enemyb

    # Update enemyb's position
    enemyb.x += speed_b * enemyb_direction

    # Reverse direction if boundaries are hit for enemyb
    if enemyb.x >= end_x_b and enemyb_direction == 1:
        enemyb_direction = -1
    elif enemyb.x <= start_x_b and enemyb_direction == -1:
        enemyb_direction = 1

def block_input(time = 0.2):
    global can_check_input

    can_check_input = False
    clock.schedule(enable_input, time)

def enable_input():
    global can_check_input
    can_check_input = True

def draw():
    if game_state == 'title_screen':
        draw_title()
    if game_state == 'playing':
        draw_playing()
    if game_state == 'game_over':
        draw_game_over()
    if game_state == 'game_win':
        draw_game_win()

def draw_title():
    screen.clear()
    titlescreen.draw()
    title.draw()

    # Draw menu options
    for i, option in enumerate(menu_options):
        color = "yellow" if i == selected_option else "black"
        screen.draw.text(
            option,
            (WIDTH // 2 - 80, 200 + i * 30),
            fontsize=18,
            color=color,
            fontname='pixeloperator8-bold.ttf',
            shadow=(4.0,4.0)
        )
    
def draw_playing():
    screen.clear()
    titlescreen.draw()
    background.draw()
    ground.draw()
    platform1.draw()
    platform2.draw()
    player.draw()
    enemy.draw()
    enemyb.draw()
    coin.draw()
    for life in lives:
        life.draw()

def draw_game_over():
    screen.clear()
    titlescreen.draw()
    game_over_title.draw()
    screen.draw.text(
            game_over_retry,
            (WIDTH // 2 - 60, 370),
            fontsize=22,
            color="yellow",
            fontname='pixeloperator8-bold.ttf',
            shadow=(4.0,4.0)
        )
    screen.draw.text(
            game_over_message,
            (WIDTH // 2 - 110, 420),
            fontsize=12,
            color="yellow",
            fontname='pixeloperator8-bold.ttf',
            shadow=(4.0,4.0)
        )

def draw_game_win():
    screen.clear()
    titlescreen.draw()
    game_win_title.draw()

pgzrun.go()
