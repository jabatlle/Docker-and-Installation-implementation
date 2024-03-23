# Docker-and-Installation-implementation
In this project I created a function that its input are two matrices and its output is the multiplication of this two matrices. After creating this function using numpy, I made some test examples and tested it with pytest. I tested correct outputs, wrong imputs, error conditions, among other things. I also used linting, flake8 specifically because it offers an easy way to ensure quality by checking syntax issues, stylistic errors, etc. Then I explore github actions.

To install it:
#### Clone Repo

git clone https://github.com/jabatlle/Docker-and-Installation-implementation.git
cd Docker-and-Installation-implementation

#### Install Requirements

pip install -r requirements.txt

#### Run Scripts

python3 MatrixMult.py

#### Docker

##### Build Image

docker build -t MatrixMult .

##### Run Container

docker run MatrixMult


##### Export Image

docker save -o MatrixMult.tar MatrixMult

##### Import Image 

docker load -i MatrixMult.tar


