import dearpygui.dearpygui as dpg
import string
import time

abc = string.ascii_lowercase
#abcdefghijklmnopqrstuvwxyz
print(abc)

callback_list = []
time_list = []
time_it = []

def callback_print(sender, app_data):
    starts = time.time()
    last_char = app_data[-1]
    print(last_char)
    for i in range(len(callback_list), len(callback_list)+1):
        if last_char == abc[i]:
            callback_list.append(last_char)
            time_list.append(starts)
            print(callback_list)
            dpg.configure_item("hint_text", show = True, default_value = callback_list, wrap = 350)
            if len(callback_list) == 26:
                end = time.time()
                print("Congratulations!")
                start = time_list[0]
                time_it.append(end - start)
                round_time = round(time_it[0], 3)
                dpg.configure_item("time_it", default_value = f"Your time is: {round_time} seconds!", show = True)
                dpg.configure_item("abc_input", enabled = False)

def reset_game(sender, app_data):
    dpg.configure_item("abc_input", default_value = "")
    callback_list.clear()
    time_list.clear()
    if time_it[0] != 0: 
        dpg.configure_item("time_it", show = False)
    time_it.clear()
    dpg.configure_item("hint_text", show = False)
    dpg.configure_item("abc_input", enabled = True)

dpg.create_context()
dpg.create_viewport(title = 'Can you beat the ABC game?', width = 360, height = 200)

with dpg.window(label = "Vnutorne sily", pos=(50, 50), tag="window"):

    dpg.add_input_text(callback = callback_print, hint = "Start typing ABC...", width = 350, tag = "abc_input")
    dpg.add_button(label = "Reset game!", show = True, callback = reset_game, tag = "reset_game")
    dpg.add_text("empty", show = False, tag = "time_it")
    dpg.add_text("Hint:", tag = "hint_text_label")
    dpg.add_text("empty", show = False, tag = "hint_text")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()
