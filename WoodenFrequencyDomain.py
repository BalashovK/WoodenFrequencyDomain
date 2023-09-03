import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Let's look at Frequency domain. We need to create something in spatial domain and apply Fourier transform
# What shall we create? Let's create a Gaussian. Gaussian is known to be able to travel between domains. It might got slimmer or fatter, but it still be Gaussian.
# Let's create one
range = range(-1024,1024)
x, y = np.meshgrid(range, range)
r = np.sqrt(x*x+y*y)
sigma_s = 3.65 # We need some sigma value. Let's use 1% of a year measured in days
gaussian_spatial = np.exp(-( (r)**2 / ( 2.0 * sigma_s**2 ) ) )

# Now let's convert it to Frequency domain with FFT
fft2d_result = np.fft.fft2(gaussian_spatial)

# It is complex. Let's simplify things and just look at magnitude
magnitude = np.abs(fft2d_result)

# Value range is too large. Let's look at logarithm instead
logged_magnitude = np.log(-magnitude + 1e-9) # add epsilon 1e-9 because logarithm likes to stay positive

# Now let's look around 
center_x, center_y = magnitude.shape[0] // 2, magnitude.shape[1] // 2
cropped_magnitude = logged_magnitude[center_x-480:center_x+480, center_y-480:center_y-50]

# We want to visualize it. Let's prepare a pleasant color map
colors = [(0.75, 0.45, 0.225), (0.17, 0.09, 0.05)]  
cmap_name = 'custom_brown'
brown_cmap = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=100)

# Ok, time to visualze it
plt.imshow(cropped_magnitude, cmap=brown_cmap)
plt.show()

# As you can see, Frequency domain is made out of wood. 
# That's because Josef Fourier live 200 years ago
# Back then they made everything out of wood.
# Maybe, it is time to upgrade?
