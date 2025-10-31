import numpy
import scipy

k=0.274
L=2.6*scipy.special.ellipeinc(numpy.pi,k)

print(f"Długość elipsy wynosi {L}")
