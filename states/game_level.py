from pyray import is_key_pressed, KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, Rectangle, draw_rectangle_rec, check_collision_recs
from resources.color.colors import GRAY, BLUE

def game_level(game):
    # --- Player Input ---
    if game.player_direction is None:
        if is_key_pressed(KEY_RIGHT):
            game.player_direction = "right"
        elif is_key_pressed(KEY_LEFT):
            game.player_direction = "left"
        elif is_key_pressed(KEY_DOWN):
            game.player_direction = "down"
        elif is_key_pressed(KEY_UP):
            game.player_direction = "up"

    # --- Player Movement ---
    if game.player_direction:
        next_pos = Rectangle(game.player_rect.x, game.player_rect.y, game.player_rect.width, game.player_rect.height)
        if game.player_direction == "right":
            next_pos.x += game.player_speed
        elif game.player_direction == "left":
            next_pos.x -= game.player_speed
        elif game.player_direction == "down":
            next_pos.y += game.player_speed
        elif game.player_direction == "up":
            next_pos.y -= game.player_speed

        collision = False
        for wall in game.wall_rects:
            if check_collision_recs(next_pos, wall):
                collision = True
                break
        
        if not collision:
            game.player_rect = next_pos
        else:
            game.player_direction = None

    # --- Drawing ---
    for wall in game.wall_rects:
        draw_rectangle_rec(wall, GRAY)

    draw_rectangle_rec(game.player_rect, BLUE)
