from PIL import Image, ImageDraw, ImageFont, ImageOps


def generate_avi(kwargs):
    W, H = (400,400)


    back = Image.new("RGBA",(W,H),kwargs['bg_color'])

    back.save('back.png')

    #pyconNG logo
    logo = Image.open('app/static/logo.png')
    # import pdb ; pdb.set_trace()
    w,h = logo.size
    logo = logo.resize((int(w/2), int(h/2)),Image.ANTIALIAS);
    back.paste(logo, (15,15),logo)
    # back.save('back.png')

    bg_w, bg_h = back.size
    #downloaded user image
    # import pdb ; pdb.set_trace()
    im = Image.open(kwargs['image'].name)
    im = im.resize((200,200),Image.ANTIALIAS)
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    im.putalpha(mask)
    # im.save("a.png")
    img_w, img_h = im.size

    offset = (int((bg_w - img_w) / 2), int((bg_h - img_h) / 2))

    back.paste(im,offset,im)

    back.save('final.png')


    name = kwargs['title']
    draw = ImageDraw.Draw(back)
    font = ImageFont.truetype("app/static/FiraCode-Bold.ttf",22)
    # import pdb ; pdb.set_trace()
    w, h = font.getsize(name)



    draw.text(((W-w)/2,(350)), name, fill=kwargs['fg_color'],font=font)

    back.save("avatar.png", "PNG")

    return True

    
