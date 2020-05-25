# tcpping
Utility for ping via TCP
## Install
git clone 
pip install -r requirements.txt
## Usage
python3 main.py host [port] [maxCount]

python main.py host [port] [maxCount]

python main.py 192.168.0.1
Connected to 192.168.0.1[80]: tcp_seq=0 time=12.75 ms
Connected to 192.168.0.1[80]: tcp_seq=1 time=19.48 ms
Connected to 192.168.0.1[80]: tcp_seq=2 time=19.65 ms

Ping Results: Connections (Total/Pass/Fail): [3/3/0] (Failed: 0%)
