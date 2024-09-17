from midiutil import MIDIFile

m = MIDIFile(eventtime_is_ticks=True)
nota = (69, 73, 76)
s_time = ...
duration = ...
print(duration)

m.addNote(0, 0, nota, 0, 3600, 100)
with open('A-major.mid', 'wb') as output:
    m.writeFile(output)