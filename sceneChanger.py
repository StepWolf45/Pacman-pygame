class SceneChanger:
    SCENE = 0
    GAME_STOPPED = False

    @staticmethod
    def change_scene(scene):
        SceneChanger.SCENE = scene

    @staticmethod
    def change_game_stopped():
        SceneChanger.GAME_STOPPED = not SceneChanger.GAME_STOPPED