# Calculate the length of a transmitting or receiving antenna given it's wavelength

# frequency * wavelength = c
# c / wavelength = frequency
# c / frequency = wavelength

c = 300_000_000

def FreqToWavelen(freq):
	return c / freq
def WavelenToFreq(wavelength):
	return c / wavelength
def FormatLen(x):
	if (x < 0.01):
		return str(x*1000) + " millimeters"
	elif (x < 1):
		return str(x*100) + " centimeters"
	elif (x < 1_000):
		return str(x) + " meters"
	else:
		return str(x / 1000) + " kilometers"
def FormatFreq(x):
	if (x < 1000):
		return str(x) + " Hz"
	elif (x < 1_000_000):
		return str(x/1000) + " KHz"
	elif (x < 1_000_000_000):
		return str(x/1_000_000) + " MHz"
	elif (x < 1_000_000_000_000):
		return str(x/1_000_000_000) + " GHz"
	else:
		return str(x/1_000_000_000_000) + " THz"

frequency = int(input("Please enter the desired antenna frequency in MHz: "))*1000000

print("Wave specs:")
print(" - Frequency: " + FormatFreq(frequency))
print(" - Fullwave: " + FormatLen(round(FreqToWavelen(frequency),4)))
print(" - Halfwave: " + FormatLen(round(FreqToWavelen(frequency*2),4)))
print(" - Quarterwave: " + FormatLen(round(FreqToWavelen(frequency*4),4)))
print()
print("Wave Harmonics:")
print(" - First Harmonic: " + FormatFreq(round(frequency*2,4)))
print(" - Second Harmonic: " + FormatFreq(round(frequency*3,4)))
print(" - Third Harmonic: " + FormatFreq(round(frequency*4,4)))
print(" - Fourth Harmonic: " + FormatFreq(round(frequency*5,4)))
print(" - Fifth Harmonic: " + FormatFreq(round(frequency*6,4)))
print()

fullwave = FreqToWavelen(frequency)
print("Antenna Specs: ")
print(" - Desired Fullwave Antenna: " + FormatLen(round(fullwave,4)))
print("   - 1st order Harmonic: " + FormatFreq(round(WavelenToFreq(fullwave),4)))
print("   - 2nd order Harmonic: " + FormatFreq(round(WavelenToFreq(fullwave/2),4)))
print("   - 3rd order Harmonic: " + FormatFreq(round(WavelenToFreq(fullwave/3),4)))
print("   - 4rd order Harmonic: " + FormatFreq(round(WavelenToFreq(fullwave/4),4)))
print("   - 5rd order Harmonic: " + FormatFreq(round(WavelenToFreq(fullwave/5),4)))
print()
print(" - Desired 1/2 wave Dipole Antenna Length: " + FormatLen(round(fullwave/2,4)))
print(" - Desired 1/4 wave Monopole Antenna Length: " + FormatLen(round(fullwave/4,4)))
print("   - 1st order Harmonic: " + FormatFreq(round(WavelenToFreq((fullwave/2)/0.5),4)))
print("   - 3rd order Harmonic: " + FormatFreq(round(WavelenToFreq((fullwave/2)/1.5),4)))
print("   - 5th order Harmonic: " + FormatFreq(round(WavelenToFreq((fullwave/2)/3.5),4)))
print("   - 7th order Harmonic: " + FormatFreq(round(WavelenToFreq((fullwave/2)/4.5),4)))

