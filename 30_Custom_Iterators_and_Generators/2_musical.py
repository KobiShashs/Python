class MusicalNote:
    def __init__(self, note, list_of_octaves):
        self._note = note
        self._list_of_octaves = list_of_octaves

    def get_note(self):
        return self._note

    def get_volume(self, note, vol):
        idx = 0
        for octave in self._list_of_octaves:
            if(idx == vol):
                return octave
            idx += 1


class MusicNotes:
    def __init__(self):
        self._frequens_list = []

    def add_note(self, new_note):
        self._frequens_list.append(new_note)

    def __iter__(self):
        self.freq_idx = -1
        return self

    def __next__(self):
        if(self.freq_idx >= len(self._frequens_list) - 1):
            raise StopIteration()
        self.freq_idx += 1
        curr_note = self._frequens_list[self.freq_idx]
        return curr_note.get_note()+" "+str(curr_note.get_volume(curr_note,1))


frequency_list = MusicNotes()
frequency_list.add_note(MusicalNote("La", [55, 110, 220, 440, 880]))
frequency_list.add_note(MusicalNote("Si", [61.74, 123.48, 246.96, 493.92, 987.84]))
frequency_list.add_note(MusicalNote("Do", [65.41, 130.82, 261.64, 523.28, 1046.56]))
frequency_list.add_note(MusicalNote("Re", [73.42, 146.84, 293.68, 587.36, 1174.72]))
frequency_list.add_note(MusicalNote("Mi", [82.41, 164.82, 329.64, 659.28, 1318.56]))
frequency_list.add_note(MusicalNote("Fa", [87.31, 174.62, 349.24, 698.48, 1396.96]))
frequency_list.add_note(MusicalNote("Sol", [98, 196, 392, 784, 1568]))


notes_iter = iter(frequency_list)
for freq in notes_iter:
    print(freq)
