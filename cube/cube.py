
colors = 'wryobg'
dic_colors = {'w': 0, 'r': 1, 'y':2, 'o': 3, 'b': 4, 'g':5}


# for each face the adjacent squares in each adjacent face organized like : 123 369 987 741
adjacent_square = {'w': {'r': [7,8,9], 'g': [1,4,7], 'o': [3,2,1], 'b': [9,6,3]}, 'r': {'y': [7,8,9], 'g': [3,2,1], 'w': [3,2,1], 'b': [3,2,1]}, 
                   'y': {'o': [7,8,9], 'g': [9,6,3], 'r': [3,2,1], 'b': [1,4,7]}, 'o': {'w': [7,8,9], 'g': [7,8,9], 'y': [3,2,1], 'b': [7,8,9]}, 
                   'b': {'r': [1,4,7], 'w': [1,4,7], 'o': [1,4,7], 'y': [1,4,7]}, 'g': {'r': [9,6,3], 'y': [9,6,3], 'o': [9,6,3], 'w': [9,6,3]}}


def create_faces():
    faces = []
    
    for color in colors:
        faces.append(9*color)

    return faces

class Cube:

    def __init__(self):
        self.faces = create_faces()

    def move_clockwise(self, color):
        face = self.faces[dic_colors[color]]
        new_face = face[6]+face[3]+face[0]+face[7]+'w'+face[1]+face[8]+face[5]+face[2]
        self.faces[dic_colors[color]] = new_face
        prev_indexes = adjacent_square.values()[0].values()[-1]
        prev_face_index = dic_colors[adjacent_square[color].keys()[-1]]
        for adjacent_color in adjacent_square[color].keys():
            face_index=dic_colors[adjacent_color]
            for index,prev_color in adjacent_square[color][adjacent_color].zip(prev_colors):
                self.faces


