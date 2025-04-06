# exp73-wsl-docker-pipeline
Learning and documenting the process of creating a code using WSL (Windows Subsystem for Linux) and also using docker. The docker will be created to easily run all the enviroment without the need of installing all the dependences. Those, will be already inside the docker. At last, the pipeline will be added to project in order of running static tests, unity tests and so on.

## WSL

To install WSL, run on CMD ```wsl --install```. After installed, its necessary to reboot windows. When entering the WSL, it will ask you to create a default Unix user. To do that, type your user name and password (twice).

## Docker 
Step 1 - Update the system: 
```
sudo apt update
sudo apt upgrade -y
```

Step 2 - Install dependencies:
```
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

Step 3 - Add Docker’s official GPG key:
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
Step 4 - Set up Docker repo:
```
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```
Step 5 - Install Docker Engine:
```
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Step 6 - Test Docker installation: 
```
docker --version
```
In my case, it returned: Docker version 28.0.4, build b8034c0

Step 7 - Run Docker without sudo:
```
sudo usermod -aG docker $USER
```

## Git - versionning control

Step 1 - Generate RSA SSH Key
```
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```
Press Enter to save key on default location (~/.ssh/id_rsa).
Type passphrase or empty for no passphrase.

Step 2 - Copy the public key to GitHub:
```
cat ~/.ssh/id_rsa.pub
```
Then add key to GitHub [keys](https://github.com/settings/keys).

Step 3 - Connect with GitHub:
```
ssh -T git@github.com
yes
```
Step 4 - Creating git folder (only required once):
```
mkdir git
cd git
```
Step 5 - Cloning the Repo:


## CI CD Pipeline

### Jenkins

