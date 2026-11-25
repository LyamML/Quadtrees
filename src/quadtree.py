from __future__ import annotations
import ast
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg
        self.quadrants = [hg, hd, bd, bg]

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        depth_count = 1
        children_depth = []
        for quadrant in self.quadrants:
            if isinstance(quadrant, QuadTree):
                children_depth.append(quadrant.depth)
            else:
                children_depth.append(0)
        return 1 + max(children_depth)

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, 'r', encoding ='utf-8') as f:
            f.seek(0) # Remettre au début du fichier au cas ou
            file_as_list = ast.literal_eval(f.read())
        return QuadTree.fromList(file_as_list)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        result = []
        for item in data:
            if isinstance(item, list):
                result.append(QuadTree.fromList(item))
            else:
                result.append(item)
        return QuadTree(result[0], result[1], result[2], result[3])

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass
