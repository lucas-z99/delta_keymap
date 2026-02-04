import keyboard

###
#  you can BACKSPACE halfway
###


shortcuts = {
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

    # We only care when the key is pressed DOWN
    if event.event_type == "down":

        # 1. Handle Backspace (The Fix!)
        if event.name == "backspace":
            # Remove the last character from our buffer
            buffer = buffer[:-1]

        # 2. Handle Standard Characters
        # We only want to track single printable characters (ignore Shift, Ctrl, etc.)
        elif len(event.name) == 1:
            buffer += event.name

            # Check for match at the END of the buffer
            for trigger, symbol in shortcuts.items():
                if buffer.endswith(trigger):
                    # MATCH FOUND!

                    # A. Remove the trigger from the screen
                    # We send 'backspace' exactly as many times as the trigger length
                    for _ in range(len(trigger)):
                        keyboard.send("backspace")

                    # B. Type the symbol
                    keyboard.write(symbol)

                    # C. Clear the buffer so we don't double-trigger
                    # (e.g. typing \alll shouldn't trigger twice)
                    buffer = ""
                    break

        # 3. Safety: Clear buffer on Space/Enter to keep it clean
        # This prevents accidental triggers from text typed 10 minutes ago
        elif event.name in ["space", "enter"]:
            buffer = ""


# start
print("--- Delta Map online ---")
print("(ESC to exit)")
print()
print("Try:")
print("    \\theta   ->  Θ")
print("    \\subset  ->  ⊆")


keyboard.hook(on_key_event)
keyboard.wait("esc")
