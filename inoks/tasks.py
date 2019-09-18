from background_task import background
from logging import getLogger




@background(schedule=4)
def demo_task(message):
    print("deneme")
