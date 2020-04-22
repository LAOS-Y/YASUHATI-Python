import cocos
from cocos.director import director

WIN_WIDTH, WIN_HEIGHT = 1280, 720

class Player(cocos.sprite.Sprite):
    def __init__(self, img_path='player.png', init_pos=(0, 0)):
        super().__init__(img_path)

        self.position = init_pos
        self.speed = 0
        self.landed = True

        # self.schedule(self.fall)

    def jump(self):
        self.speed = 5
        self.landed = False

    def fall(self, dt):
        self.speed -= 10 * dt
        self.y += self.speed
        print(self.y, self.speed)

    def land(self):
        self.landed = True
        self.speed = 0


class Game(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        # player = cocos.sprite.Sprite('player.png')
        self.player = Player(init_pos=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        # player.position = 

        self.add(self.player)

        self.schedule(self.update)

    def update(self, dt):
        if self.player.landed:
            self.player.jump()

        self.player.fall(dt)

        if self.player.y <= WIN_HEIGHT / 2:
            self.player.land()



director.init(width=WIN_WIDTH, height=WIN_HEIGHT)

game_layer = Game()
main_scene = cocos.scene.Scene(game_layer)
director.run(main_scene)