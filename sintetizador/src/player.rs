use std::path::Path;

use midly::MidiMessage;

use crate::{audio_out::{AudioMode, AudioOut}, synth::instrument::Instrument, midi_scheduler::MidiScheduler, synth::Synth, SAMPLE_RATE};

pub struct MidiPlayer {
    scheduler: MidiScheduler,
}

impl MidiPlayer {
    pub fn new(file_path: &Path) -> Self {
        let scheduler = MidiScheduler::new(file_path);
        Self {
            scheduler,
        }
    }

    fn update(&mut self, synth: &mut Synth, time: f64) -> bool {
        if let Some((timestamp, channel, message)) = self.scheduler.current_event() {
            if timestamp <= time {
                match message {
                    MidiMessage::NoteOn { key, vel } => {
                        if vel == 0 {
                            synth.note_off(channel, key.as_int());
                        }
                        else {
                            synth.note_on(channel, key.as_int());
                        }
                    }
                    MidiMessage::NoteOff { key, .. } => {
                        synth.note_off(channel, key.as_int());
                    }
                    _ => ()
                }

                self.scheduler.next_event();
            }
            true
        }
        else {
            false
        }
    }
}


pub enum PlayerKind {
    Midi(MidiPlayer),
}

pub struct Player {
    synth: Synth,
    out: AudioOut,
    time: f64,
    
    kind: PlayerKind,
}

impl Player {
    pub fn new(kind: PlayerKind, audio_mode: AudioMode) -> Self {
        let mut synth = Synth::new();

        let voice = Instrument::lead_square(0.5);

        synth.add_instrument(0, voice);

        let out = AudioOut::new(audio_mode);

        Self {
            synth,
            kind,
            out,
            time: 0.,
        }
    }

    pub fn new_midi(file_path: &Path, audio_mode: AudioMode) -> Self {
        let midi_player = MidiPlayer::new(file_path);
        Self::new(PlayerKind::Midi(midi_player), audio_mode)
    }

    pub fn update(&mut self) -> bool {
        let condition;
        match &mut self.kind {
            PlayerKind::Midi(midi_player) => {
                condition = midi_player.update(&mut self.synth, self.time);
            }
        }

        let sample = self.synth.next_sample();
        self.out.send(bipolar2u8(sample));
        self.time += 1. / SAMPLE_RATE as f64;
        condition
    }

    pub fn drain(&mut self) {
        self.out.drain()
    }
}

pub fn bipolar2u8(sample: f32) -> u8 {
    let sample = ((sample + 1.) / 2.) * 255.;
    sample.round() as u8
}