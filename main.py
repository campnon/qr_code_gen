import qrcode
class qr:
    def __init__(self, data):
        self.data = data
        self.name = ''

    def fname(self):
        name = self.name
        rip = self.data.split()
        for i in range(len(rip)):
            name = name + rip[i]
        name = name + '.png'
        return name
    
    def generate_qr(self, save):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10, 
            border = 4,
        )
        qr.add_data(self.data)
        qr.make(fit = True)
        img = qr.make_image(fill_color="black", back_color="white")
        name = self.fname()
        if save.strip() == 'True' or save.strip() == "T":
            img.save(name)
            print("Saving...")
        print(img)
        
        return img
if __name__ == '__main__':
    usr = input("Please Enter the QR code Value, follwed True or False:  ")
    i_put  = usr.split(',')
    qr(i_put[0]).generate_qr(i_put[1])