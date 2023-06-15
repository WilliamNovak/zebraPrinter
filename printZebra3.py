from zebra import Zebra
from PIL import Image
from zplgrf import GRF

z = Zebra('Zebra GC420t - ZPL')

with open('1342318.BMP', 'rb') as image:
    grf = GRF.from_image(image.read(), 'TESTE')

grf.optimise_barcodes()
grfCommands = grf.to_zpl(compression=3, quantity=1)

indice = grfCommands.find('^XA')  # Encontra a posição da primeira ocorrência da sequência (ignorando maiúsculas e minúsculas)
grfImage = grfCommands[:indice]  # Extrai a substring do início até a posição da sequência

file_contents  = grfImage
file_contents += "^XA"
file_contents += "^LH10,10"
file_contents += "^A0N,30^FT10,40^FDLOTE: 11342071^FS"
file_contents += "^A0N,30^FT300,40^FDOS: 853515 2/4^FS"
file_contents += "^A0N,30^FT550,40^FDFAB: 10^FS"
file_contents += "^A0N,30^FT550,430^FDI1342-318^FS"
file_contents += "^A0N,80^FT680,80^FD34^FS"
file_contents += "^FT50,150^BY2^BCN,75,Y,N"
file_contents += "^FD7891234348173^FS"

file_contents += "^XGE:TESTE.GRF^FT525,350^FS"
# file_contents += commands

file_contents += "^A1N,20^FT10,220^FDCOR 1: MALHA ACTIVE - PRETO^FS"
file_contents += "^A1N,20^FT10,245^FDELASTICO 1: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,270^FDELASTICO 2: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,295^FDFORRO CACHAREL: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,320^FDPALMILHA INTERNA: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,345^FDSOLADO: _ - BRANCO TOFU^FS"
file_contents += "^PQ1"
file_contents += "^XZ"

# print(file_contents)

listaArquivos = "^XA^WDR:*.*^XZ"

z.output(file_contents)