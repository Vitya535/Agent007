class Player():
    player = None

    def inst(i:int, j:int):
        if player is None:
            Player.player = Player(i, j)
        return Player

    def __init__(self, i:int, j:int):
        self.x = i
        self.y = j

    def move(steponrow:int, steponcolumn:int, CountSteps:int):
        for i in range(CountSteps, steponrow):
            for j in range(CountSteps, steponcolumn):


