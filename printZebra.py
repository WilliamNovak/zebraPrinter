from zebra import Zebra
from zplgrf import GRF
from PIL import Image

z = Zebra('Zebra GC420t - ZPL') # Seleciona a impressora

image = Image.open('1342318.BMP') # Open the image file
    
original_width, original_height = image.size # Get the original width and height
        
aspect_ratio = original_width / original_height # Calculate the aspect ratio

calculated_height = int(256 / aspect_ratio) # Calculate the new height based on the aspect ratio and the new width

resized_image = image.resize((256, calculated_height)) # Resize the image using the new width and calculated height

pcxImage = resized_image.convert('1') # Convert image to B&W format
pcxImage.save('1342318.jpg') # Save the resized image

with open('1342318.jpg', 'rb') as image: # Abre o arquivo da image com permissao de leitura no formato de bytes
    grf = GRF.from_image(image.read(), 'TESTE') # Cria um objeto GRF da imagem com o nome TESTE

grf.optimise_barcodes()
grfCommands = grf.to_zpl(compression=3, quantity=1) # Gera o codigo ZPL da imagem em GRF

indice = grfCommands.find('^XA')  # Encontra a posição da primeira ocorrência da sequência de caracteres
grfImage = grfCommands[:indice]  # Extrai a substring do início até a posição da sequência

qrCode = "^FO570,170^BQR,2,5,H,7^FDQA,www.google.com'^FS"

# Comandos ZPL para imprimir a etiqueta
file_contents  = grfImage # ZPL para gravar a imagem na memoria de impressora
file_contents += "^XA"
file_contents += "^LH10,10"
file_contents += "^A0N,30^FT10,40^FDLOTE: 11342071^FS"
file_contents += "^A0N,30^FT300,40^FDOS: 853515 2/4^FS"
file_contents += "^A0N,30^FT550,40^FDFAB: 10^FS"
file_contents += "^A0N,30^FT550,430^FDI1342-318^FS"
file_contents += "^A0N,80^FT680,80^FD34^FS"
file_contents += "^FT50,150^BY2^BCN,75,Y,N"
file_contents += "^FD7891234348173^FS"
file_contents += "^XGR:TESTE.GRF^FT525,350^FS" # ZPL para imprimir a imagem
# file_contents += qrCode
file_contents += "^A1N,20^FT10,220^FDCOR 1: MALHA ACTIVE - PRETO^FS"
file_contents += "^A1N,20^FT10,245^FDELASTICO 1: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,270^FDELASTICO 2: _ - PRETO^FS"
file_contents += "^A1N,20^FT10,295^FDFORRO CACHAREL: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,320^FDPALMILHA INTERNA: FORRO CACHAREL - PRETO^FS"
file_contents += "^A1N,20^FT10,345^FDSOLADO: _ - BRANCO TOFU^FS"
file_contents += "^PQ1"
file_contents += "^XZ"

# print(grf)
# listaArquivos = "^XA^WDR:*.*^XZ"

z.output(file_contents) # Imprime a etiqueta com a imagem