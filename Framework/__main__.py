# -*- coding: utf-8 -*-
"""
main entry point
"""

import sys
import gc

from PyQt4.QtGui import QApplication
from Framework.MainWindow import EE_MainWindow

def main(argv=None):
    if argv is None:
        argv = sys.argv

    app = QApplication(argv)

    main_window = EE_MainWindow()
    main_window.setWindowTitle("Eagleyes")

    main_window.show()
    main_window.raise_()
    app.exec_()
    app.processEvents()
    app.flush()
    del main_window

    # Collect any cycles before deleting the QApplication instance
    gc.collect()

    del app
    return 0


if __name__ == "__main__":
    sys.exit(main())
