# tcpping
Utility for ping via TCP
## Install
git clone 
pip install -r requirements.txt
## Usage
python main.py  [-h] [--host HOST] [--port PORT] [--max MAX]

>python main.py -H 192.168.0.1
>Connected to 192.168.0.1[80]: tcp_seq=0 time=2.18 ms 
>Connected to 192.168.0.1[80]: tcp_seq=1 time=1.50 ms
>Connected to 192.168.0.1[80]: tcp_seq=2 time=11.54 ms

Ping Results: Connections (Total/Pass/Fail): [3/3/0] (Failed: 0%)