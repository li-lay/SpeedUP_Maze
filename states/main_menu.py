from pyray import (
    KEY_ENTER,
    KEY_ESCAPE,
    KEY_SPACE,
    draw_text,
    draw_texture,
    is_key_pressed,
    measure_text,
)

from resources.color.colors import WHITE


def main_menu(game, meme):
    # --- Input ---
    if is_key_pressed(KEY_ENTER) or is_key_pressed(KEY_SPACE):
        game.game_state = "level_selection"
    if is_key_pressed(KEY_ESCAPE):
        game.previous_game_state = game.game_state
        game.game_state = "quit_confirmation"
        game.quit_selection = 0

    # --- Drawing --- #
    Logo_Text = "SpeedUP Maze"
    Logo_Size = 60
    draw_text(
        Logo_Text,
        (1280 - measure_text(Logo_Text, Logo_Size)) // 2,
        80,
        Logo_Size,
        WHITE,
    )
    draw_texture(meme, (1280 - meme.width) // 2, (800 - meme.height) // 2, WHITE)
    enter_to_start = "Press [ENTER] to start..."
    draw_text(
        enter_to_start, (1280 - measure_text(enter_to_start, 30)) // 2, 700, 30, WHITE
    )
