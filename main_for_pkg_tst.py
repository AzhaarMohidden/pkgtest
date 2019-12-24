from mods import printname as pr
from mods import count as ct
#import mods.printname
#import mods.count
import time
import sys

#printname.Printnames_txt(input1)
start = time.time()
ct.Count(sys.argv[1])
end = time.time()
elapsed = end - start
print("Time elapsed for the above is: " + str(elapsed))
pr.Printnames_txt("\n count ended")
