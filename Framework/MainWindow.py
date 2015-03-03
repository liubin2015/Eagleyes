# -*- coding: utf-8 -*-
'''
Main Window
'''

__author__ = 'Liu Bin'

from PyQt4.QtGui import (
    QMainWindow, QAction, QKeySequence, QMenuBar,
    QMenu)


class EE_MainWindow(QMainWindow):

    def __init__(self,*args):
        QMainWindow.__init__(self, *args)

        self.setup_actions()
        self.setup_ui()


    def setup_actions(self):
        """
        quit action
        """
        self.quit_action = \
            QAction(self.tr("Quit"), self,
                    objectName="quit-action",
                    toolTip=self.tr("Quit Eagleyes."),
                    menuRole=QAction.QuitRole,
                    shortcut=QKeySequence.Quit,
                    )

    def setup_ui(self):
        menu_bar = QMenuBar()

        file_menu = QMenu(self.tr("&File"), menu_bar)
        file_menu.addAction(self.quit_action)
        menu_bar.addMenu(file_menu)

        self.setMenuBar(menu_bar)