# Docker-and-Installation-implementation
This is a simple project I created. It has a function that its input are two matrices and its output is the multiplication of this two matrices. After creating this function using numpy, I made a test example and tested it with pytest. I also used linting, flake8 specifically because it offers an easy way to ensure quality by checking syntax issues, stylistic errors, etc. Then I proceeded to implement Docker and created an image.

To install it:
#### Clone Repo

git clone https://github.com/jabatlle/Docker-and-Installation-implementation.git
cd Docker-and-Installation-implementation

pip install -r requirements.txt

Build Image

docker build -t mymatrixmult .

Run Container

docker run mymatrixmult

docker save -o mymatrixmult.tar mymatrixmult

docker load -i mymatrixmult.tar

<img width="1262" alt="Screenshot 2024-03-23 at 7 28 17 PM" src="https://github.com/jabatlle/Docker-and-Installation-implementation/assets/114434629/5b68ab27-6a0c-4792-a530-6f356817adf6">

