import faulthandler
faulthandler.enable()

import multiprocessing

pool = multiprocessing.Pool(processes=5)