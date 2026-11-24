"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""

from PySide6.QtWidgets import QStatusBar,QComboBox,QLabel


class StatusBar(QStatusBar):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.tab_width = QComboBox(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)

        self._initialize_statusbar()
        self._initialize_tab_width()
        self._initialize_label()


    def _initialize_statusbar(self):
        self.setSizeGripEnabled(False)
        self.addWidget(self.label1,stretch=0)
        self.addWidget(self.label2, stretch=0)
        self.addPermanentWidget(self.label3, stretch=0)
        self.addPermanentWidget(self.tab_width, stretch=0)

    def _initialize_label(self):
        self.label1.setText('Developed by Baibhav Bhattacharya')
        self.label2.setText('MDEdit Version 1.0')
        self.label3.setText('Tab Width')

    def _initialize_tab_width(self):
        self.tab_width.addItems(['2','4','6','8'])
        self.tab_width.setCurrentIndex(1)

