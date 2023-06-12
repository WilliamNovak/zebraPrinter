c:
cd \sft\MOVTO\ETIQUETA\
copy del_image.txt /y LPT1
"C:\Program Files (x86)\IrfanView\i_view32.exe" C:\SFT\MOVTO\ETIQUETA\1342318.bmp /bpp=1 /resize=(256,256) /resample /aspectratio /silent /convert=C:\SFT\MOVTO\ETIQUETA\1342318.bmp
java -jar C:\SFT\MOVTO\ETIQUETA\ZSDK_API.jar graphic C:\SFT\MOVTO\ETIQUETA\1342318.bmp -y 256 -x 256 -n 1342318.grf -s C:\SFT\MOVTO\ETIQUETA\1342318.prn
sleep.exe 1 /quiet
copy C:\SFT\MOVTO\ETIQUETA\1342318.prn /y LPT1
sleep.exe 1 /quiet
copy C:\SFT\MOVTO\ETIQUETA\etiqueta.txt /y LPT1
