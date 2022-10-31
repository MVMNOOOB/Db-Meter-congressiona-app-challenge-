from scipy.io.wavfile import read
#samprate, wavdata = read('ALMOST PANDORAS BOX FINAL.wav')
#filename = input("Please enter the name of the audio file you wish to analyze -must usename as it is shown in folder with .wav at the end\n")

samprate, wavdata = read("intro.wav")
import numpy as np
import math
import statistics
# basically taking a reading every half a second - the size of the data 
# divided by the sample rate gives us 1 second chunks so I chop 
# sample rate in half for half second chunks
chunks = np.array_split(wavdata, wavdata.size/(samprate/2))
for chunk in chunks:
    print(chunk)
    print(chunk.size)
dbs = [20*math.log10( math.sqrt(statistics.mean(chunk**2)) ) for chunk in chunks]
print(dbs)
print("Input wav size is: %d" % wavdata.size)
print("Average dB value is: %.2f" % statistics.mean(dbs))

if (statistics.mean(dbs) >= 30):

    print("Your song is too loud!  Consider passing it into a limiter and try again.")

elif (statistics.mean(dbs)  <= 15):

    print("Your song is too quiet!  Consider passing it into a limiter, boosting the gain, and try again")

else:

    print("Your song is ready to release!")