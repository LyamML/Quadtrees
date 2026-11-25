from __future__ import annotations
import tkinter as tk
import ast
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.quadrants = [hg, hd, bd, bg]

    @property
    def depth(self) -> int:
        """Recursion depth of the quadtree"""
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
        """ 
        Open a given file, containing a textual representation of a list,
        calling the contructor to return a list version of it instead of a string.
        """
        with open(filename, 'r', encoding ='utf-8') as f:
            f.seek(0) # Remettre au début du fichier au cas ou
            file_as_list = ast.literal_eval(f.read())
        return QuadTree.from_list(file_as_list)

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation : Constructor"""
        result = []
        for item in data:
            if isinstance(item, list):
                result.append(QuadTree.from_list(item))
            else:
                result.append(item)
        return QuadTree(*result)

class TkQuadTree(QuadTree):
    def __init__(self, filename):
        q = QuadTree.from_file(filename=filename)
        super().__init__(*q.quadrants)
    def paint(self):
        """ TK representation of a Quadtree in a window"""
        SIZE = 512
        MARGIN = 20

        window = tk.Tk()
        window.title("QuadTree Visualization")
        canvas = tk.Canvas(window, width=SIZE, height=SIZE, bg="lightgrey")



        canvas.pack()
        window.mainloop()

if __name__ == "__main__": # Ligne ajoutée par Claude car la fenetre s'ouvrait en BOUCLE avec mes tests ci-dessous
    quadtreevis = TkQuadTree("files/quadtree.txt")
    quadtreevis.paint()