use std::{env, path::Path};

use duvet::{audio_out::AudioMode, player::Player};



fn main() {
    
    let args: Vec<String> = env::args().collect();
    let file_path = Path::new(&args[1]);

    // write to wav from midi file
    let file_name = file_path.file_stem().unwrap().to_str().unwrap().to_string();
    let mut player = Player::new_midi(file_path, AudioMode::Record(file_name));

    // main update loop
    while player.update() {
        // thread::sleep(Duration::from_millis(50));
    }
    player.drain();
}

