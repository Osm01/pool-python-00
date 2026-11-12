from datetime import datetime
import time


n = time.time()


print(f"Seconds since January 1, 1970:{n: ,.4f} or{n: .2e} ", end="")
print("in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
