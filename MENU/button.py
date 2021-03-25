class Button:
    """
    Propriedades:
        label,
        size,
        offset,
        colors (main_color, alt_color)
    """
    def __init__(self, label, size, offset, colors):
        self.__label = label
        self.__size  = size
        self.__offset = offset
        self.__main_color = colors[0]
        self.__alt_color = colors[1]

    @property
    def label(self):
        return self.__label

    @property
    def size(self):
        return self.__size

    @property
    def offset(self):
        return self.__offset

    @property
    def main_color(self):
        return self.__main_color

    @property
    def alternative_color(self):
        return self.__alt_color

    @property
    def rect(self):
        x0, y0 = self.offset
        dx, dy = self.size
        return [x0, y0, dx, dy]

    def text_offset(self, text_size):
        x0, y0 = self.offset
        dx, dy = self.size
        dxt, dyt = text_size

        xt = x0 + dx // 2 - dxt // 2
        yt = y0 + dy // 2 - dyt // 2
        return xt, yt

    def __contains__(self, point):
        x0, y0 = self.offset
        dx, dy = self.size
        px, py = point

        contains_x = x0 <= px <= x0 + dx
        contains_y = y0 <= py <= y0 + dy

        return contains_x and contains_y