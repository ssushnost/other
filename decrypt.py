from PIL import Image, ImageDraw

orig = Image.open('../../Downloads/Telegram Desktop/original.png')
res = Image.open('result.png')
draw = ImageDraw.Draw(orig)
draw_res = ImageDraw.Draw(res)
width = orig.size[0]
height = orig.size[1]
pix = orig.load()
res_pix = res.load()

for i in range(width):
    for j in range(height):
        if pix[i, j] != res_pix[i, j]:
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            if res_pix[i, j] == (r + 1, g, b):
                draw.point((i, j), (0, 0, 0))

orig.save('result_message.png', 'PNG')
