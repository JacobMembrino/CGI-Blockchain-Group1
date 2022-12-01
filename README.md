Instructions to setup development environment within cluster:
```
cd ~
mkdir myworkspace
source ./myworkspace/bin/activate
git clone https://github.com/JacobMembrino/CGI-Blockchain-Group1
cd CGI-Blockchain-Group1
pip install -r requirements.txt
```

## Development in local machine

```
git clone https://github.com/JacobMembrino/CGI-Blockchain-Group1
python3 -m venv ./workspace/
source ./workspace/bin/activate
```

Create an infura account from `https://www.infura.io/` and get your api key

## To Access Brownie Console
```
1. Create .env file inside `cgi-abac` directory.
2. In that `.env` file, insert this line `WEB3_INFURA_PROJECT_ID=your_api_key_goes_here`
3. Type `brownie console --network goerli`
4. Once within the brownie console, type `network.is_connected()` to see if you are connected

```

Source code for the brownie project is in `cgi-abac` folder


