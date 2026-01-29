from gtts import gTTS
import random

class Solution:
    def task3(self,):
        random_vlu = random.randint(1000,9999)
        with open("python1.txt", "w") as d:
                d.write(str(random_vlu))
                d.close()
        tts = gTTS(f"{random_vlu}")
        tts.save("otp.mp3")

if __name__ == "__main__":
    s = Solution()
    s.task3()
