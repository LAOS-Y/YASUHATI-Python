import cocos
from cocos.director import director
from pyaudio import PyAudio, paInt16
import struct

WIN_WIDTH, WIN_HEIGHT = 1280, 720

class Player(cocos.sprite.Sprite):
    def __init__(self, img_path='player.png', init_pos=(0, 0)):
        super().__init__(img_path)

        self.position = init_pos
        self.speed = 0
        self.landed = True

        # self.schedule(self.fall)

    def jump(self, velocity):
        self.speed = velocity
        self.landed = False

    def fall(self, dt):
        self.speed -= 10 * dt
        self.y += self.speed

    def land(self):
        self.landed = True
        self.speed = 0


class Game(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        self.player = Player(init_pos=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.add(self.player)
        self.schedule(self.update)

        self.mic = PyAudio()
        self.sampling_rate = int(self.mic.get_device_info_by_index(0)['defaultSampleRate'])
        self.num_samples = 2048

    def getVolumn(self):
        stream = self.mic.open(
            format=paInt16,
            channels=1,
            rate=self.sampling_rate,
            input=True,
            frames_per_buffer=self.num_samples)
        string_audio_data = stream.read(self.num_samples)

        v = max(struct.unpack('2048h', string_audio_data))

        return v

    def update(self, dt):
        if self.player.landed:
            # pass
            v = self.getVolumn()

            if v > 2000:
                velocity = min((v - 2000) / 5000, 1) * 5
                print(v, velocity)

                self.player.jump(velocity)

        if not self.player.landed:
            self.player.fall(dt)

        if self.player.y <= WIN_HEIGHT / 2:
            self.player.land()
            self.player.y = WIN_HEIGHT / 2


director.init(width=WIN_WIDTH, height=WIN_HEIGHT)

game_layer = Game()
main_scene = cocos.scene.Scene(game_layer)
director.run(main_scene)