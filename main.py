#Random Subraction Drills Generator:

#Generate a random subtraction equation in the format of the following example:

#5487 - 843

#Where the following rules apply.

#5487 will be known as the subtractee
#843 will be known as the subtractor

#1. The subtractee is in the thousands, and the subtractor is in the hundreds
#2. The hundredth of the subtractee must be less than the hundredth of the subtractor

import random

thousandth = random.randrange(1, 10) * 1000
high_hundredth = random.randrange(2, 10)
high_hundred = high_hundredth * 100
low_hundred = random.randrange(1, high_hundredth) * 100
complete_low_hundred = random.randrange(low_hundred, low_hundred + 100)
subtractee = thousandth + complete_low_hundred
subtractor = random.randrange(high_hundred, 1000)

print('Algorithm A', subtractee, '-', subtractor)

subtractor = random.randrange(200, 1000)
low_hundred = random.randrange(subtractor)
subtractee = random.randrange(1,10) * 1000 + low_hundred

print('Algorithm B', subtractee, '-', subtractor)










