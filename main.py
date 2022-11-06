import qrcode
from time import strftime, gmtime
class qr:
    def __init__(self):

        self.name = ''

    def fname(self):
        
        rip = self.data.split() # Spilts the QR input by whitespace
        for i in range(len(rip)): # for loop, to cycle through rip then builds a file name 
            if i > 2:
                break
            self.name = self.name + rip[i]
        self.name = self.name + strftime('%m%d%y',gmtime()) + '.png'
        return self.name # returns the name of the file
    
    def generate_qr(self, data, save):
        self.data = data
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
        
        if save == 1:
            print("saving img ")
            img.save(name)        
        
        return img
if __name__ == '__main__':
    usr = input("Please Enter the QR code Value, follwed True or False:  ")
    i_put  = usr.split(',')
    print(qr().generate_qr('Sam Mesic is the best', 0))