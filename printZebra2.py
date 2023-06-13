from zebra import Zebra
from PIL import Image

z = Zebra('Zebra GC420t - ZPL')

# Open the image file
image = Image.open('./logotipo.png')
# Convert RGBA image to RGB
rgb_image = image.convert('RGB')
# Save the image as PCX format
rgb_image.save('./logo.pcx', format='PCX')

graphic_name = 'logo'
#z.store_graphic(graphic_name,'./logo.pcx')

# Specify the path to your text file
file_path = './rotulo zebra/rotulo.txt'
# './etiqueta_diamante/etiqueta.txt'

# Read the contents of the text file
# with open(file_path, 'r') as file:
#     file_contents = file.read()

file_contents  = "^XA"
file_contents += "^LH10,10"
file_contents += "^A0N,30^FT10,40^FDLOTE: 11342071^FS"
file_contents += "^A0N,30^FT300,40^FDOS: 853515 2/4^FS"
file_contents += "^A0N,30^FT550,40^FDFAB: 10^FS"
file_contents += "^A0N,30^FT550,430^FDI1342-318^FS"
file_contents += "^A0N,80^FT680,80^FD34^FS"
file_contents += "^FT50,150^BY2^BCN,75,Y,N"
file_contents += "^FD7891234348173^FS"

#file_contents += "^XGE:1342318.GRF^FT525,350^FS"
#z.print_graphic(graphic_name,1)

file_contents += "^A1N,20^FT10,220^FDCOR 1: MALHA ACTIVE - PRETO^FS"
file_contents += "^A1N,20^FT10,245^FDELASTICO 1: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,270^FDELASTICO 2: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,295^FDFORRO CACHAREL: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,320^FDPALMILHA INTERNA: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,345^FDSOLADO: _ - BRANCO TOFU^FS"
file_contents += "^PQ1"
file_contents += "^XZ"

z.output(file_contents)