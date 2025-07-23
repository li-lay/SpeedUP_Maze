from pyray import (
    Rectangle,
    begin_drawing,
    clear_background,
    close_audio_device,
    close_window,
    end_drawing,
    init_audio_device,
    init_window,
    load_music_stream,
    load_sound,
    load_texture,
    play_music_stream,
    set_exit_key,
    set_master_volume,
    unload_music_stream,
    unload_sound,
    unload_texture,
    update_music_stream,
    window_should_close,
)

from resources.color.colors import BLACK
from states.game_level import game_level
from states.level_selection import level_selection
from states.main_menu import main_menu
from states.quit_confirmation import quit_confirmation


class Game:
    def __init__(self):
        self.game_state = "main_menu"
        self.previous_game_state = "main_menu"
        self.selected_level = 0
        self.exit_window = False
        self.quit_selection = 0  # 0 for YES, 1 for NO

        # --- Player --- #
        self.player_rect = Rectangle(80, 80, 40, 40)
        self.player_speed = 10
        self.player_direction = None  # None, "left", "right", "up", "down"

        # --- Level --- #
        self.level = [
            "                                ",
            " ############################## ",
            " #     #    ##                # ",
            " ##### # ## ##                # ",
            " #   # # ## ##                # ",
            " #     # ## ##                # ",
            " #     # ## ##                # ",
            " ### ### ## ##                # ",
            " #     # ## ##                # ",
            " # #   # ## ##                # ",
            " # # ### ## ##                # ",
            " # # ### ## ##############    # ",
            " # # ### ## ####        ##    # ",
            " # # ### ## #### ###### ##    # ",
            " # # ### ## ####    ### ##    # ",
            " # # ### ## ####### ### ##    # ",
            " # # ### ##         ### ##    # ",
            " #       ##############       # ",
            " ############################## ",
            "                                ",
        ]

        self.wall_rects = []
        for r, row in enumerate(self.level):
            for c, col in enumerate(row):
                if col == "#":
                    self.wall_rects.append(Rectangle(c * 40, r * 40, 40, 40))

        # --- Levels --- #
        self.levels = []
        for i in range(10):
            self.levels.append(
                {
                    "unlocked": i == 0,
                    "rect": Rectangle(
                        (1280 - 5 * 110) // 2 + (i % 5) * 110,
                        200 + (i // 5) * 110,
                        100,
                        100,
                    ),
                }
            )

        # --- Buttons --- #
        self.back_button = Rectangle(20, 20, 100, 40)
        self.quit_yes_button = Rectangle(1280 // 2 - 100, 800 // 2, 80, 40)
        self.quit_no_button = Rectangle(1280 // 2 + 20, 800 // 2, 80, 40)


def main():
    init_window(1280, 800, "SpeedUP Maze")
    init_audio_device()
    set_master_volume(0.5)
    set_exit_key(0)

    game = Game()
    meme = load_texture("resources/images/meme.jpeg")
    music = load_music_stream("resources/music/time_for_adventure.mp3")
    jump_sound = load_sound("resources/sounds/jump.wav")
    world_tileset = load_texture("resources/sprites/world_tileset.png")

    play_music_stream(music)

    while not game.exit_window:
        if window_should_close():
            game.previous_game_state = game.game_state
            game.game_state = "quit_confirmation"
            game.quit_selection = 0

        update_music_stream(music)

        begin_drawing()
        clear_background(BLACK)

        if game.game_state == "main_menu":
            main_menu(game, meme)
        elif game.game_state == "level_selection":
            level_selection(game)
        elif game.game_state == "quit_confirmation":
            quit_confirmation(game)
        elif game.game_state == "game_level":
            game_level(game, jump_sound, world_tileset)

        end_drawing()

    unload_texture(meme)
    unload_music_stream(music)
    unload_sound(jump_sound)
    unload_texture(world_tileset)
    close_audio_device()
    close_window()


if __name__ == "__main__":
    main()
