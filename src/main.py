from game import Game

if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        game = Game()
        game.run()
    except Exception:
        # TODO - connect to sentry
        pass
