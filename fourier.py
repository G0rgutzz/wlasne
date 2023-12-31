import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()
'''
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active


wb.save('fourier.xlsx')

exit()
'''
