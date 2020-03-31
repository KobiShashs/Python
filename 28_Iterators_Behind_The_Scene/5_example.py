freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes ="sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

my_iterable = str(notes).split("-")
print(my_iterable)
print(type(my_iterable))


import winsound
for item in my_iterable:
    frequency = str(item).split(",")[0]
    duration = str(item).split(",")[1]
    print(frequency,duration,)
    winsound.Beep(int(freqs[frequency]), int(duration)*5)

    