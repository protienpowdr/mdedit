"""
This file is a part of MDEdit
Written by Baibhav Bhattacharya
LICENSED under GPLv3 2026
"""


from PySide6.QtGui import QIcon, QFontDatabase, QFont

class AppAsset():
    _font_oswald_path = "assets/fonts/oswald.ttf"
    _font_jetbrains_path = "assets/fonts/jetbrains-mono.ttf"
    _font_trebuchet_path = "assets/fonts/trebuc.ttf"
    _app_title = "MDEdit2"
    _app_icon = "assets/icons/appicon.png"
    _app_geometry = (200,200,1280,720)
    _stylesheet_path = "styles/"
    _preview_theme_path = "themes/"
    _oswald_id = 0
    _jetbrains_id = 0
    _trebuchet_id = 0
    _font_weights = {
        "bold" : QFont.Weight.Bold,
        "black" : QFont.Weight.Black,
        "extrabold" : QFont.Weight.ExtraBold,
        "demibold" : QFont.Weight.DemiBold,
        "normal" : QFont.Weight.Normal,
        "light" : QFont.Weight.Light,
        "extralight" : QFont.Weight.ExtraLight,

    }


    @classmethod
    def load_fonts(cls):
        cls._oswald_id = QFontDatabase.addApplicationFont(cls._font_oswald_path)
        cls._jetbrains_id= QFontDatabase.addApplicationFont(cls._font_jetbrains_path)
        cls._trebuchet_id= QFontDatabase.addApplicationFont(cls._font_trebuchet_path)

    @classmethod
    def Oswald(cls,size=16,weight="normal",italic=False):
        families = QFontDatabase.applicationFontFamilies(cls._oswald_id)
        qtweight = cls._font_weights[weight.lower()]
        return QFont(families[0],size,qtweight,italic)

    @classmethod
    def Jetbrains(cls, size=16, weight="normal", italic=False):
        families = QFontDatabase.applicationFontFamilies(cls._jetbrains_id)
        qtweight = cls._font_weights[weight.lower()]
        return QFont(families[0], size, qtweight, italic)

    @classmethod
    def Trebuchet(cls, size=16, weight="normal", italic=False):
        families = QFontDatabase.applicationFontFamilies(cls._trebuchet_id)
        qtweight = cls._font_weights[weight.lower()]
        return QFont(families[0], size, qtweight, italic)

    @classmethod
    def Icon(cls):
        return QIcon(cls._app_icon)

    @classmethod
    def Title(cls):
        return cls._app_title

    @classmethod
    def BaseGeometry(cls):
        return cls._app_geometry




class AppStyles:
    app_styles_directory= "styles/"