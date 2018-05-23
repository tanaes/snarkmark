#!/usr/bin/env python
import os
import re
import yaml
import shutil
from collections import OrderedDict

indir = '/projects/emp500/public/shotgun/raw/180404_A00169_0085_AH7CV2DMXX'
outdir = 'samples'
outfile = 'samples.yaml'

file = 'emp500_samples.txt'

sample_dict =  OrderedDict()

os.makedirs(outdir)

with open(file) as f:
    for line in f:
        subdir, r1_l1 = os.path.split(line.strip())
        # Rohwer85_deep_sediment_AP18_S5_L001_R1_001.fastq.gz
        match = re.match(r'(.*)_(S\d+)_L00\d_R\d_001.fastq.gz', r1_l1)
        sample = match.group(1)
        S = match.group(2)

        r2_l1 = '%s_%s_L001_R2_001.fastq.gz' % (sample, S)

        r1_out = os.path.join(outdir, r1_l1)
        r2_out = os.path.join(outdir, r2_l1)

        sample_dict[sample] = {'forward': r1_out,
                               'reverse': r2_out}

        shutil.copy(os.path.join(indir, subdir, r1_l1), outdir)
        shutil.copy(os.path.join(indir, subdir, r2_l1), outdir)


with open(outfile, 'w') as out:
    yaml.dump(sample_dict, out, default_flow_style=False)