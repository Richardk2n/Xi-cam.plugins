from qtpy.QtCore import *
from qtpy.QtWidgets import *
from yapsy.IPlugin import IPlugin


class ControllerPlugin(QWidget, IPlugin):
    isSingleton = False

    def __init__(self, device, parent=None, *args):
        self.device = device
        IPlugin.__init__(self)
        QWidget.__init__(
            self, parent, *args
        )  # TODO: Strange MRO, not sure why QWidget init isn't being called; replaced by IPlugin init twice?


def test_QWidgetPlugin():
    from pyqtgraph import ImageView

    class ImageViewPlugin(ControllerPlugin, ImageView):
        pass

    app = makeapp()
    i = ImageViewPlugin()
    i.show()
    t = QTimer()
    t.singleShot(1000, i.close)
    mainloop()


def makeapp():
    app = QApplication([])
    return app


def mainloop():
    app = QApplication.instance()
    app.exec_()
