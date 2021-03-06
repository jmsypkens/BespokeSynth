def schedule_seq(seq, pitchOffset=0, velocity=80, start=0, bars=1, output=None):
   if output is None:
      output = this.this()
   if not type(seq) is list:
      seq = [seq]
   if len(seq) == 0:
      return
   stepLength = float(bars) / len(seq)
   for i,entry in enumerate(seq):
      if entry != '':
         if type(entry) is tuple:
            for subentry in entry:
               schedule_seq(subentry, pitchOffset, velocity, start + stepLength * i, stepLength, output)
         elif type(entry) is list:
            schedule_seq(entry, pitchOffset, velocity, start + stepLength * i, stepLength, output)
         elif type(entry) is int or type(entry) is str:
            pitch = entry
            if type(entry) is str:
               pitch = bespoke.name_to_pitch(entry)
            output.schedule_note(start + stepLength * i, pitch + pitchOffset, velocity, stepLength) 