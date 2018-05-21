# snakefile
configfile: "config.yaml"

samples = config["samples"]

# import rules
include: "rules/folders.rule"
include: "rules/qc.rule"

# import rules
rule all:
    input: 
        rules.qc.input
        rules.taxonomy.input