"""Main module and implicit initialization.

This module expects the following environment variables defined:

  - NPP2NVM_PATH Path to the file that will be used. Typically, this file will
    be in a place where a SCM is mounted and thus has the DAX flag and so on.
    The pynvm Python library will be able to leverage the PMDK features.

  - NPP2NVM_SIZE The size (in MB) of the persistent space.
"""
import os
from nvm import pmem
import numpy as np

# Aligning data to 4k because I don't know any better
ALIGNMENT = 4096

BYTE_SIZE = 1024 * 1024 * int(os.environ["NPP2NVM_SIZE"])


blocks_written = 0
reg = None
initialized = False


def initialize():
    global reg
    global initialized
    reg = pmem.map_file(os.environ["NPP2NVM_PATH"], BYTE_SIZE, pmem.FILE_CREATE, 0o666)
    initialized = True


def np_persist(np_array):
    """Persist a given numpy array.

    This will persist the object into the NVM and return a handler to the
    persisted array, which will be similar (a new reference, but same values
    and shape) to the original one.

    Typically, `np_persist` will be called like this:

      a = np_persist(a)
    """

    # The following is extremely ugly and anti-pythonic.
    # I know.
    # Consider yourself invited to propose a PR to improve all this mess :)
    global blocks_written
    global initialized
    global reg
    
    if not initialized:
      initialize()

    b = np_array.tobytes()

    last_offset = blocks_written * ALIGNMENT
    print("Persisting a numpy array at offset: %d" % last_offset)

    # Rationale for the following formula: 
    # sizes of both 1 byte and ALIGNMENT bytes should increment the blocks by 1
    # a size of ALIGNMENT+1 bytes should increment the blocks by 2
    blocks_written += (len(b) - 1) // ALIGNMENT + 1
    reg.write(b)
    reg.seek(blocks_written * ALIGNMENT)

    # Get all the raw data in the buffer into a numpy array
    ret = np.frombuffer(reg.buffer, dtype=np_array.dtype, count=np_array.size, offset=last_offset)
    # Reshape it properly
    return ret.reshape(np_array.shape)
