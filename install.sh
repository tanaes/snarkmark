# create core conda env
conda env create --name snarkmark -f environment.yml

# unzip test dbs
cd test_data/test_dbs
bash install_test_dbs.sh
