class Pixel:
    def __init__(self, x, y,r=0,g=0,b=0):
        self._x = x
        self._y = y
        self._red = r
        self._green = g
        self._blue = b

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_colors(self, r, g, b):
        self._red = r
        self._green = g
        self._blue = b

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue)//3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        string_color = ''
        if(self._red!= self._green and self._green==self._blue):
            string_color = "Red"
        if(self._green!= self._red and self._red==self._blue):
            string_color = "Green"
        if(self._blue!= self._red and self._red==self._green):
            string_color = "Blue"

        print("X: {0}, Y: {1}, Color: ({2}, {3}, {4}) {5}".format(self._x, self._y, self._red, self._green, self._blue,string_color))


def main():
    p1 = Pixel(5, 6,250)
    p1.print_pixel_info()
    p1.set_grayscale()
    p1.print_pixel_info()


main()
