from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.brightness = 37

# Camera warm-up time - Отображение входных данных камеры в ральном времени
camera.start_preview()

#camera.resolution = (1280, 720) #- задание разрешения снимка
camera.contrast = 33
brightness = str(camera.brightness)
resolution = str(camera.resolution)
contrast = str(camera.contrast)
print('Яркость камеры: ' + brightness + '%')
print('Разрешение снимков камеры: ' + resolution + 'пикселей')
print('Контрастность снимков камеры: ' + contrast + ' единиц')

sleep(5)
camera.capture('MVVK_white_37.jpg')  # Take a picture - и сохранение фото

camera.stop_preview() #- остановка предварительного просмотра


camera.close() #-   метод для освобождения ресурсов камеры