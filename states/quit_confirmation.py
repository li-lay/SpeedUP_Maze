from pyray import (
    KEY_ENTER,
    KEY_ESCAPE,
    KEY_LEFT,
    KEY_RIGHT,
    MOUSE_LEFT_BUTTON,
    check_collision_point_rec,
    draw_rectangle_lines_ex,
    draw_rectangle_rec,
    draw_text,
    get_mouse_position,
    is_key_pressed,
    is_mouse_button_pressed,
    measure_text,
)

from resources.color.colors import BLACK, RED, WHITE


def quit_confirmation(game):
    # --- Input --- #
    if is_key_pressed(KEY_RIGHT):
        game.quit_selection = 1
    if is_key_pressed(KEY_LEFT):
        game.quit_selection = 0

    if is_key_pressed(KEY_ENTER):
        if game.quit_selection == 0:  # YES
            game.exit_window = True
        else:  # NO
            game.game_state = game.previous_game_state
    if is_key_pressed(KEY_ESCAPE):
        game.game_state = game.previous_game_state

    # --- Drawing --- #
    draw_text(
        "Are you sure you want to quit?",
        1280 // 2 - measure_text("Are you sure you want to quit?", 30) // 2,
        800 // 2 - 40,
        30,
        WHITE,
    )

    draw_rectangle_rec(game.quit_yes_button, WHITE)
    draw_text(
        "Yes",
        int(game.quit_yes_button.x) + 25,
        int(game.quit_yes_button.y) + 10,
        20,
        BLACK,
    )

    draw_rectangle_rec(game.quit_no_button, WHITE)
    draw_text(
        "No",
        int(game.quit_no_button.x) + 30,
        int(game.quit_no_button.y) + 10,
        20,
        BLACK,
    )

    if game.quit_selection == 0:
        draw_rectangle_lines_ex(game.quit_yes_button, 5, RED)
    else:
        draw_rectangle_lines_ex(game.quit_no_button, 5, RED)

    if check_collision_point_rec(
        get_mouse_position(), game.quit_yes_button
    ) and is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
        game.exit_window = True

    if check_collision_point_rec(
        get_mouse_position(), game.quit_no_button
    ) and is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
        game.game_state = game.previous_game_state
