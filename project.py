import os
try:
    import pyray as rl
    import random as rng
except:
    os.system("py -m pip install raylib")
    quit()
class game():
    def __init__(engine):
        engine.setup()
    def tick(engine):
        if rl.is_key_pressed(rl.KEY_SPACE):
            if engine.balance >= engine.bet:
                engine.balance -= engine.bet
                engine.roll()
        if rl.is_key_pressed(rl.KEY_UP):
            engine.changebet("up")
        if rl.is_key_pressed(rl.KEY_DOWN):
            engine.changebet("down")
        if rl.is_key_pressed(rl.KEY_R):
            engine.balance = 1000.00
            engine.bet = 10.00
    def setup(engine):
        engine.slots = [0, 0, 0]
        engine.texturecache = {}
        engine.texturecache["cherry"] = rl.load_texture("assets/cherry.png")
        engine.texturecache["lemon"] = rl.load_texture("assets/lemon.png")
        engine.texturecache["orange"] = rl.load_texture("assets/orange.png")
        engine.texturecache["bell"] = rl.load_texture("assets/bell.png")
        engine.texturecache["bar"] = rl.load_texture("assets/bar.png")
        engine.slotoptions = ["cherry", "lemon", "orange", "bell", "bar"]
        engine.slotoptionscolours = [rl.RED, rl.YELLOW, rl.ORANGE, rl.GOLD, rl.BLUE]
        engine.accum24hz = 0
        engine.balance = 1000.00
        engine.bet = 10.00
        rl.init_window(400, 300, "Not a slot machine")
        rl.set_target_fps(60)
        while not rl.window_should_close():
            engine.tick()
            rl.begin_drawing()
            rl.clear_background(rl.GRAY)
            rl.draw_text(f"Slot Machine", 20, 20, 20, rl.LIGHTGRAY)
            rl.draw_text(f"balance: ${engine.balance}", 20, 40, 20, rl.LIGHTGRAY)
            rl.draw_text(f"current bet: ${engine.bet}", 20, 60, 20, rl.LIGHTGRAY)
            rl.draw_rectangle(75, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[0]], 80, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(85, 105, 30, 25, engine.slotoptionscolours[engine.slots[0]])
            rl.draw_texture_ex(engine.texturecache[engine.slotoptions[engine.slots[0]]], rl.Vector2(75, 100), 0, 1, rl.WHITE)
            rl.draw_rectangle(175, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[1]], 180, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(185, 105, 30, 25, engine.slotoptionscolours[engine.slots[1]])
            rl.draw_texture_ex(engine.texturecache[engine.slotoptions[engine.slots[1]]], rl.Vector2(175, 100), 0, 1, rl.WHITE)
            rl.draw_rectangle(275, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[2]], 280, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(285, 105, 30, 25, engine.slotoptionscolours[engine.slots[2]])
            rl.draw_texture_ex(engine.texturecache[engine.slotoptions[engine.slots[2]]], rl.Vector2(275, 100), 0, 1, rl.WHITE)
            rl.end_drawing()
        rl.close_window()
    def roll(engine):
        starttime = rl.get_time()
        rl.set_target_fps(12)
        while rl.get_time() - starttime < 1:
            engine.slots[0] = rng.randint(0, 4)
            engine.slots[1] = rng.randint(0, 4)
            engine.slots[2] = rng.randint(0, 4)
            rl.begin_drawing()
            rl.clear_background(rl.GRAY)
            rl.draw_text(f"Slot Machine", 20, 20, 20, rl.LIGHTGRAY)
            rl.draw_text(f"balance: ${engine.balance}", 20, 40, 20, rl.LIGHTGRAY)
            rl.draw_text(f"current bet: ${engine.bet}", 20, 60, 20, rl.LIGHTGRAY)
            rl.draw_rectangle(75, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[0]], 80, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(85, 105, 30, 25, engine.slotoptionscolours[engine.slots[0]])
            rl.draw_rectangle(175, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[1]], 180, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(185, 105, 30, 25, engine.slotoptionscolours[engine.slots[1]])
            rl.draw_rectangle(275, 100, 50, 50, rl.DARKGRAY)
            rl.draw_text(engine.slotoptions[engine.slots[2]], 280, 135, 10, rl.LIGHTGRAY)
            rl.draw_rectangle(285, 105, 30, 25, engine.slotoptionscolours[engine.slots[2]])
            rl.end_drawing()
        rl.set_target_fps(60)
        engine.checkwin()
    def checkwin(engine):
        match engine.slots:
            case [0, 0, 0]:
                print("You win a cherry!")
                engine.balance += engine.bet * 2
            case [1, 1, 1]:
                print("You win a lemon!")
                engine.balance += engine.bet * 3
            case [2, 2, 2]:
                print("You win an orange!")
                engine.balance += engine.bet * 3
            case [3, 3, 3]:
                print("You win a bell!")
                engine.balance += engine.bet * 3
            case [4, 4, 4]:
                print("You win a bar!")
                engine.balance += engine.bet * 5
            case _:
                if engine.slots.count(0) == 2:
                    print("You win a small prize!")
                    engine.balance += engine.bet * 1.1
                elif engine.slots.count(1) == 2:
                    print("You win a small prize!")
                    engine.balance += engine.bet * 1.25
                elif engine.slots.count(2) == 2:
                    print("You win a small prize!")
                    engine.balance += engine.bet * 1.25
                elif engine.slots.count(3) == 2:
                    print("You win a small prize!")
                    engine.balance += engine.bet * 1.25
                elif engine.slots.count(4) == 2:
                    print("You win a small prize!")
                    engine.balance += engine.bet * 1.5
                else:
                    print("You lose!")
    def changebet(engine, direction):
        if rl.is_key_down(rl.KEY_LEFT_SHIFT):
            engine.shifting = 10
        else:
            engine.shifting = 1
        if direction == "up":
            engine.bet += 10 * engine.shifting
        elif direction == "down":
            engine.bet -= 10 * engine.shifting
        engine.bet = rl.clamp(engine.bet, 10, 1000)
instance = game()
