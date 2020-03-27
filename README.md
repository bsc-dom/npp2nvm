# NumPy Persistence to Non-Volatile Memory

This library will help you persist numpy array structures into NVM devices.

Internally, it uses [`pynvm`](https://github.com/pmem/pynvm) and buffers --which are
natively supported by `numpy`.

## Installation

`pip install npp2nvm`

## Requirements

 - A NVM device, such as Intel(R) Optane(TM) DC Persistent Memory modules.
 - Python 3.x
 - numpy arrays to be stored.

## Usage

Two environment variables are used for configuring the storage:

 - **NPP2NVM_SIZE** which specifies the size (in MiB) that will be assigned to
 persistence
 - **NPP2NVM_PATH** which specifies the file path that will be used for persistence.
 Note that this file should be located into a _Storage Class Memory_ device, which will
 allow `pynvm` to leverage its characteristics --keep in mind that `pynvm` are bindings of the 
 [PMDK](https://pmem.io/pmdk/) libraries.

## Example

```python
import numpy as np
import npp2nvm

a = np.random.random([256, 256])
a = npp2nvm.np_persist(a)
print(a.shape)
# > (256, 256)
```

## Limitations

Storage and retrieval of data structures (outside the application lifecycle) 
are not implemented in this library (yet?). You can implement your own 
mechanism and/or propose a PR. It will be appreciated!
