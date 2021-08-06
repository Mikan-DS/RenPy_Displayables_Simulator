from Composite import Composite
from Solid import Solid


def save_image(name, image):

    image.save(name+(".png" if "A" in image.mode else ".jpg"))

