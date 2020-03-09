from PIL import Image

image_url = 'jw.jpg'
image_size = (300,300)
image_mode = 'RGB'

image = Image.open(image_url).resize(image_size)
m, n, pixels, blurred_pixels = image_size[0], image_size[1], list(image.getdata()), []

for i in range(m):
    for j in range(n):
        try: a = pixels[i*m+j-1]
        except: a = (0,0,0)
        try: b = pixels[i*m+j+1]
        except: b = (0,0,0)
        try: c = pixels[(i-1)*m+j]
        except: c = (0,0,0)
        try: d = pixels[(i+1)*m+j]
        except: d = (0,0,0)
        blurred_pixels.append(((a[0]+b[0]+c[0]+d[0])//4, (a[1]+b[1]+c[1]+d[1])//4, (a[2]+b[2]+c[2]+d[2])//4))


blurred_image = Image.new(image_mode,image_size)
blurred_image.putdata(blurred_pixels)
image.show()
blurred_image.show()
