from pydgilib_extra import DGILibExtra, LOGGER_PLOT, LOGGER_CSV, LOGGER_OBJECT
import os
from matplotlib import pyplot as plt

from atprogram.atprogram import atprogram, get_project_size

# Make the plot not show up too big, if you ever used the 
#  "Make everything bigger" option in Windows 10 to set DPI
#  bigger than 100%
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True) 
except:
    pass

dgilib_config = {
    "loggers" : [
        LOGGER_OBJECT, # Have the .log function return a 'data' object you can use
        LOGGER_CSV,
        LOGGER_PLOT    # You can omit this to hide the plot and make everything run silently
    ],
    "plot_pins_colors": ["red", "yellow", "blue", "green"],
    "window_title": "Plot of electric current (in amperes) and GPIO pins",
    "gpio_delay_time": 0.00075, # Default is 0.00075, another value to try is 0.0015
    "log_folder": "../Output",
    "file_name_base": "untitled"
}

# This line below compiles and flashes the Atmel solution to your card
# You have to have had compiled the project at least once
# Verbosity here shows more of the compilation + flashing process
atprogram("../../BeginnerProject-ARM/BeginnerProject", verbose=1) 

with DGILibExtra(**dgilib_config) as dgilib:
    dgilib.device_reset()
    # Afterwards, you have the data in the 'data' object
    data = dgilib.logger.log(10) 

    # Block figure from closing at the end of the script
    plt.show(block=True) 