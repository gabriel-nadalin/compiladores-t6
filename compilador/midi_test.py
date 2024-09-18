from midiutil import MIDIFile

m = MIDIFile(eventtime_is_ticks=True)
nota = (69, 73, 76)
s_time = ...
duration = ...
# print(duration)
# m.addTempo(0, 0, 60)
m.addNote(0, 0, 69, 0, 3600, 100)
m.addNote(0, 0, 73, 0, 3600, 100)
m.addNote(0, 0, 76, 0, 3600, 100)

m.addNote(0, 0, 69, 3600, 7200, 100)
m.addNote(0, 0, 72, 3600, 7200, 100)
m.addNote(0, 0, 76, 3600, 7200, 100)
with open('A-major-minor.mid', 'wb') as output:
    m.writeFile(output)