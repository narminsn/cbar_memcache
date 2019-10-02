# flask_memcached

--- Installation command


First check this bellow command: One line download script copy paste your terminal



#!
$ git clone git@github.com:narminsn/flask_memcached.git


---  Virtual Environment


$ cd flask_memcached/
$ python3 -m venv .venv
$ source .venv/bin/activate


---  Install packages


$ pip install -r requirements.txt

---  Build Docker


$ docker build -t local/memcached:0.1 .

---  Run the Memcached Container


$ docker run -itd --name memcached -p 11211:11211 -e MEMCACHED_MEMUSAGE=32 rbekker87/memcached:alpine


---  Run app


$ python app.py


