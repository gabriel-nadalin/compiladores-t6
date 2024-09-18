use std::fs::File;
use std::io::BufWriter;

use hound::{self, WavWriter};

use crate::{BIT_DEPTH, BUFFER_SIZE, SAMPLE_RATE};


pub enum Writer {
    WAV(WavWriter<BufWriter<File>>),
}

impl Writer {
    fn new(mode: AudioMode) -> Self {
        match mode {
            AudioMode::Record(file_name) => {
                let spec = hound::WavSpec {
                    channels: 1,
                    sample_rate: SAMPLE_RATE,
                    bits_per_sample: BIT_DEPTH,
                    sample_format: hound::SampleFormat::Int,
                };
                let file_name = "wav/".to_string() + &file_name + ".wav";
                let writer = hound::WavWriter::create(file_name, spec).unwrap();
        
                Self::WAV(writer)
            }
        }
    }

    fn write(&mut self, buffer: &Vec<u8>) {
        match self {
            Self::WAV(writer) => {
                for &sample in buffer {
                    writer.write_sample((sample as i16 - 128) as i8).unwrap();
                }
            }
        }
    }

    fn drain(&mut self) {
        match self {
            Self::WAV(_writer) => {}
        }
    }
}

pub enum AudioMode {
    Record(String),
}

pub struct AudioOut {
    writer: Writer,
    buffer: Vec<u8>
}

impl AudioOut {

    pub fn new(mode: AudioMode) -> Self {
        let writer = Writer::new(mode);
        let buffer = vec![];

        Self {
            writer,
            buffer,
        }
    }

    pub fn send(&mut self, sample: u8) {
        self.buffer.push(sample);
        if self.buffer.len() >= BUFFER_SIZE {
            self.writer.write(&self.buffer);
            self.buffer.clear();
        }
    }

    pub fn drain(&mut self) {
        self.writer.drain();
    }
}