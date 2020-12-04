from gtts import gTTS
import os
tts = gTTS(text='Hello sir, how can I help you?', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")