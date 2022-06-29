from pygame import mixer
from gtts import gTTS

def main():
    text = gTTS("Hello guys, welcome to learn apply build")
    text.save("/home/sanman/tinyprojects/lab.mp3")
    mixer.init()
    mixer.music.load("/home/sanman/tinyprojects/lab.mp3")
    mixer.music.play
    
    
if __name__== "__main__":
    main()