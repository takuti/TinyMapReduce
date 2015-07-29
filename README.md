## Tiny MapReduce for text processing

A simple MapReduce library for text processing in Python.

Requirements for this library is described [here](https://sites.google.com/site/kudoutokyoislecture/).

### Usage

```python
from tiny_map_reduce import TinyMapReduce

master = TinyMapReduce(map_func, reduce_func)
txt_filenames = ['texts/1.txt', 'texts/2.txt']
master(txt_filenames)
```

Note that MapReduce app spawns N Mapper/reducer processes. (3rd argument of TinyMapReduce() indicates N; default value is None which sets the number of available CPUs to N)

#### Map function (map_func)

- Map function takes a text file, and handles lines one-by-one
- The result will be output to a temporary file
- The function returns the temporary file's name and keys in the file
- **Return** [([keys_in_tmp1], tmp1_name), ([keys_in_tmp2], tmp2_name), ...]

#### Reduce function (reduce_func)

- Reduce function handles each key for all temporary files
- The argument will be one tuple as: (key, [tmp1_name, tmp2_name, ...])
- **Return** [(key1, value1), (key2, value2), ...]

### References

- http://pymotw.com/2/multiprocessing/mapreduce.html
- http://matsulib.hatenablog.jp/entry/2014/06/19/001050