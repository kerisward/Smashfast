from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "Muwwah ha ha ha!  You die!!!  Ripley will be so disappointed!!!!",
        "Not a good choice and you're way too slow!!!  RIP Furiosa!!!",
        "Too bad, you die!  You will make a tasty treat Zombie Bunnies!!!",
        "Words can't describe your incompetence, so I'll just throw up and kill you!!!"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Opening_Scene(Scene):

    def enter(self):
        print "opening scene text here"
        return 'scene1'

class Scene_1(Scene):

    def enter(self):
        print "description of scene 1"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene2'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene1'

class Scene_2(Scene):

    def enter(self):
        print "description of scene 2"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene3'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene2'

class Scene_3(Scene):

    def enter(self):
        print "description of scene 3"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene4'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene3'

class Scene_4(Scene):

    def enter(self):
       print "Scene 4 description"

       action = raw_input("> ")

       if action == "option_a":
           print "Option A description"
           return 'finalscene'

       elif action == "option_b":
           print "Option B description"
           return 'death'

       elif action == "option_c":
           print "Option C description"
           return 'death'

       else:
           print "DOES NOT COMPUTE!"
           return 'scene4'

class Final_Scene(Scene):

    def enter(self):
        print "You won! Good job."
        exit()

class Map(object):

    scenes = {
        'openingscene': Opening_Scene(),
        'scene1': Scene_1(),
        'scene2': Scene_2(),
        'scene3': Scene_3(),
        'scene4': Scene_4(),
        'finalscene': Final_Scene(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('openingscene')
a_game = Engine(a_map)
a_game.play()
