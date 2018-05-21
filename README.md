# snarkmark
a snakemake workflow for benchmarking HTC systems for bioinformatics

## installation
to install the basic environment and minimal test databases, clone this 
repository and run `install.sh`:

```bash

bash install.sh
```

## execution
Snarkmark uses the built-in conda environment functionality to install and
run software, and will automatically create new conda environments when they
are needed (first time they're run, and anytime the checksum of the listed
environment file in `envs/env_*.yaml` changes).

To execute a complete workflow on the minimal test data, just run:

```bash

snakemake --cores 16 --use-conda --configfile config_test.yaml all
```

where `--cores N` species the number of cores to make available to the
benchmark workflow.

This will run all available jobs steps, producing the following output folders:

- `results`: the data outputs and log files
- `benchmarks`: json-formatted benchmarks for each job step
- `reports`: a directory with html-formatted report summarizing
             the benchmark data per job and per input file

## running with different data

To run with alternative input data, you will need to modify
`config_example.yaml` appropriately. This involves updating the temp folder
directory:

```yaml
tmp_dir_root: /panfs/panfs1.ucsd.edu/panscratch/jgsanders
```

the db_dir, where *all* databases used are stored:

```yaml
  db_dir: ~/git_sw/snarkmark/test_data/test_dbs
```

and the `samples` dictionary, which should point to one `forward` and one
`reverse` gzipped-fastq per sample:

```yaml
samples:
  sample_S22205:
    forward: test_data/test_reads/S22205_S104_L001_R1_001.fastq.gz
    reverse: test_data/test_reads/S22205_S104_L001_R2_001.fastq.gz
```