from PyQt5.QtWidgets import (QMainWindow,
     QDesktopWidget)
from View.view import Ui_MainWindow
import numpy as np
from node import Node
from node import Puzzle
from node import Distance

class PuzzleView(QMainWindow):
    def __init__(self):
        super(PuzzleView, self).__init__()
        self.puzzleView = Ui_MainWindow()      
        self.puzzleView.setupUi(self)
           
        # centrar ventana
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width())/2),
                  int((screen.height() - size.height())/2))
        
        self.initial_board=[]
        self.final_board=[]
        



        self.puzzleView.btn_sol.clicked.connect(self.start_puzzle)
        # logic inicial board 

    def start_puzzle(self):
        initial_board=[]
        final_board=[]

        initial_board.append(int(self.puzzleView.txt_1.text()))
        initial_board.append(int(self.puzzleView.txt_2.text()))
        initial_board.append(int(self.puzzleView.txt_3.text()))
        initial_board.append(int(self.puzzleView.txt_4.text()))
        initial_board.append(int(self.puzzleView.txt_5.text()))
        initial_board.append(int(self.puzzleView.txt_6.text()))
        initial_board.append(int(self.puzzleView.txt_7.text()))
        initial_board.append(int(self.puzzleView.txt_8.text()))
        initial_board.append(int(self.puzzleView.txt_9.text()))

        
        final_board.append(int(self.puzzleView.final_1.text()))
        final_board.append(int(self.puzzleView.final_2.text()))
        final_board.append(int(self.puzzleView.final_3.text()))
        final_board.append(int(self.puzzleView.final_4.text()))
        final_board.append(int(self.puzzleView.final_5.text()))
        final_board.append(int(self.puzzleView.final_6.text()))
        final_board.append(int(self.puzzleView.final_7.text()))
        final_board.append(int(self.puzzleView.final_8.text()))
        final_board.append(int(self.puzzleView.final_9.text()))


        initial_board   =   Node(initial_board)
        final_board     =   Node(final_board)
        explored_nodes  =   []
        fringe          =   [initial_board]
        distance        =   Distance.distance(initial_board.get_current_state(),final_board.get_current_state(),heuristic=2)
        fringe[0].update_hn(distance)
        count=1

        while not not fringe:
            puzzle  = Puzzle(self.puzzleView.textEdit,
            self.puzzleView.no_nodos_exp,
            self.puzzleView.num_nodos_gen,
            self.puzzleView.costo)
            minimum_fn_index    =   puzzle.least_fn(fringe)
            current_node        =   fringe.pop(minimum_fn_index)
            g                   =   current_node.get_gn()+1
            goal_node           =   np.asarray(final_board.get_current_state())
            if np.array_equal(np.asarray(current_node.get_current_state()), goal_node ):
                distance    =   Distance.distance(np.asarray(current_node.get_current_state()),goal_node,heuristic=2)
                explored_nodes.append(current_node)
                puzzle.goal_reached(explored_nodes,count)
                fringe      =   []
            elif not np.array_equal(current_node, goal_node ):
                zero    =   np.where(np.asarray(current_node.get_current_state()) == 0)[0][0]
                count   =   Node.expand_node(fringe, explored_nodes, current_node,goal_node, zero, g, count,heuristic=2)

                