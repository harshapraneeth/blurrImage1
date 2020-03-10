from PIL import Image

image_url = 'jw.jpg'
image_size = (300,300)
image_mode = 'RGB'
blurr_radius = 3
blurr_intensity = 1

image = Image.open(image_url).resize(image_size)
m, n, br, dv, pixels, blurred_pixels = image_size[0], image_size[1], blurr_radius, (2*blurr_radius+1)**2, list(image.getdata()), []
blurred_pixels = pixels[:]

for k in range(blurr_intensity):
    pixels = blurred_pixels[:]
    for i in range(m):
        for j in range(n):
            r, g, b = 0, 0, 0
            for x in range(-br,br+1):
                for y in range(-br,br+1):
                    try:
                        p = pixels[(i+x)*m+j+y]
                        r, g, b = r+p[0], g+p[1], b+p[2]
                    except: pass
            blurred_pixels[i*m+j] = ((r//dv,g//dv,b//dv))


blurred_image = Image.new(image_mode,image_size)
blurred_image.putdata(blurred_pixels)
blurred_image.save('blurred.jpg')
image.show()
blurred_image.show()
