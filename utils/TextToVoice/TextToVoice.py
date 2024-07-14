from gtts import gTTS
import os
from pydub import AudioSegment
import simpleaudio as sa

DIR_PATH = os.path.abspath(os.path.curdir)

class TextToVoice:
    def __init__(self,name="output"):
        self.audio_file = f"{name}.wav"
        self.audio_wave_object = None
        self.play_obj = None

    def generate_speech(self, text, lang='en', tld='com', slow=False, lang_check=True, name=None):
        AudioSegment.converter = DIR_PATH+r"\ffmpeg.exe"
        tts = gTTS(text=text, lang=lang, tld=tld, slow=slow, lang_check=lang_check)
        if name is None:
            name = 'output.mp3'
        else:
            name = name + '.mp3'
        name = DIR_PATH + name
        tts.save(name)
        sound = AudioSegment.from_mp3(name)
        sound.export(self.audio_file, format="wav")
        os.remove(name)
        self.audio_wave_object = sa.WaveObject.from_wave_file(self.audio_file)

    def play(self, text, lang='en'):
        self.generate_speech(text, lang=lang)
        if self.play_obj is not None:
            self.play_obj.stop()
        self.play_obj = self.audio_wave_object.play()
        self.play_obj.wait_done()

        self.remove()


    def stop(self):
        if self.play_obj is not None:
            self.play_obj.stop()

        self.remove()

    def remove(self):
        try:
            os.remove(self.audio_file)
        except:pass