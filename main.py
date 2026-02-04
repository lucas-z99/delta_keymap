import keyboard

###
#  you can BACKSPACE halfway
###


word_list = {
    "\\belong": "∈",
    "\\in": "∈",
    "\\not belong": "∉",
    "\\subset": "⊆",
    "\\s subset": "⊂",  # strictly subset of
    "\\include": "⊇",
    "\\s include": "⊃",  # strictly include
    "\\union": "∪",
    "\\inter": "∩",
    "\\empty": "∅",
    "\\forall": "∀",
    "\\thereexist": "∃",
    "\\exist": "∃",
    "\\neg": "¬",
    "\\theta": "Θ",
    "\\omega": "Ω",
    "\\delta": "Δ",
    "\\lambda": "λ",
    "\\approx": "≈",
}

buffer = ""


def on_key_event(event):
    global buffer

    if event.event_type == "down":

        if event.name == "backspace":
            buffer = buffer[:-1]  # remove last char

        elif event.name in ["space", "enter"]:
            buffer = ""

        elif len(event.name) == 1:  # ignore shift/ctrl etc
            buffer += event.name

            for word, symbol in word_list.items():
                if buffer.endswith(word):

                    # replace the word with symbol
                    for _ in range(len(word)):
                        keyboard.send("backspace")
                    keyboard.write(symbol)

                    buffer = ""
                    break


# check config - eg. if /in exists, /include will never trigger
for w1, _ in word_list.items():
    for w2, _ in word_list.items():
        if not w1 == w2 and w2.startswith(w1):
            print(f"[Warning] {w1} blocks {w2}")
        pass


# start
print("\n--- Delta Map online ---")
print("(ESC to exit)")
print()
print("Try:")
print("    \\theta   ->  Θ")
print("    \\subset  ->  ⊆")


keyboard.hook(on_key_event)
keyboard.wait("esc")
