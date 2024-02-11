import time
import unittest
import ps2
import ps2_test

start = time.time()

suite = unittest.TestLoader().loadTestsFromModule(ps2)
unittest.TextTestRunner(verbosity=2).run(suite)

end = time.time()

time_ps2 = end - start
print("time for ps2:", time_ps2)

start = time.time()

suite = unittest.TestLoader().loadTestsFromModule(ps2_test)
unittest.TextTestRunner(verbosity=2).run(suite)

end = time.time()

time_ps2_test = end - start
print("time for ps2 test:", time_ps2_test)

