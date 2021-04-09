import _multiprocessing
import sys
class ReplacementSemLock(_multiprocessing.SemLock):
    def acquire(self, blocking: bool = True, timeout: float = None):
        if blocking:
            if timeout is None:
                timeout = sys.getswitchinterval()
            else:
                timeout = min(timeout, sys.getswitchinterval())
        else:
            timeout = None
        
        while True:
            acquired = super().acquire(blocking, timeout)
            if acquired:
                return True
            if not blocking:
                return False


_multiprocessing.SemLock = ReplacementSemLock
with open('multiprocessing_test.py', 'rb') as f:
    code = compile(f.read(), 'multiprocessing_test.py', "exec")
exec(code)
