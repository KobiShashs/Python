keyboard_shortcuts = {"Copy": "Ctrl + C",
                      "Paste": "Ctrl + V", "Undo": "Ctrl + Z", "Cut": "Ctrl + X"}

print(keyboard_shortcuts)
del keyboard_shortcuts["Copy"]
print(keyboard_shortcuts)
keyboard_shortcuts.pop("Paste")
print(keyboard_shortcuts)