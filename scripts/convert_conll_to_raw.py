"""
Embarassingly simple (should I have written it in bash?) script
for turning conll-formatted files to sentence-per-line
whitespace-tokenized files.

Takes the filepath at sys.argv[1]; writes to stdout
"""

import sys
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('input_conll_filepath')
args = argp.parse_args()

buf = []

# TODO is it better to tokenize using bert's tokenizer, or use the tokenized versions?
# Check the paper!

for line in open(args.input_conll_filepath):
  if line.startswith('#'):
    continue
  if not line.strip():
    sys.stdout.write(' '.join(buf) + '\n')
    buf = []
  else:
    buf.append(line.split('\t')[1])
if buf:
    sys.stdout.write(' '.join(buf) + '\n')
