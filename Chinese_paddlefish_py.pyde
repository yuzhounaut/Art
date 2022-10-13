def setup():
    global f
    frameRate(60)
    global img
    size(1920,823)
    img = loadImage("21-9-1080p.png")
    background(255)
    smooth()

def num_to_string(num):
    numbers = {
        0 : "A",
        1 : "T",
        2 : "C",
        3 : "G"
    }
    
    return numbers.get(num, "A")

def draw(): # draw() loops forever, until stopped
    #Pick a random point
    x = int(random(img.width))
    y = int(random(img.height))
    loc = x + y*img.width
    #Look up the RGB color in the source image
    loadPixels()
    r = red(img.pixels[loc])
    g = green(img.pixels[loc])
    b = blue(img.pixels[loc])
    noStroke()
    
    Sz=random(1,200)
    sz=int(Sz)
    if sz<=198:
        sz=random(13,30)
        sz=int(sz)
    else:
        if(Sz>=170 and Sz<=198):
            sz=random(60,90)
            sz=int(sz)
        else:
            sz=random(120,160)
            sz=int(sz)
    f=createFont("Arial", sz, True)
    textFont(f)
    RD=random(5)
    RD=int(RD)
    Str=num_to_string(RD)
    #use the color from a pixel to draw a letter
    fill(r, g, b, 100)
    text(Str, x, y)
    if frameCount%600 ==0:# every 600 frames
         saveFrame("ATCG-######.png") # save a frame
    
    


    
    
