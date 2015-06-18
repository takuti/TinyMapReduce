import multiprocessing

class TinyMapReduce:

  def __init__(self, map_func, N, reduce_func, M):

    self.map_func = map_func
    self.reduce_func = reduce_func

    # MapReduce app spawns N Mapper processes and M Reducer processes
    self.map_workers = multiprocessing.Pool(N)
    self.reduce_workers = multiprocessing.Pool(M)
