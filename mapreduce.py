import multiprocessing

class TinyMapReduce:

  def __init__(self, map_func, N, reduce_func, M):

    self.map_func = map_func
    self.reduce_func = reduce_func

    # MapReduce app spawns N Mapper processes and M Reducer processes
    self.map_workers = multiprocessing.Pool(N)
    self.reduce_workers = multiprocessing.Pool(M)

  def __call__(self, txt_filenames):
    """Specifications of TinyMapReduce
    src_url => https://sites.google.com/site/kudoutokyoislecture/

    Input: text files. pass each line to Map function.
    Output: text files. each line will be "<key> <value>\n".
            (assume no space in key, no '\n' in value.)
    - Each Mapper process reads n input files (no overlap),
      runs Map function and outputs temporary files for Reducers.
    - Each Reducer process reads temporary files,
      runs Reduce function, and writes 1 output file (no key overlap)
    """

    # Map function takes a text file, and handles lines one-by-one
    # The result will be output to a temporary file
    # Each mapper returns the temporary file's name and keys in the file
    # responses: [([keys_in_tmp1], tmp1_name), ([keys_in_tmp2], tmp2_name), ...]
    responses = self.map_workers.map(self.map_func, txt_filenames)

    # get all temporary files' name and existing keys
    tmp_filenames = []
    all_keys = []
    for keys, tmp_filename in responses:
      all_keys += keys
      tmp_filenames.append(tmp_filename)
    all_keys = list(set(all_keys))

    # Reduce function handles each key for all temporary files
    # arg for reduce_func: (key, [tmp1_name, tmp2_name, ...]) (= one tuple)
    results = self.reduce_workers.map(self.reduce_func, zip(all_keys, [tmp_filenames] * len(all_keys)))

    # reduced results will have tuples of (key, value)
    # these tuples are output to one file `results.txt` with key-value format
    with open('results.txt', 'w') as f:
      for k, v in results:
        f.write('%s %s\n' % (k, v))
