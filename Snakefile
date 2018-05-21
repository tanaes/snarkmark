# snakefile
configfile: "config.yaml"

samples = config["samples"]

# import rules
include: "rules/folders.rule"
include: "rules/qc.rule"
include: "rules/taxonomy.rule"
include: "rules/function.rule"
include: "rules/assemble.rule"
include: "rules/report.rule"

# import rules
rule processing:
    input:
        rules.qc.input,
        rules.taxonomy.input,
        rules.function.input,
        rules.assemble.input

rule report:
    input:
        rules.report_benchmark_summary.output

rule all:
    input:
        rules.processing.input,
        rules.report.input
