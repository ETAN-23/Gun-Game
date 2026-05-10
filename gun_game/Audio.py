from pygame import mixer

class Audio:
    def __init__(self):
        self.music = {"lobby": r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\home_music.mp3",
                      "die":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\death.mp3", 
                      "reload":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\reload.mp3", 
                      "gun_shot":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\shot2.mp3", 
                      "victory":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\victory.mp3",
                      "background":r"C:\Users\Ethan\Coding Tutoring\gun_game\assests\bg_music.mp3"}
        self.currently_playing = None # lobby, die, survive
    
    def play_audio(self, audio_name, volume):
        if self.currently_playing != audio_name:
            mixer.music.load(self.music[audio_name])
            mixer.music.set_volume(volume)
            if audio_name !="victory":
                mixer.music.play(-1)
            mixer.music.play(1)
            self.currently_playing = audio_name

    def play_sound_effect(self, sound_effect, channel):
        sound = mixer.Sound(sound_effect)
        channel.play(sound)
