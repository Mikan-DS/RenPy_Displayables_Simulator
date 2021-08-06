from re import fullmatch as match
from PIL.Image import new


def Solid(color, xsize=1920, ysize=1080):

    if isinstance(color, str):

        color = color.replace("#" , "")

        if match("[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", color):

            mode = "RGB"

        elif match("[0-9a-fA-F]{4}|[0-9a-fA-F]{8}", color):

            mode = "RGBA"

        else:

            raise Exception("Wrong color: "+str(color))

        color = "#"+color

    elif isinstance(color, [list, tuple]):

        if len(color) == 3:

            mode = "RGB"

        elif len(color) == 4:

            mode = "RGBA"
    
        else:
            raise Exception("Wrong color: "+str(color))

    else:
        raise Exception("Wrong color: "+str(color))

    return new(mode, (xsize, ysize), color)

if __name__ == "__main__":

    color = input("Цвет (RGB HTML): ")

    assert color, input("Нужно указать цвет")

    xsize = 1920
    x = input("Ширина (1920): ")
    if x.isnumeric():
        xsize = int(x)

    ysize = 1080
    y = input("Высота (1080): ")
    if y.isnumeric():
        ysize = int(y)


    name = input("Название файла (Blank): ") or "Blank"

    image = Solid(color, xsize, ysize)

    image.show()

    image.save(name+(".png" if "A" in image.mode else ".jpg"))
