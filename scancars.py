# ScanCARS v1
# Software to control the SIPCARS experimental setup
# Priyank Shah - King's College London

import sys
import time
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore

from guiForms import WindowMAIN
from guiFunctions import toggle, post
from guiFunctions.graphing import *
from guiMain.InitializeAndor import *

from ADwinSDK import ADwin
from AndorSDK.pyandor import Andor


class ScanCARS(QMainWindow, WindowMAIN.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ScanCARS, self).__init__(parent)
        self.setupUi(self)

        # TODO Add options to take individual pump/Stokes. Will depend on being able to code up some shutters.
        # TODO Change textboxes to spin boxes where relevant
        # TODO If speed becomes an issue, consider using numba package with jit decorator
            # Required to use maths functions instead of numpy
        # TODO Move all non-GUI functions to separate threads

        # ------------------------------------------------------------------------------------------------------------
        # Creating variables for tracks (perhaps create function here instead)
        self.track1 = None
        self.track2 = None
        self.trackdiff = None
        self.tracksum = None

        # Main: connecting buttons to functions
        self.Main_start_acq.clicked.connect(lambda: self.main_startacq())
        self.Main_shutdown.clicked.connect(lambda: self.main_shutdown())

        # CameraTemp: connecting buttons to functions
        self.CameraTemp_cooler_on.clicked.connect(lambda: self.cameratemp_cooler())

        # SpectraWin: connecting buttons to functions
        self.SpectraWin_single_track.clicked.connect(lambda: self.spectrawin_tracks())
        self.SpectraWin_sum_track.clicked.connect(lambda: self.spectrawin_sum())

        # Grating: connecting buttons to functions
        self.Grating_update.clicked.connect(lambda: self.grating_update())

        # CameraOptions: connecting buttons to functions
        self.CameraOptions_update.clicked.connect(lambda: self.cameraoptions_update())
        self.CameraOptions_openimage.clicked.connect(lambda: self.cameraoptions_openimage())

        # SpectralAcq: connecting buttons to functions
        self.SpectralAcq_update_time.clicked.connect(lambda: self.spectralacq_updatetime())
        self.SpectralAcq_start.clicked.connect(lambda: self.spectralacq_start())

        # HyperAcq: connecting buttons to functions
        self.HyperAcq_start.clicked.connect(lambda: self.hyperacq_start())

        # ------------------------------------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------------------------------------
        # Startup Processes
        post.event_date(self)
        toggle.deactivate_buttons(self)

        # Initializing the camera
        self.cam = Andor()
        self.post = post
        # self.initialize_andor()

        self.threadpool = QtCore.QThreadPool()
        initializeandor = InitializeAndor(self)
        self.threadpool.start(initializeandor)

        toggle.activate_buttons(self)
        # ------------------------------------------------------------------------------------------------------------

    def __del__(self):
        post.eventlog(self, 'An error has occurred. This program will exit after the Andor camera has shut down.')

        messageCoolerOFF = self.cam.CoolerOFF()
        if messageCoolerOFF is not None:
            post.eventlog(self, messageCoolerOFF)

        messageShutDown = self.cam.ShutDown()
        if messageShutDown is not None:
            post.eventlog(self, messageShutDown)

    # Initialization functions (Andor and ADwin)
    def initialize_andor(self):
        # Initializing the camera
        messageInitialize = self.cam.Initialize()
        if messageInitialize is not None:
            post.eventlog(self, messageInitialize)
            return

        # Setting the shutter
        messageSetShutter = self.cam.SetShutter(1, 2, 0, 0)
        if messageSetShutter is not None:
            post.eventlog(self, messageSetShutter)
            return

        # Setting read mode to Random Track and setting track positions
        messageSetReadMode = self.cam.SetReadMode(2)
        if messageSetReadMode is not None:
            post.eventlog(self, messageSetReadMode)
            return

        RandomTrackposition = np.array([int(self.CameraOptions_track1lower.text()),
                                        int(self.CameraOptions_track1upper.text()),
                                        int(self.CameraOptions_track2lower.text()),
                                        int(self.CameraOptions_track2upper.text())])

        messageSetRandomTrack = self.cam.SetRandomTracks(2, RandomTrackposition)
        if messageSetRandomTrack is not None:
            post.eventlog(self, messageSetRandomTrack)
            return

        # Getting and setting AD channel
        messageGetNumberADChannels = self.cam.GetNumberADChannels()
        if messageGetNumberADChannels is not None:
            post.eventlog(self, messageGetNumberADChannels)
            return

        messageSetADChannel = self.cam.SetADChannel(1)
        if messageSetADChannel is not None:
            post.eventlog(self, messageSetADChannel)
            return

        # Setting trigger mode
        messageSetTriggerMode = self.cam.SetTriggerMode(0)
        if messageSetRandomTrack is not None:
            post.eventlog(self, messageSetRandomTrack)
            return

        # Getting the detector chip size
        messageGetDetector = self.cam.GetDetector()
        if messageGetDetector is not None:
            post.eventlog(self, messageGetDetector)
            return

        # Setting horizontal and vertical shift speeds
        messageSetHSSpeed = self.cam.SetHSSpeed(1, 0)
        if messageSetHSSpeed is not None:
            post.eventlog(self, messageSetHSSpeed)
            return

        messageSetVSSpeed = self.cam.SetVSSpeed(3)
        if messageSetVSSpeed is not None:
            post.eventlog(self, messageSetVSSpeed)
            return

        post.eventlog(self, 'Andor: Successfully initialized.')

    def initialize_adwin(self):
        pass

    # Main: defining functions
    def main_startacq(self):
        # If acquisition is not alreadly running:
        if self.Main_start_acq.text() == 'Start Acquisition':
            # Setting the acquisition mode to single scan
            messageSetAcquisitionMode = self.cam.SetAcquisitionMode(1)
            if messageSetAcquisitionMode is not None:
                post.eventlog(self, messageSetAcquisitionMode)
                return

            messageSetExposureTime = self.cam.SetExposureTime(float(self.SpectralAcq_time_req.text()))
            if messageSetExposureTime is not None:
                post.eventlog(self, messageSetExposureTime)
                return

            messageGetAcquisitionTimings = self.cam.GetAcquisitionTimings()
            if messageGetAcquisitionTimings is not None:
                post.eventlog(self, messageGetAcquisitionTimings)
                return
            else:
                self.SpectralAcq_actual_time.setText(str("%.4f" % round(self.cam.exposure, 4)))

            messageSetShutter = self.cam.SetShutter(1, 0, 0, 0)
            if messageSetShutter is not None:
                post.eventlog(self, messageSetShutter)
                return

            # ... functions to start acquiring ...

            messageStartAcquisition = self.cam.StartAcquisition()
            if messageStartAcquisition is not None:
                post.eventlog(self, messageStartAcquisition)
                self.cam.AbortAcquisition()
                return
            else:
                # post.status(self, 'Acquiring...')
                # self.Main_start_acq.setText('Stop Acquisition')

                self.cam.GetAcquiredData16()

                post.eventlog(self, str(type(self.cam.imagearray)))

                # self.track1 = self.cam.imagearray[0:self.cam.width-1]
                # self.track2 = self.cam.imagearray[self.cam.width:2*self.cam.width - 1]
                # self.trackdiff = self.track2 - self.track1
                # self.tracksum = self.track1 + self.track2

                # # Plotting tracks and different spectra
                # self.Main_specwin.clear()
                # self.Main_specwin.plot(self.track1, pen='r', name='track1')
                # self.Main_specwin.plot(self.track2, pen='g', name='track2')
                # self.Main_specwin.plot(self.trackdiff, pen='w', name='trackdiff')

            post.status(self, 'Acquiring...')

        # If acquisition is to be stopped:
        elif self.Main_start_acq.text() == 'Stop Acquisition':
            post.status(self, '')
            self.Main_start_acq.setText('Start Acquisition')

    def main_shutdown(self):
        messageCoolerOFF = self.cam.CoolerOFF()
        if messageCoolerOFF is not None:
            post.eventlog(self, messageCoolerOFF)

        else:
            post.eventlog(self, 'Andor: Waiting for camera to heat up (~ 2.5 minutes)...')
            time.sleep(150)

            messageShutDown = self.cam.ShutDown()
            if messageShutDown is not None:
                post.eventlog(self, messageShutDown)

    # CameraTemp: defining functions
    def cameratemp_cooler(self):
        tempreq = int(self.CameraTemp_temp_req.text())
        self.cam.SetTemperature(tempreq)
        self.cam.CoolerON()

    # SpectraWin: defining functions
    def spectrawin_tracks(self):
        pass

    def spectrawin_sum(self):
        pass

    # Grating: defining functions
    def grating_update(self):
        pass

    # CameraOptions: defining functions
    def cameraoptions_update(self):
        RandomTrackposition = [int(self.CameraOptions_track1lower.text()),
                               int(self.CameraOptions_track1upper.text()),
                               int(self.CameraOptions_track2lower.text()),
                               int(self.CameraOptions_track2upper.text())]

        messageSetRandomTrack = self.cam.SetRandomTracks(2, RandomTrackposition)
        if messageSetRandomTrack is not None:
            post.eventlog(self, messageSetRandomTrack)

    def cameraoptions_openimage(self):
        pass

    # SpectralAcq: defining functions
    def spectralacq_updatetime(self):
        messageSetExposureTime = self.cam.SetExposureTime(float(self.SpectralAcq_time_req.text()))
        if messageSetExposureTime is not None:
            post.eventlog(self, messageSetExposureTime)

        # To retrieve the data
        # messageGetAcquiredData16 = self.cam.GetAcquiredData16()
        # if messageGetAcquiredData16 is not None:
        #     post.eventlog(self, messageGetAcquiredData16)

    def spectralacq_start(self):
        time_req = float(self.SpectralAcq_update_time.text())
        darkfield_req = int(self.SpectralAcq_darkfield.text())

    # HyperAcq: defining functions
    def hyperacq_start(self):
        xpixel = int(self.HyperAcq_xpixel.text())
        ypixel = int(self.HyperAcq_ypixel.text())
        zpixel = int(self.HyperAcq_zpixel.text())

        xystep = float(self.HyperAcq_xystep.text())
        zstep = float(self.HyperAcq_zstep.text())

        time_req = float(self.HyperAcq_time_req.text())
        darkfield_req = int(self.HyperAcq_darkfield.text())


def main():
    app = QApplication(sys.argv)
    form = ScanCARS()
    form.setWindowTitle('ScanCARS')
    form.show()
    sys.exit(app.exec_())


# If the file is run directly and not imported, this runs the main function
if __name__ == '__main__':
    main()
