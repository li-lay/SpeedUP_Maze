from pyray import init_window, window_should_close, begin_drawing, clear_background, end_drawing, close_window, load_texture, unload_texture, Rectangle, set_exit_key
from resources.color.colors import BLACK
from states.main_menu import main_menu
from states.level_selection import level_selection
from states.quit_confirmation import quit_confirmation
from states.game_level import game_level

class Game:
    def __init__(self):
        self.game_state = "main_menu"
        self.previous_game_state = "main_menu"
        self.selected_level = 0
        self.exit_window = False
        self.quit_selection = 0 # 0 for YES, 1 for NO

        # --- Player --- #
        self.player_rect = Rectangle(80, 80, 40, 40)
        self.player_speed = 10
        self.player_direction = None # None, "left", "right", "up", "down"

        # --- Level --- #
        self.level = [
            "################################",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "#                              #",
            "################################",
        ]

        self.wall_rects = []
        for r, row in enumerate(self.level):
            for c, col in enumerate(row):
                if col == "#":
                    self.wall_rects.append(Rectangle(c * 40, r * 40, 40, 40))

        # --- Levels --- #
        self.levels = []
        for i in range(10):
            self.levels.append({
                "unlocked": i == 0,
                "rect": Rectangle((1280 - 5*110) // 2 + (i % 5) * 110, 200 + (i // 5) * 110, 100, 100)
            })

        # --- Buttons --- #
        self.back_button = Rectangle(20, 20, 100, 40)
        self.quit_yes_button = Rectangle(1280 // 2 - 100, 800 // 2, 80, 40)
        self.quit_no_button = Rectangle(1280 // 2 + 20, 800 // 2, 80, 40)

def main():
    init_window(1280, 800, "SpeedUP Maze")
    set_exit_key(0)

    game = Game()
    meme = load_texture("resources/images/meme.jpeg")

    while not game.exit_window:
        if window_should_close():
            game.previous_game_state = game.game_state
            game.game_state = "quit_confirmation"
            game.quit_selection = 0

        begin_drawing()
        clear_background(BLACK)

        if game.game_state == "main_menu":
            main_menu(game, meme)
        elif game.game_state == "level_selection":
            level_selection(game)
        elif game.game_state == "quit_confirmation":
            quit_confirmation(game)
        elif game.game_state == "game_level":
            game_level(game)

        end_drawing()

    unload_texture(meme)
    close_window()

if __name__ == "__main__":
    main()
