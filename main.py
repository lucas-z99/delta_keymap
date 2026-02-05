import keyboard

word_list = {
    # set
    "\\not": "¬",
    "\\belong": ["∈", "∉"],
    "\\and": "∧",
    # sets
    "\\subset": ["⊆", "⊂"],
    "\\include": ["⊇", "⊃"],
    "\\union": "∪",
    "\\inter": "∩",
    "\\empty": "∅",
    "\\forall": "∀",
    "\\thereexist": "∃",
    # greek
    "\\alpha": ["α"],
    "\\beta": ["β"],
    "\\gamma": ["γ", "Γ"],
    "\\delta": ["Δ", "δ"],
    "\\epsilon": ["ε"],
    "\\zeta": ["ζ"],
    "\\theta": ["θ"],
    "\\lambda": ["λ"],
    "\\mu": ["μ"],
    "\\pi": ["π", "∏"],
    "\\sigma": ["∑"],
    "\\tau": ["τ"],
    "\\phi": ["φ", "Φ"],
    "\\psi": ["ψ", "Ψ"],
    "\\omega": ["Ω"],
    # others
    "\\infty": "∞",
    "\\integral": "∫",
    "\\approx": "≈",
}

buffer = ""
in_use = True
last_word = ""
last_index = 0


def on_key_event(event):
    global buffer, in_use, last_word, last_index

    if event.event_type == "down":

        if event.name == "esc":
            in_use = not in_use
            buffer = ""
            print(f"{in_use=}")
        if not in_use:
            pass

        if event.name == "backspace":
            buffer = buffer[:-1]

        elif event.name in ["space", "enter"]:
            buffer = ""

        elif event.name == "`":
            # a special KEY to loop between options, eg ["⊆", "⊂"] or ["Δ", "δ"]
            if last_word != "":
                options = word_list[last_word]
                if type(options) is not list:
                    pass
                old_symbol = options[last_index]
                last_index = (last_index + 1) if (last_index + 1) < len(options) else 0
                new_symbol = options[last_index]
                replace(len(old_symbol) + 1, new_symbol)  # +1 for the "`"

        elif len(event.name) == 1:  # single char

            if last_word != "":
                last_word = ""  # end of window to edit last_word

            buffer += event.name

            for word, options in word_list.items():  # replace the word with symbol
                if buffer.endswith(word):
                    symbol = options[0] if type(options) == list else options
                    replace(len(word), symbol)

                    buffer = ""
                    last_word = word
                    last_index = 0
                    break


def replace(to_remove, symbol):
    for _ in range(to_remove):
        keyboard.send("backspace")
    keyboard.write(symbol)


# check config - eg. if /in exists, /include will never trigger
for w1, _ in word_list.items():
    for w2, _ in word_list.items():
        if w1 != w2 and w2.startswith(w1):
            print(f"[Warning] {w1} blocks {w2}")
        pass

# start
print("---  Delta Map  ---")
print("Try:")
print("    \\theta   ->  Θ")
print("    \\subset  ->  ⊆")
print("(ESC to toggle ON/OFF)\n")


keyboard.hook(on_key_event)
keyboard.wait()
