import socket
import MySQLdb             

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '192.168.0.107' 
port = 12002         

server_socket.bind((host, port))        
server_socket.listen(5)
client, addr = server_socket.accept()

while True:	     
	uid_tag = client.recv(1024).decode("utf-8")
	enc_tag = "".join("{:02x}".format(ord(c)) for c in uid_tag)

	db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '1192001',db = 'project')
	str = 'select name, gender, designation, city from rfid where id = ' + enc_tag
	cur = db.cursor()
	cond = cur.execute(str)

	if cond!=0:
		print("Database identified")
		for row in cur.fetchall():
			print(row)
	
	else:
		print("Not A Genuine Person")
	
	db.close()

c.close() 




               
