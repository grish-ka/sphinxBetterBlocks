# sphinxBetterBlocks

a simple sphinx extension for making attaching github block for github repos!

# Install
for now just download the [`betterBlocks.py`](betterBlocks.py)
and put it in a folder like **directives**,
in your `conf.py`
add the `betterBlocks.py` file to your extensions,
at the start of your file add this:
```python
import sys
import os

sys.path.insert(0, os.path.abspath('.'))
```

that should be all