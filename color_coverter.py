import sys
print(sys.path)

from PIL import Image, ImageDraw



def main():
    #ask the user for an image file they would like to change the colors of
    #defin the image file into a varible and assign it double quotes
    image_file = ("")
    image_file = input("what is the chart, or image you would like to upload?")
    #print a list of different types of color blindness to cutomize to
    #assign each type a number to make it easier for the user to input the type
    print()
    print("What is your type of color blindness:")
    print("1. deuteranomaly ")
    print("2. protanopia ")
    print("3. tritanopia ")
    print("4. complete color blindness ")
    
    #ask the user for the type of colorblindness
    value_scale = input("Which type of color value scale would you like to convert to?")

    #assign a varible to function to open, display, get the pixels, find the width and height,
    #and create a new image for the image the user input
    user_image = open_image(image_file)
    show_image(user_image)
    user_pixels = get_pixels(user_image)
    (width, height) = user_image.size
    new_color_image = new_image(user_image)
   


    # create if statements to lanch the correct function depending on the user input

    if value_scale == "1":
        deuteranomaly_colors(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "2":
        protanopia_colors(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "3":
        tritanopia_colors(user_image, user_pixels, new_color_image, width, height)
    if value_scale == "4":
        complete_color_blindness(user_image)
    else: 
        print("I'm sorry, that is not a valid option")

#create a function that will open and read and return the file given by the user
def open_image(image_file):
    color_image = Image.open(image_file)
    return color_image

#display the original un edited image file to the user
def show_image(user_image):
    user_image.show()

#create a new image for the new color values to be added to   
def new_image(user_image):
    output_image = Image.new("RGB", user_image.size)
    return output_image

#get the pixels from the image file given by the user
def get_pixels(user_image):

    pixels_image = user_image.load()
    return pixels_image





def deuteranomaly_colors(user_image, user_pixels, new_color_image, width, height):
    """ Unable to percieve green light. Deuteranomaly  is the most common type of color blindness. 
    it is also known as red/green color blindness. It makes red look brownish/yellowish. 
    It makes yellow and green look beige. and it makes it difficult to tell blue and violet apart. 
    this function will determine any pixels within the file that have colors that are hard
    for people with Deuteranomaly to tell apart and change them to a color they 
    can easily tell apart. Don't use red/green/brown/orange together. """
    
    


    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (255, 0, 0)
    
    threshold = 230

    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * 1.50)
                g = int(g * .25)
                b = int(b * .25)
            draw.point((x, y), (r, g, b))
    
    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")


def protanopia_colors(user_image, user_pixels, new_color_image, width, height):
    """ it is also known as red/green color blindness. Protanopia happens
    when there are no working red cones, making it impossible
    to see the color red. orange, yellow and green look yellow. this function will 
    determine any pixels within the file that have colors that are hard
    for people with protanopia to tell apart and change them to a color they 
    can easily tell apart."""

    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (255, 0, 0)
    threshold = 230


    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * .50)
                g = int(g * .50)
                b = int(b * 1.25)
            draw.point((x, y), (r, g, b))

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")

#there is one type of Blue /yellow color blindness

def tritanopia_colors(user_image, user_pixels, new_color_image, width, height):
    """this is also known as blue/yellow color blindness. it is the 2nd most common
    type of colorblindness. there are no blue cone cells. blue looks green
    yellow looks light gray or violet """

    def distance2(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

    color_to_change = (0, 255, 0)
    
    threshold = 230


    # Create output image
    
    draw = ImageDraw.Draw(new_color_image)

    # Generate image
    for x in range(width):
        for y in range(height):
            r, g, b = user_pixels[x, y]
            if distance2(color_to_change, user_pixels[x, y]) < threshold ** 2:
                r = int(r * 1.00)
                g = int(g * .25)
                b = int(b * 1.50)

            
            draw.point((x, y), (r, g, b))

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")

#make a function for the third type of color blindness. complete color blindness

def complete_color_blindness(user_image):
    """this is the most rare color blindness someone can have. you have no 
    color perseption at all. making the world gray, white, and black. it is 
    very hard to tell color apart from each other. this function will take each color
    and put it into a gray scale version of that color making it easier for people
    with complete colorblindness to tell values apart"""

    new_color_image = user_image.convert("L")

    #display and save the new image
    new_color_image.show()
    new_color_image.save("new_image.png")

#Color combinations to avoid for people with color blindness include:
#Red & green
#Green & brown
#Green & blue
#Blue & gray
#Blue & purple
#Green & gray
#Green & black
if __name__ == "__main__":      
    main()