print('<html>')
print('<head>')
print('<meta http-equiv="Content-Language" content="pt-br">'+'\n')
print('<meta http-equiv="Content-Type" content="text/html; charset= utf-8">'+"\n")
print('<title>Teste com Python</title>')
print('<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css' integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u' crossorigin='anonymous'>')
print('</head>')
print('<body style="background:gray">')
print('<center>')
print('<div style="width:900px; border-radius:2em; background-color:white; border: 3px solid green";>')
print('<img width='400px' alt='IFRS-RESTINGA' src='https://ads.restinga.ifrs.edu.br/wp-content/uploads/2015/03/2013615111655517novo_logo_restinga_curto.png'/>')
print('<div style="width:1000px; border-radius:2em; background-color:white; border: none">')
print('<ul class="dropdown-menu" aria-labelledby="dropdownMenu4">')
print('<li><a href="#">Regular link</a></li>')
print('<li class="disabled"><a href="#">Disabled link</a></li>')
print('<li><a href="#">Another link</a></li>')
print('</ul>')
print('</div>')
print ('<div class="jumbotron">')
print('<div class="panel panel-default">')
print('<div class="panel-heading"><h2>Dados Arduino - Sala 412</h2></div>')
print ('<table class="table">')
     
#import MySQLdb
#from socket import *
#import time
#from datetime import date

#address = ( '169.254.39.10', 5000) #Defind who you are talking to (must match arduino IP and port)
#client_socket = socket(AF_INET, SOCK_DGRAM) #Set Up the Socket
#client_socket.settimeout(1) #only wait 1 second for a resonse

#conexao = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="reservasala")

while(a=="1"): #Main Loop

    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM salas')
    cursor = cursor.fetchall()

    print cursor

   
    
    hoje = datetime.now()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    hora = hoje.hour
    minuto = hoje.minute
    segundo = hoje.second
    print ("<tr>")
    print ("<th>")
    print ("Mensagem")
    print ("</th>")
    print ("<th>")
    print ("Luminosidade")
    print ("</th>")
    print ("<th>")
    print ("Temperatura")
    print ("</th>")
    print ("<th>")
    print ("Luz")
    print ("</th>")
    print ("<th>")
    print ("Ar-condicionado")
    print ("</th>")
    print ("<th>")
    print ("Data/hora")
    print ("</th>")
    print ("</tr>")
    print ("<tr>")

    
 
    data = "Liga" #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        print ("<td>")
        print(   rec_data) #Print the response from Arduino
        print("</td>")
    except:
        pass
 
    time.sleep(1) #delay before sending next command
 
    data = "Lum" #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        print ("<td>")
        print (rec_data) #Print the response from Arduino
        print ("</td>")
    except:
        pass
 
    time.sleep(1) 
    data = "Temp" 
    client_socket.sendto(data, address) 
    try:
        rec_data, addr = client_socket.recvfrom(2048) 
        print ("<td>")
        print (rec_data) 
        print ("</td>")
    except:
        pass
 
    time.sleep(1) 
    
    data = "Desliga" #Atribui a palavra "Desliga" para a variável data
    client_socket.sendto(data, address) #envia o comando "Desliga" para o arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Recebe a resposta do arduino
        print ("<td>")
        print (rec_data) #Mostra a resposta recebida do Arduino
        print ("</td>")
    except:
        pass
    time.sleep(1) #Espera 1 segundo para o próximo comando

    data = "Ar" #Atribui a palavra "Desliga" para a variável data
    client_socket.sendto(data, address) #envia o comando "Desliga" para o arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Recebe a resposta do arduino
        print ("<td>")
        print (rec_data) #Mostra a resposta recebida do Arduino
        print ("</td>")
        
    except:
        pass
    time.sleep(1) #Espera 1 segundo para o próximo comando

    print ("<td>")
    print dia,'/',mes,'/',ano,' ',hora,':',minuto,':',segundo 
    print("</td>")
    print ("</tr>")

    
    time.sleep(10)


print("</table>")
print("</div>")
print("</div>")
print("</div>")
print("</div>")
print("</center>")
print("</body>")
print("</html>")