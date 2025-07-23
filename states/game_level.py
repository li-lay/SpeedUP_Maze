from pyray import (
    KEY_DOWN,
    KEY_LEFT,
    KEY_RIGHT,
    KEY_UP,
    KeyboardKey,
    Rectangle,
    check_collision_recs,
    draw_rectangle_rec,
    draw_texture_rec,
    is_key_pressed,
    play_sound,
    set_sound_volume,
)

from resources.color.colors import BLUE, GRAY, WHITE


def game_level(game, jump_sound, world_tileset):
    set_sound_volume(jump_sound, 0.5)
    # --- Player Input ---
    if game.player_direction is None:
        if is_key_pressed(KEY_RIGHT) or is_key_pressed(KeyboardKey(76)):
            game.player_direction = "right"
            play_sound(jump_sound)
        elif is_key_pressed(KEY_LEFT) or is_key_pressed(KeyboardKey(72)):
            game.player_direction = "left"
            play_sound(jump_sound)
        elif is_key_pressed(KEY_DOWN) or is_key_pressed(KeyboardKey(74)):
            game.player_direction = "down"
            play_sound(jump_sound)
        elif is_key_pressed(KEY_UP) or is_key_pressed(KeyboardKey(75)):
            game.player_direction = "up"
            play_sound(jump_sound)

    # --- Player Movement ---
    if game.player_direction:
        next_pos = Rectangle(
            game.player_rect.x,
            game.player_rect.y,
            game.player_rect.width,
            game.player_rect.height,
        )
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
    source_rec = Rectangle(0, 0, 40, 40)  # Assuming a 40x40 tile from the tileset
    for wall in game.wall_rects:
        draw_texture_rec(world_tileset, source_rec, wall.x, wall.y)

    draw_rectangle_rec(game.player_rect, BLUE)
