from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.pow_ups.pow_up import PowerUp


class Hammer(PowerUp):  

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

        #vscode
        
