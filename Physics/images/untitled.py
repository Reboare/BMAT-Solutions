import numpy
from matplotlib import pyplot as plt
from matplotlib2tikz import save as tikz_save

x = numpy.linspace(0,2*numpy.pi,100)
y = numpy.sin(x)


fig, ax = plt.subplots()

fig.patch.set_visible(False)
ax.axis('off')

plt.plot(x, y, color="r", label=r"$3x-2$")

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.annotate(s='', xy=(numpy.pi/2.0,1), xytext=(numpy.pi/2.0,0), arrowprops=dict(arrowstyle='<->'))

plt.annotate(s='', xy=(0,0), xytext=(2*numpy.pi,0), arrowprops=dict(arrowstyle='<->'))
ax.text(4.5, 0.1, "Wavelength",)
ax.text(1.6, 0.4, "Amplitude")
plt.xlim(0, 2*numpy.pi)
plt.ylim(-1.5, 1.5)
#plt.show()
tikz_save("lambda.tex")