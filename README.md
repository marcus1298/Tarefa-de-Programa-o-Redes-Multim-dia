# Relatório do roteiro: 
Realizar procedimento indicado no arquivo a seguir e enumerar os testes de
funcionamento realizados e os resultados obtidos. Inserir capturas de telas e/ou
comentários que considerar pertinente.
Além disso, link com as instruções da atividade em python:
https://gaia.cs.umass.edu/kurose_ross/programming/Python_code_only/VideoStream
ing_programming_lab_only.pdf

Link: https://docs.google.com/document/d/1ha8w8kitTISUG3h0c7RSUKXn7fC7hW5-9CjU9r3adzY/edit?usp=sharing

Tarefa de Programação referente ao Capítulo de Redes Multimídia. Neste laboratório,
o aluno implementará um servidor de streaming vídeo e um cliente que se comunicam
usando o protocolo de fluxo contínuo em tempo real (RTSP) e envia dados usando o
protocolo de tempo real (RTP). O objetivo é implementar o protocolo RTSP no cliente e
implementar o empacotamento RTP no servidor.
# Abaixo a implementação de um servidor de streaming em python:
# Streaming de Vídeo com RTSP e RTP
Este projeto consiste na implementação de um cliente e um servidor para streaming de vídeo utilizando os protocolos RTSP (Real-Time Streaming Protocol) e RTP (Real-time Transport Protocol).

# Funcionalidades Implementadas:
# Cliente (client.py):
Estabelecimento de conexão RTSP com o servidor.
Envio de solicitações RTSP, incluindo SETUP, PLAY, PAUSE e TEARDOWN.
Recebimento de respostas do servidor.
Gerenciamento de estado do cliente de acordo com as respostas do servidor.
# Servidor (server.py):
Aceita conexões RTSP de clientes.
Tratamento de solicitações RTSP recebidas dos clientes.
Resposta a solicitações RTSP, incluindo SETUP, PLAY, PAUSE e TEARDOWN.
Implementação básica da transmissão de vídeo usando RTP (a ser expandida).
Como Usar:
# Cliente:
Execute o script client.py.
Crie uma instância do RTSPClient passando os seguintes parâmetros:
server_host: O endereço IP ou nome do host do servidor.
server_port: A porta onde o servidor RTSP está escutando.
rtp_port: A porta para receber os pacotes RTP.
video_file: O nome do arquivo de vídeo a ser solicitado ao servidor.
Chame os métodos setup(), play(), pause() e teardown() conforme necessário para interagir com o servidor.

# Exemplo de uso:


client = RTSPClient('localhost', 554, 1234, 'movie.Mjpeg')
client.setup()
client.play()
client.pause()
client.teardown()
Servidor:
Execute o script server.py.
Crie uma instância do RTSPServer passando os seguintes parâmetros:
server_port: A porta onde o servidor RTSP deve escutar.
video_file: O nome do arquivo de vídeo a ser transmitido aos clientes.
O servidor estará pronto para aceitar conexões RTSP de clientes e responder às solicitações.
Exemplo de uso:

server = RTSPServer(554, 'movie.Mjpeg')
server.start()

# Observações:
Este projeto é uma implementação simplificada e pode ser expandido com recursos adicionais, como tratamento de erros mais robusto, suporte a múltiplos clientes simultâneos, melhorias na transmissão de vídeo RTP, entre outros.
Certifique-se de ajustar o código conforme necessário para atender aos requisitos específicos da sua aplicação.
