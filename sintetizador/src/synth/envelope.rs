use std::f32::consts::LN_2;

use crate::SAMPLE_RATE;

#[derive(Clone, Copy, Debug)]
pub enum EnvelopeShape {
    Linear,
    Exponential,
}

impl EnvelopeShape {
    pub fn attack(self, time: f32, attack: f32) -> f32 {
        match self {
            Self::Linear => time / attack,
            Self::Exponential => (time / attack * LN_2).exp() - 1.,
        }
    }
    
    pub fn decay(self, time: f32, sustain: f32, decay: f32) -> f32 {
        match self {
            Self::Linear => 1. - (1. - sustain) * (time / decay),
            Self::Exponential => sustain + (1. - sustain) * (-6. * time / decay).exp(),
        }
    }
    
    pub fn release(self, time: f32, sustain: f32, release: f32) -> f32 {
        match self {
            Self::Linear => sustain * (1. - time / release),
            Self::Exponential => sustain * (-6. * time / release).exp(),
        }
    }
}

#[derive(Clone, Copy, Debug)]
pub enum EnvelopeState {
    Idle,
    Attack,
    Decay,
    Sustain,
    Release,
}

#[derive(Clone, Copy, Debug)]
pub struct Envelope {
    attack: f32,
    decay: f32,
    sustain: f32,
    release: f32,
    shape: EnvelopeShape,
    state: EnvelopeState,
    level: f32,
    time: f32,
}

impl Envelope {
    pub fn new(attack: f32, decay: f32, sustain: f32, release: f32, shape: EnvelopeShape) -> Self {
        Self {
            attack,
            decay,
            sustain,
            release,
            shape,
            state: EnvelopeState::Idle,
            level: 0.,
            time: 0.,
        }
    }

    pub fn state(&self) -> EnvelopeState {
        self.state
    }

    pub fn trigger(&mut self) {
        self.state = EnvelopeState::Attack;
        self.time = 0.;
    }

    pub fn release(&mut self) {
        if !matches!(self.state, EnvelopeState::Idle) && self.sustain > 0. {
            self.state = EnvelopeState::Release;
            self.time = 0.;
        }
    }

    pub fn get_level(&mut self) -> f32 {
        self.time += 1. / SAMPLE_RATE as f32;
        match self.state {
            EnvelopeState::Idle => {
                self.level = 0.;
            }
            EnvelopeState::Attack => {
                self.level = self.shape.attack(self.time, self.attack).min(1.).max(self.level);
                if self.time >= self.attack {
                    self.state = EnvelopeState::Decay;
                    self.time = 0.;
                }
            }
            EnvelopeState::Decay => {
                self.level = self.shape.decay(self.time, self.sustain, self.decay).min(1.);
                if self.time >= self.decay {
                    if self.sustain > 0. {
                        self.state = EnvelopeState::Sustain;
                    } else {
                        self.state = EnvelopeState::Release;
                        self.time = 0.;
                    }
                }
            }
            EnvelopeState::Sustain => {
                self.level = self.sustain;
            }
            EnvelopeState::Release => {
                self.level = self.shape.release(self.time, self.sustain, self.release).max(0.);
                if self.time >= self.release {
                    self.state = EnvelopeState::Idle;
                }
            }
        }
        self.level
    }
}
