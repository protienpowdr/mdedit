"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""

from PySide6.QtWidgets import QMenuBar, QMenu
from ui.api import AppInterface as Ai


class Menubar(QMenuBar):
    def __init__(self,parent):
        QMenuBar.__init__(self,parent=parent)

        self.FileMenu = QMenu("&File")
        self.InsertMenu = QMenu("&Insert")
        self.ModeMenu = QMenu("&Appearance")
        self.ThemeMenu = QMenu("&Themes")
        self.ExportMenu = QMenu("&Export")

        self._initialize_file_menu()
        self._initialize_insert_menu()
        self._initialize_mode_menu()
        self._initialize_theme_menu()
        self._initialize_export_menu()
        self._initialize_menubar()


    def _initialize_menubar(self):
        self.addMenu(self.FileMenu)
        self.addMenu(self.InsertMenu)
        self.addMenu(self.ModeMenu)
        self.addMenu(self.ThemeMenu)
        self.addMenu(self.ExportMenu)

    def _initialize_file_menu(self):
        self.FileMenu.addAction("&New", "Ctrl+N", None)
        self.FileMenu.addAction("&Open","Ctrl+O",None)
        self.FileMenu.addAction("&Save", "Ctrl+S", None)
        self.FileMenu.addAction("&Save As...", "Ctrl+Shift+S", None)

    def _initialize_insert_menu(self):
        self.InsertMenu.addAction("<\tLess-than sign")
        self.InsertMenu.addAction(">\tGreater-than sign")
        self.InsertMenu.addAction("&\tAmpersand")
        self.InsertMenu.addAction("©\tCopyright")
        self.InsertMenu.addAction("®\tRegistered trademark")
        self.InsertMenu.addAction("™\tTrademark")
        self.InsertMenu.addAction("—\tEm dash")
        self.InsertMenu.addAction("\"\tDouble quote")
        self.InsertMenu.addAction("•\tBullet point")

    def _initialize_mode_menu(self):
        fn = self.window().get_function(Ai.ChangeAppTheme)
        self.ModeMenu.addAction("&Light","Ctrl+Shift+L", lambda : fn("light"))
        self.ModeMenu.addAction("&Dark", "Ctrl+Shift+D", lambda : fn("dark"))

    def _initialize_theme_menu(self):
        self.ThemeMenu.addAction("Default")
        self.ThemeMenu.addAction("MDEdit Classic Light")
        self.ThemeMenu.addAction("MDEdit Classic Dark")
        self.ThemeMenu.addAction("MDEdit Modern Light")
        self.ThemeMenu.addAction("MDEdit Modern Light")

    def _initialize_export_menu(self):
        self.ExportMenu.addAction("&PDF","Ctrl+Alt+P",None)
        self.ExportMenu.addAction("&HTML","Ctrl+Alt+H",None)


