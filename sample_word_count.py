from mapreduce import TinyMapReduce

def map_func(txt_filename):
  with open(txt_filename, 'r') as f:
    lines = f.readlines()

  # make word counting for the lines
  wc_dict = {}
  for line in lines:
    words = set(line.rstrip().split(' '))
    for word in words:
      if word not in wc_dict: wc_dict[word] = 0
      wc_dict[word] += 1

  # output to temporary file with key-value format as: "<word> <count>\n"
  tmp_filename = '%s.tmp' % txt_filename
  with open(tmp_filename, 'w') as f:
    for word, cnt in wc_dict.items():
      f.write('%s %s\n' % (word, cnt))

  # return all keys and temporary file's name
  return (wc_dict.keys(), tmp_filename)

def reduce_func((word, tmp_filenames)):
  cnt = 0

  # reduce results for the given word from all tmporary files
  for tmp_filename in tmp_filenames:

    with open(tmp_filename, 'r') as f:
      lines = f.readlines()

    for line in lines:
      key, value = line.rstrip().split(' ')
      if key == word: cnt += int(value)

  # return overall count of the given word
  return (word, cnt)

def main():
  master = TinyMapReduce(map_func, 2, reduce_func, 2)
  txt_filenames = ['texts/1.txt', 'texts/2.txt']
  master(txt_filenames)

if __name__ == '__main__':
  main()
