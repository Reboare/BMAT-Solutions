import numpy
from matplotlib import pyplot as plt
from matplotlib2tikz import save as tikz_save

x = numpy.arange(0, 4, 0.01)

y = 100*2**(-x)
print numpy.interp(1, x, y)


fig, ax = plt.subplots()

#fig.patch.set_visible(False)
#ax.axis('off')

plt.plot(x, y, color="r")
plt.plot([1, 1], [50,0], color="b")
plt.plot([2, 2], [25,0], color="b")
plt.plot([3, 3], [12.5,0], color="b")

#ax.spines['left'].set_position('zero')
#ax.spines['bottom'].set_position('zero')

#plt.annotate(s='', xy=(numpy.pi/2.0,1), xytext=(numpy.pi/2.0,0), arrowprops=dict(arrowstyle='<->'))

#plt.annotate(s='', xy=(0,0), xytext=(2*numpy.pi,0), arrowprops=dict(arrowstyle='<->'))
#ax.text(4.5, 0.1, "Wavelength",)
#ax.text(1.6, 0.4, "Amplitude")

plt.xlabel("Time (s)")
plt.ylabel("Activity")
#plt.show()
tikz_save("exp.tex")