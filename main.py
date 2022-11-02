import qrcode
class qr:
    def __init__(self, data):
        self.data = data
        self.name = ''

    def fname(self):
        name = self.name
        rip = self.data.split() # Spilts the QR input by whitespace
        for i in range(len(rip)): # for loop, to cycle through rip then builds a file name 
            name = name + rip[i]
        name = name + '.png'
        return name # returns the name of the file
    
    def generate_qr(self, save):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10, 
            border = 4,
        )
        qr.add_data(self.data)
        qr.make(fit = True)
        img = qr.make_image(fill_color="black", back_color="white") # Photo color settings 
        name = self.fname() # Call function to provide a file name 
        if save.strip() == 'True' or save.strip() == "T": # Checks to see if the img should be save or not
            img.save(name)        
        return img
if __name__ == '__main__':
    usr = input("Please Enter the QR code Value, follwed True or False:  ")
    i_put  = usr.split(',')
    qr(i_put[0]).generate_qr(i_put[1])