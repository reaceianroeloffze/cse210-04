import os
import random
import pyray

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 2


def main():
    score= 0
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_number("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    robot_x = int(MAX_X / 2)
    robot_y = int(585)
    position = Point(robot_x, robot_y)

    robot = Actor()
    robot.set_number(score)
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    #with open(DATA_PATH) as file:
    #    data = file.read()
    #    messages = data.splitlines()
    points = 0
    wind = random.randint(-3, 3)
    art_y =0
    while score <= 0 and art_y < 600:
    #for n in range(DEFAULT_ARTIFACTS):
        #text = chr(random.randint(33, 126))
        #message = messages[n]
        art_x = random.randint(1, COLS - 1)
        art_y += 2 + wind #random.randint(1, ROWS - 1)
        position = Point(art_x, art_y)
        position = position.scale(CELL_SIZE)
        #falling_position = Point(x, y+1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        number = score
        artifact = Artifact()
        artifact.set_number(number)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_points(points)
        cast.add_actor("artifacts", artifact)
        if art_x > 30:
            if pyray.is_key_down(pyray.KEY_LEFT):
                art_x -= 5
        if art_x < 770:
            if pyray.is_key_down(pyray.KEY_RIGHT):
                art_x += 5
        if artifact.set_position == robot.set_position:
            score += 1
            #respawn()
        if robot_y > 600:
            score -= 1
            #respawn()
        if robot_x < 30 or robot_x > 770:
            somewhere = -somewhere
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()