python3 worker.py 4000 1 &
python3 worker.py 4001 2 &
python3 worker.py 4002 3 &
python3 master.py config.json 'random' &
#python3 master.py config.json 'round-robin' &
#python3 master.py config.json 'least-loaded' &
