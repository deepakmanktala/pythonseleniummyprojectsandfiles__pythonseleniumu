from PIL import ImageGrab
from datetime import datetime

while True:
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "Funadamentals_of_BIG_DATA_and_analytics_slides{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 2000000)
    im.save(fname, 'png')