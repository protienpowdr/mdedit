"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""

from PySide6.QtWidgets import QMainWindow
from ui.misc import  AppAsset
from ui.menubar import Menubar
from ui.api import AppFunctionResolver,AppWidgetResolver
from ui.api import AppWidgetType as Aw
from ui.api import AppInterface as Ai
from ui.uibridge import UiBridge


class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Registry
            self._function_registry = AppFunctionResolver()
            self._widgets_registry = AppWidgetResolver()

            # UiBridge
            self.bridge = UiBridge(self)

            # Base Window Initialization
            self._initialize_window()
            self._initialize_function_registry()
            self._initialize_widget_registry()


            # Widgets
            self.menubar =Menubar(self)

            # Initialize Widgets
            self._initialize_widget_groups()



        def _initialize_window(self):
            self.setWindowTitle(AppAsset.Title())
            self.setWindowIcon(AppAsset.Icon())
            self.setGeometry(*AppAsset.BaseGeometry())

        def _initialize_widget_groups(self):
            self.setMenuBar(self.menubar)

        def _initialize_widget_registry(self):
            pass

        def _initialize_function_registry(self):
            self._function_registry.add_entry(Ai.ChangeAppTheme,self.bridge.change_theme)

        def get_function(self,function : Ai):
            return self._function_registry.get_entry(function)

        def get_widget(self, widget : Aw):
            pass