# create core conda env
conda env create --name snarkmark -f environment.yml

# unzip test dbs
bash test_data/test_dbs/install_test_dbs.sh
