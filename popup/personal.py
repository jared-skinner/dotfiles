from popup.tasks.main import *
from popup.tasks.shell import *
from popup.tasks.group import *
HOME = os.environ['HOME']

from cmd import copy_dots, cmd_packages

graphics = Group(name = "graphics", deps = [
    Package("gimp"),
    Package("inkscape"),
])

math = Group(name = "math", deps = [
    Package("xaos"),
])

video = Group(name = "video", deps = [
    Package("vlc"),
])

gaming = Group(name = "gaming", deps = [
    Package("steam"),
    #TODO: emulators and roms
])

alacritty = Group(name = "alacritty", deps = [
    Bash("sudo apt update -y && sudo apt upgrade -y"),
    Bash("sudo add-apt-repository ppa:aslatter/ppa -y"),
    Package("alacritty")
])

office = Group(name = "office", deps = [
    Package("anki"),
    # TODO: LaTeX
    # TODO: Task warrior?
])

main_task = Main(name="personal_work", deps=[
    copy_dots,
    cmd_packages,
    graphics,
    math,
    video,
    gaming,
    alacritty,
    office
])
