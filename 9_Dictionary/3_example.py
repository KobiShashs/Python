keyboard_shortcuts = {"Copy": "Ctrl + C",
                      "Paste": "Ctrl + V", "Undo": "Ctrl + Z"}
print(keyboard_shortcuts)

print(keyboard_shortcuts["Paste"])
keyboard_shortcuts["Paste"] = "Shift + Insert"
print(keyboard_shortcuts["Paste"])
print(keyboard_shortcuts)

print(keyboard_shortcuts["Cut"])
