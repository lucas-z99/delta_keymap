import keyboard

###
#  does not support BACKSPACE
###


shortcuts = {
    '\\belong': '∈',
    '\\in': '∈',
    '\\not belong': '∉',

    '\\subset': '⊆',
    '\\s subset': '⊂', # strictly subset of
    '\\include': '⊇',
    '\\s include': '⊃', # strictly include

    '\\union': '∪',
    '\\inter': '∩', 
    '\\empty': '∅',

    '\\forall': '∀',
    '\\thereexist': '∃',
    '\\exist': '∃',
    '\\neg': '¬',

    '\\theta': 'Θ',
    '\\omega': 'Ω',
    '\\delta': 'Δ',
    '\\lambda': 'λ',


    '\\approx': '≈',
}

def register_hotkeys():
    for trigger, symbol in shortcuts.items():
        keyboard.add_abbreviation(trigger, symbol)
    
    print("--- Delta Map online ---")
    print("Try:")
    print("    \delta")
    print("    \subset")
    print("ESC to exit")
    keyboard.wait('esc')

if __name__ == "__main__":
    try:
        register_hotkeys()
    except KeyboardInterrupt:
        pass