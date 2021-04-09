# A minimal example of a SIGSEGV

To replicate: `python3 multiprocessing-run.py`

Notes:
- this behavior is consistent across `3.6.7`, `3.7.4`, `3.8.1`, and `3.8.6`
- the fault handler does not impact the behavior at all