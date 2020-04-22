import cocos
from cocos.director import director

WIN_WIDTH, WIN_HEIGHT = 1280, 720

class Player(cocos.sprite.Sprite):
    def __init__(self, img_path='player.png', init_pos=(0, 0)):
        super().__init__(img_path)

        self.init_pos = init_pos
        # self.position = init_pos
        # self.speed = 0

        self.reset()

        self.schedule(self.update)

    def jump(self, dt):
        self.speed = 50

    def update(self, dt):
        self.speed -= 10 * dt
        self.y += self.speed
        print(self.y)
        if self.y < 100:
            self.reset()

    def reset(self):
        self.speed = 0
        self.position = self.init_pos


class Game(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        # player = cocos.sprite.Sprite('player.png')
        player = Player(init_pos=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        # player.position = 

        self.add(player)


director.init(width=WIN_WIDTH, height=WIN_HEIGHT)

hello_layer = Game()
main_scene = cocos.scene.Scene(hello_layer)
director.run(main_scene)