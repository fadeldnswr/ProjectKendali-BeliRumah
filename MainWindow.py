# Imported UI Files
from FrontUIVer110 import Ui_MainWindow
from Account import Account
import AppIcons_rc

# Needed Libraries
import time
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class MainWindow(QMainWindow, Ui_MainWindow):

    # Window Setup and Settings
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.accounts = Account()

        # Stored Flags
        self.is_login = False
        self.is_match = False
        self.is_this_button_clicked = False

        # Variables to store the position of the mouse
        self._is_dragging = False
        self._start_pos = None

        # Enable Scrolling to Content Page and Display Content Page

        # Connect buttons to close, minimize, and maximize the program
        self.CloseButton.clicked.connect(self.close_program)
        self.Minimize.clicked.connect(self.minimize_program)
        self.Resize.clicked.connect(self.resize_program)

        # Connect buttons to switch pages
        self.Rumah.clicked.connect(self.list_rumah_page)
        self.Kredit.clicked.connect(self.kredit_page)
        self.Beli.clicked.connect(self.beli_page)
        self.Bantuan.clicked.connect(self.bantuan_page)
        self.Pengaturan.clicked.connect(self.pengaturan_page)
        self.User.clicked.connect(self.user_page)
        self.Notifcation.clicked.connect(self.notification_page)
        self.Preferences.clicked.connect(self.preferences_page)
        self.ProfileLoginButton.clicked.connect(self.login_page)
        self.ProfileRegisterButton.clicked.connect(self.register_page)
        
        # Navigation Buttons
        self.GoBackToHomeButton.clicked.connect(self.list_rumah_page)
        self.ProfilePageExitButton.clicked.connect(self.close_notification_page)
        self.NotificationsCloseContainerButton.clicked.connect(self.close_notification_page)
        self.SearchPreferencesCloseButton.clicked.connect(self.close_notification_page)

        # User Account
        self.LoginButton.clicked.connect(self.process_login)
        self.BuatAkunButton.clicked.connect(self.process_account_creation)
        self.SimpanDataButton.clicked.connect(self.process_account_data)

# Program Panel Functions______________________________________________________________________________________________________________________
    def mouse_press_event(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._is_dragging = True
            self._start_pos = event.pos()

    def mouse_move_event(self, event):
        if self._is_dragging:
            self.move(self.pos() + event.pos() - self._start_pos)

    def mouse_release_event(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._is_dragging = False

    def close_program(self):
        self.close()
    
    def minimize_program(self):
        self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), self.width(), 0))
        self.showMinimized()

    def resize_program(self):
        if self.isMaximized():
            self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), 800, 600))
            self.showNormal()
        else:
            self.animate_window(QRect(self.x(), self.y(), self.width(), self.height()), QRect(self.x(), self.y(), self.screen().size().width(), self.screen().size().height()))
            self.showMaximized()

    def animate_window(self, start_rect, end_rect):
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(500)  # Duration in milliseconds
        animation.setStartValue(start_rect)
        animation.setEndValue(end_rect)
        animation.start()

# Page Switching Functions______________________________________________________________________________________________________________________
    def list_rumah_page(self):
        self.ContentFrame.setCurrentIndex(0)

    def kredit_page(self):
        self.ContentFrame.setCurrentIndex(3)

    def beli_page(self):
        self.ContentFrame.setCurrentIndex(4)

    def bantuan_page(self):
        self.ContentFrame.setCurrentIndex(5)

    def pengaturan_page(self):
        self.ContentFrame.setCurrentIndex(6)

    def user_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()

        if self.is_login == False:
            self.ProfilePagePhotoContainer.hide()
            self.DashboardControlContainer.hide()
            self.ProfilePageLoginContainer.show()
        else:
            self.ProfilePagePhotoContainer.show()
            self.DashboardControlContainer.show()
            self.ProfilePageLoginContainer.hide()

        self.NotificatioFrame.setCurrentIndex(0)

    def notification_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()
        self.NotificatioFrame.setCurrentIndex(1)

    def preferences_page(self):
        if self.NotificatioFrame.isVisible():
            self.NotificatioFrame.hide()
        else:
            self.NotificatioFrame.show()
        self.NotificatioFrame.setCurrentIndex(2)    

    def close_notification_page(self):
        self.NotificatioFrame.hide()

# Account Functions______________________________________________________________________________________________________________________
    # Login Functions
    def login_page(self):
        self.LoginLabelStatus.hide()
        self.NotificatioFrame.hide()
        self.ContentFrame.setCurrentIndex(1)

    def process_login(self):
        parse_username = self.UsernameBox.toPlainText()
        parse_password = self.PasswordBox.toPlainText()
        # print(parse_username, parse_password) Debugg Purpose
        self.is_login = self.accounts.user_login(parse_username, parse_password)
        
        if self.is_login == True:
            self.LoginLabelStatus.show()
            self.LoginLabelStatus.setText("Selamat Datang!")
            time.sleep(2)
            self.ContentFrame.setCurrentIndex(0)
            self.ProfilePageLoginContainer.hide()
        else:
            self.LoginLabelStatus.show()
            time.sleep(2)
            self.LoginLabelStatus.setText("Username atau Password Salah!")

    # Register Functions
    def register_page(self):
        self.RegisterFlag.hide()
        self.NotificatioFrame.hide()
        self.ContentFrame.setCurrentIndex(2)
        self.KolomData.hide()

    def register_data_page(self):
        self.SavedFlag.hide()
        self.KolomAkun.hide()
        self.KolomData.show()

    def process_account_creation(self):
        parse_username = self.BuatUserBox.toPlainText()
        parse_password = self.BuatPasswordBox.toPlainText()
        parse_repassword = self.BuatRePasswordBox.toPlainText()
        self.is_match = self.accounts.create_account_username_password(parse_username, parse_password, parse_repassword)

        if self.is_match == True:
            self.RegisterFlag.show()
            self.RegisterFlag.setText("Selamat Akun Anda Telah Dibuat!")
            time.sleep(2)
            self.register_data_page()
        else:
            self.RegisterFlag.show()
            self.RegisterFlag.setText("Password Tidak Cocok!")
            time.sleep(2)
            self.RegisterFlag.setText("Silahkan Coba Lagi!")
    
    def process_account_data(self):
        parse_nama = self.NamaBox.toPlainText()
        parse_pekerjaan = self.PekerjaanBox.toPlainText()
        parse_gaji = self.GajiBox.toPlainText()
        parse_tempat_kerja = self.TempatKerjaBox.toPlainText()
        parse_tanggungan = self.TanggunganBox.toPlainText()
        parse_cicilan = self.CicilanBox.toPlainText()
        parse_tabungan = self.TabunganBox.toPlainText()
        self.accounts.create_account_data(parse_nama, parse_pekerjaan, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan)
        time.sleep(2)
        self.SavedFlag.show()
        self.SavedFlag.setText("Data Anda Telah Tersimpan!")
        time.sleep(2)
        self.is_login = True
        self.ContentFrame.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
