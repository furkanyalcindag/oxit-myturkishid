from PIL import Image, ImageDraw

from myturkishiid.models import Menu
from myturkishiid.models.Language import Language


def getMenu(request):
    menus = Menu.objects.all().order_by('name')

    return {'menus': menus}


def languages(request):
    languages = Language.objects.all()

    lang = None

    if not ('lang' in request.COOKIES):
        lang = Language.objects.get(code='tr')
    else:
        lang = Language.objects.get(id=request.COOKIES['lang'])

    return {'langs': languages, 'lang': lang}


def add_text_overlay(image, text):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    text_size_x, text_size_y = image_draw.textsize(text)
    text_xy = ((rgba_image.size[0] / 2) - (text_size_x / 2), (rgba_image.size[1] / 2) - (text_size_y / 2))
    image_draw.text(text_xy, text, fill=(255, 255, 255, 128))
    image_with_text_overlay = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text_overlay