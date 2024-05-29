# устанавливаем pyqrcode и pupng


import pyqrcode


qr = 'https://gasoil.uz'

cr = pyqrcode.create(qr)

cr.png('qr.png', scale=8)