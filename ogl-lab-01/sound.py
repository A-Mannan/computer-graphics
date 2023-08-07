from playsound import playsound

def play_audio_file(file_path):
    playsound(file_path)

if __name__ == "__main__":
    audio_file_path = "./sample.wav"
    play_audio_file(audio_file_path)
