from pyray import is_key_pressed, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, KEY_ESCAPE, KEY_ENTER, draw_text, measure_text, draw_rectangle_rec, draw_rectangle_lines_ex, check_collision_point_rec, get_mouse_position, is_mouse_button_pressed, MOUSE_LEFT_BUTTON
from resources.color.colors import BLACK, WHITE, GRAY, BLUE, RED, YELLOW

def level_selection(game):
    # --- Input --- #
    if is_key_pressed(KEY_RIGHT):
        game.selected_level = (game.selected_level + 1) % 10
    if is_key_pressed(KEY_LEFT):
        game.selected_level = (game.selected_level - 1 + 10) % 10
    if is_key_pressed(KEY_DOWN):
        game.selected_level = (game.selected_level + 5) % 10
    if is_key_pressed(KEY_UP):
        game.selected_level = (game.selected_level - 5 + 10) % 10
    if is_key_pressed(KEY_ESCAPE):
        game.game_state = "main_menu"
    if is_key_pressed(KEY_ENTER):
        if game.selected_level == 0 and game.levels[0]["unlocked"]:
            game.game_state = "game_level"

    # --- Drawing --- #
    draw_text("Level Selection", (1280 - measure_text("Level Selection", 50)) // 2, 80, 50, WHITE)
    draw_rectangle_rec(game.back_button, WHITE)
    draw_text("Back", int(game.back_button.x) + 25, int(game.back_button.y) + 10, 20, BLACK)

    if check_collision_point_rec(get_mouse_position(), game.back_button) and is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
        game.game_state = "main_menu"

    for i, level in enumerate(game.levels):
        if level["unlocked"]:
            draw_rectangle_rec(level["rect"], BLUE)
        else:
            draw_rectangle_rec(level["rect"], GRAY)

        draw_text(str(i + 1), int(level["rect"].x) + 40, int(level["rect"].y) + 30, 40, WHITE)

        if i == game.selected_level:
            if game.levels[i]["unlocked"]:
                draw_rectangle_lines_ex(level["rect"], 5, RED)
            else:
                draw_rectangle_lines_ex(level["rect"], 5, YELLOW)
