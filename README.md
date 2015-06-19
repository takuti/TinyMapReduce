## Tiny MapReduce for text processing

A simple MapReduce library for text processing in Python.

Requirements for this library is described [here](https://sites.google.com/site/kudoutokyoislecture/).

### Usage

```python
from tiny_map_reduce import TinyMapReduce

master = TinyMapReduce(map_func, 2, reduce_func, 2)
txt_filenames = ['texts/1.txt', 'texts/2.txt']
master(txt_filenames)
```

Note that MapReduce app spawns N Mapper processes and M Reducer processes. (both of N and M are 2 in the above example)

#### Map function (map_func)

- Map function takes a text file, and handles lines one-by-one
- The result will be output to a temporary file
- The function returns the temporary file's name and keys in the file
- :return [([keys_in_tmp1], tmp1_name), ([keys_in_tmp2], tmp2_name), ...]:

#### Reduce function (reduce_func)

- Reduce function handles each key for all temporary files
- The argument will be one tuple as: (key, [tmp1_name, tmp2_name, ...])
- :return [(key1, value1), (key2, value2), ...]: