import json
import time
from typing import List, Tuple

import websocket
from ttfquery import describe
from ttfquery import glyphquery
import ttfquery.glyph as glyph


class FigureDrawer:

    def __init__(self):
        self.ws = websocket.create_connection("wss://drawserver.jonay2000.nl/")

    def print_cross(self):
        x = 0
        y = 0
        for i in range(50):
            x += 2
            y += 2

            obj = {"x": x, "y": y}
            self.ws.send(json.dumps(obj))

            print(x, y)
            time.sleep(0.001)

        obj2 = {"x": -1, "y": -1}
        self.ws.send(json.dumps(obj2))

        x = 100
        y = 0
        for i in range(50):
            x -= 2
            y += 2

            obj = {"x": x, "y": y}
            self.ws.send(json.dumps(obj))

            print(x, y)
            time.sleep(0.001)


    def print_image(self, coords: str, x_offset, y_offset, scaling):

        coords_shapes = coords.split("\n")
        coords_shapes = list(filter(None, coords_shapes))

        parsed_coords = []

        for i in range(len(coords_shapes)):
            curr_string = coords_shapes[i]
            curr_string = curr_string\
                .replace(" ", "")\

            curr_coords = curr_string.split("),(")

            curr_parsed_coords = []

            for y in range(len(curr_coords)):
                curr_coord = curr_coords[y]

                curr_numbers = curr_coord\
                    .replace("(", "")\
                    .replace(")", "")\
                    .split(",")

                curr_parsed_coords.append(curr_numbers)

            parsed_coords.append(curr_parsed_coords)

        print(parsed_coords)
        self.print_coords(parsed_coords, x_offset, y_offset, scaling)

    def print_text(self, text: Tuple[str, str], x_offset, y_offset, scaling):

        curr_offset = 0

        chars = text[0]
        font_file = text[1]

        for char in chars:
            font = describe.openFont(f"fonts/{font_file}.ttf")
            glyph_name = font["cmap"].getBestCmap().get(ord(char))
            g = glyph.Glyph(glyph_name)

            contours = g.calculateContours(font)

            coords_list = []

            largest_point = -10000

            for c in range(len(contours)):
                countour = contours[c]

                curr_coords = []

                for i in range(len(countour)):
                    point = countour[i][0]
                    x = point[0] + curr_offset
                    y = point[1]
                    curr_coords.append([x * 0.05, y * 0.05])

                    if point[0] > largest_point:
                        largest_point = point[0]


                coords_list.append(curr_coords)

            curr_offset += (largest_point + 5)

            self.print_coords(coords_list, x_offset, y_offset, scaling)


    def print_coords(self, coords, x_offset, y_offset, scaling):

        for i in range(len(coords)):
            curr_shape = coords[i]
            for j in range(len(curr_shape)):
                curr_coord = curr_shape[j]

                x_coord = float(curr_coord[0]) * scaling
                y_coord = float(curr_coord[1]) * scaling
                obj = {"x": x_coord + 50 + x_offset, "y": 50 - y_coord - y_offset}

                print(obj)
                self.ws.send(json.dumps(obj))

                time.sleep(0.001)

            obj2 = {"x": -1, "y": -1}
            print(obj2)
            self.ws.send(json.dumps(obj2))


    def clear(self):
        for i in range(2048):
            obj = {"x": 1, "y": 1}
            self.ws.send(json.dumps(obj))
            time.sleep(0.001)

        obj = {"x": -1, "y": -1}
        self.ws.send(json.dumps(obj))
