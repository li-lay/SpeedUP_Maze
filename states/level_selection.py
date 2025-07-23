from pyray import (
    KEY_DOWN,
    KEY_ENTER,
    KEY_ESCAPE,
    KEY_LEFT,
    KEY_RIGHT,
    KEY_UP,
    MOUSE_LEFT_BUTTON,
    KeyboardKey,
    check_collision_point_rec,
    draw_rectangle_lines_ex,
    draw_rectangle_rec,
    draw_text,
    get_mouse_position,
    is_key_pressed,
    is_mouse_button_pressed,
    measure_text,
)

from resources.color.colors import BLACK, BLUE, GRAY, RED, WHITE, YELLOW


def level_selection(game):
    # --- Input --- #
    if is_key_pressed(KEY_RIGHT) or is_key_pressed(KeyboardKey(76)):
        game.selected_level = (game.selected_level + 1) % 10
    if is_key_pressed(KEY_LEFT) or is_key_pressed(KeyboardKey(72)):
        game.selected_level = (game.selected_level - 1 + 10) % 10
    if is_key_pressed(KEY_DOWN) or is_key_pressed(KeyboardKey(74)):
        game.selected_level = (game.selected_level + 5) % 10
    if is_key_pressed(KEY_UP) or is_key_pressed(KeyboardKey(75)):
        game.selected_level = (game.selected_level - 5 + 10) % 10
    if is_key_pressed(KEY_ESCAPE):
        game.game_state = "main_menu"
    if is_key_pressed(KEY_ENTER):
        if game.selected_level == 0 and game.levels[0]["unlocked"]:
            game.game_state = "game_level"

    # --- Drawing --- #
    draw_text(
        "Level Selection",
        (1280 - measure_text("Level Selection", 50)) // 2,
        80,
        50,
        WHITE,
    )
    draw_rectangle_rec(game.back_button, WHITE)
    draw_text(
        "Back", int(game.back_button.x) + 25, int(game.back_button.y) + 10, 20, BLACK
    )

    if check_collision_point_rec(
        get_mouse_position(), game.back_button
    ) and is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
        game.game_state = "main_menu"

    for i, level in enumerate(game.levels):
        if level["unlocked"]:
            draw_rectangle_rec(level["rect"], BLUE)
        else:
            draw_rectangle_rec(level["rect"], GRAY)

        draw_text(
            str(i + 1), int(level["rect"].x) + 40, int(level["rect"].y) + 30, 40, WHITE
        )

        if i == game.selected_level:
            if game.levels[i]["unlocked"]:
                draw_rectangle_lines_ex(level["rect"], 5, RED)
            else:
                draw_rectangle_lines_ex(level["rect"], 5, YELLOW)
