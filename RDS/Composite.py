from os import listdir
from PIL import Image # фикс везде

def Composite(size, pos, image, *images):

    images = [pos, image]+list(images)
    
    assert len(images)//2, "Должно быть четное количество пар"

    image_pairs = [(pos, image) for pos, image in zip(images[::2], images[1::2])]

    composite = Image.new("RGBA", size, color="#0000")

    for pos, image in image_pairs:
        image_offset = Image.new("RGBA", size, color="#0000")
        image_offset.paste(image, pos)
        composite = Image.alpha_composite(composite, image_offset)

    return composite



if __name__ == "__main__":

    images = []

    for image in listdir("images"):
        images+= [(0, 0), Image.open("images/"+image)]

    Composite(images[1].size,  *images).show()

