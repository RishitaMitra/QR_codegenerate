#QR code generate for any link with some edits 

import qrcode
#from PIL import Image
#img = qr.make("https://www.linkedin.com/in/rishita-mitra-242716226")

#img.save("Rishita_LinkedIn.png")

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
qr.add_data("https://www.linkedin.com/in/rishita-mitra-242716226")
qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="black")
img.save("linkdin_Rishita.png")
