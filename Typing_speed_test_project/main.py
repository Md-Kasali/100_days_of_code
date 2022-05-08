from tkinter import Tk
import tkinter as tk

FONT = ("SourceSansPro", "14", "normal")

# Practice-text
model_text = "Curling is the best sport named after something you do to your hair." \
             " If a dog and cat had a baby together that grew up and worked a desk job he'd be a Cog in the machine." \
             " I have a moral code, but I haven't figured out how to read it yet. " \
             "You know the Grammys are a joke when Future doesn't win Best Everything. " \
             "A tagline for a car company that prides itself on its morals and ethics: Take the High Road."

text_list = model_text.split(" ")

text_color = "#6B4F4F"

# ----------------------------GLOBAL VARIABLES------------------------------- #

# Count number of correct and incorrect words
nr_correct = 0
nr_incorrect = 0

# Index selects the word from the text_list
select_index = 0
start_pressed = False

# Global Variables to track index in the text box
start_index = "1.0"
end_index = "1.X"
track_index_value = 0

window = Tk()
window.title("Type-master")
window.configure(padx=100, pady=50, bg="#FF9292")

def initializer():
    global nr_correct, nr_incorrect, select_index, start_index, track_index_value
    nr_correct = 0
    nr_incorrect = 0
    select_index = 0
    start_index = "1.0"
    track_index_value = 0

# ----------------------------- Functions --------------------------#

#
def key_press():
    global select_index, \
        end_index, start_index, track_index_value, nr_correct, nr_incorrect, start_pressed

    # Deletes the highlighting of previously highlighted text
    text_box.tag_delete("highlight", start_index, end_index)

    if len(entry_box.get()) != 0 and start_pressed:
        curr_text = text_list[select_index]
        user_input = entry_box.get().strip()
        if user_input == curr_text:
            nr_correct += 1
        else:
            nr_incorrect += 1
        entry_box.delete(0, last=len(entry_box.get()))

        track_index_value += len(curr_text) + 1

        start_index = f'1.{track_index_value}'
        select_index += 1
        end_index = track_index_value + len(text_list[select_index]) # Bug
        end_index = f"1.{end_index}"
        text_box.tag_add("highlight", start_index, end_index)
        text_box.tag_config("highlight", background="#FFC947")


def start_timer(c):
    global nr_correct, model_text, start_pressed
    if c == -1:
        wpm_canvas.itemconfig(wpm_count, text=str(nr_correct))
        text_box.delete(1.0, float(f"1.{len(model_text)}"))
        start_pressed = False
    else:
        count = c
        time_canvas.itemconfig(timer_text, text=str(count))
        window.after(1000, start_timer, count-1)


def start():
    global end_index, model_text, start_pressed
    entry_box.delete(0, len(entry_box.get()))
    start_pressed = True
    initializer()
    text_box.delete(1.0, float(f"1.{len(model_text)}"))
    text_box.insert(1.0, model_text)
    end_index = f"1.{len(text_list[select_index])}"
    text_box.tag_add("highlight", start_index, end_index)
    text_box.tag_config("highlight", background="#FFC947")
    start_timer(60)


window.bind('<space>', lambda x: key_press())

time_canvas = tk.Canvas(width=150, height=100, bg="#FFF9B6", highlightthickness=0)
time_text = time_canvas.create_text(70, 20, text="Time", fill=text_color, font=("SourceSansPro", "18", "bold"))
timer_text = time_canvas.create_text(72, 60, text="60", fill=text_color, font=("SourceSansPro", "28", "bold"))
time_canvas.grid(row=0, column=0, pady=20)

wpm_canvas = tk.Canvas(width=150, height=100, bg="#FFF9B6", highlightthickness=0)
wpm_text = wpm_canvas.create_text(75, 20, text="WPM", fill=text_color, font=("SourceSansPro", "18", "bold"))
wpm_count = wpm_canvas.create_text(75, 60, text="0", fill=text_color, font=("SourceSansPro", "28", "bold"))
wpm_canvas.grid(row=0, column=2, pady=20)

text_box = tk.Text(window, height=5, font=FONT, bd=0, highlightthickness=0, padx=10, pady=10, wrap="word", bg="#FFF9B6", fg=text_color)
text_box.insert(1.0, model_text)
text_box.config(state="disabled")
text_box.grid(row=1, column=0, columnspan=3)

entry_box = tk.Entry(window, font=FONT, highlightthickness=0, width=40, bg="#FFCCD2", border=0, fg=text_color)
entry_box.grid(row=2, column=0, columnspan=3, pady=20)

start_btn = tk.Button(window, text="Start", command=start, bg="#C85C5C", fg="white",
                      highlightthickness=0, font=FONT, relief="raised", activebackground="#FFCCD2",
                      activeforeground=text_color)
start_btn.grid(row=3, column=1)

window.mainloop()
