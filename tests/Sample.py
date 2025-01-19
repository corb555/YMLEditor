import platform
import sys

# Handle imports for PyQt6 versus PySide
try:
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, \
            QSpacerItem, QSizePolicy, QStyleFactory
except ImportError:
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, \
            QSpacerItem, QSizePolicy, QStyleFactory

from YMLEditor.settings_widget import SettingsWidget
from YMLEditor.yaml_config import YamlConfig

"""
A sample application that loads data from a YAML config file, initializes
the SettingsWidget for displaying and editing settings, and provides a save button
and an undo button.
"""

def create_window(wn, settings):
    """
    Creates the main application window with the settings widget.
    """
    layout = QVBoxLayout()

    # Create a horizontal button layout for save and undo buttons
    button_bar = QHBoxLayout()

    # Create and add Save button linked to settings.save()
    button_width = 80
    save_button = QPushButton("Save")
    save_button.clicked.connect(settings.save)
    save_button.setFixedWidth(button_width)
    button_bar.addWidget(save_button)

    # Create and add Undo button linked to settings.undo()
    undo_button = QPushButton("Undo")
    undo_button.clicked.connect(settings.undo)
    undo_button.setFixedWidth(button_width)
    button_bar.addWidget(undo_button)

    # Set up the display with the settings widget and buttons
    layout.addWidget(settings)
    layout.addLayout(button_bar)
    vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    layout.addItem(vertical_spacer)

    wn.setLayout(layout)

def _exec(obj):
    # PySide and PyQT handle exec differently
    if hasattr(obj, 'exec'):
        return obj.exec()
    else:
        return obj.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if platform.system() == "Darwin":
        style_name = "MacOs"
        app.setStyle(QStyleFactory.create(style_name))

    # Set background color for read only fields
    # Set other widget colors to your preference here
    if False:
        app.setStyleSheet(
            f"""
                    QLineEdit:read-only {{
                        color:"lightslategray"; 
                        background-color:"#3a3a3a";
                        outline:none; 
                        border:none;
                    }}
                    """
        )

    # Create the layout for the fields in the "tests/sample.yml" file.
    formats = {
        "layout1": {
            "TIP": ("Tip Amount", "line_edit", r'^\d{1,2}$', 50),
            "DESSERT": ("Dessert", "combo", ["Tiramisu", "Apple Tart", "Cheesecake"], 200),
            "HOME": ("Home", "combo", ["A", "B", "C", "D"], 200),
            "SITES.@HOME": ("Preferred", "read_only", None, 180, "color: slategray;"),
            "SITES.B": ("Location B", "line_edit", None, 180),
            "SITES": ("Sites", "line_edit", None, 500),
            "BRIGHT": ("Brightness", "slider", [0, 10], 200),
            "EXPERT": ("Expert", "checkbox", None, 200),
            "VALUE": ("Value", "spinbox", [-.5, 1.5, .1, 1], 200),
        },
    }

    # Load YAML config file
    config = YamlConfig()
    success = config.load("sample.yml")
    if not success:
        sys.exit()

    w = QWidget()

    # Create a settings widget to display and edit the YAML settings with our format
    settings_widget = SettingsWidget(config, formats, "layout1", ["HOME"], verbose=2)

    # Create main window and add the settings_widget and buttons
    create_window(w, settings_widget)

    # Display the settings
    settings_widget.display()
    w.show()

    # Start QT App event loop
    sys.exit(_exec(app))
