import speedtest

teste = speedtest.Speedtest()


# download
print('Testando Download')
velocidade_download = teste.download()
print(f'A velocidade de download é: {velocidade_download / 10**6:.2f} MB/s')

# upload
print('Testando Upload')
velocidade_upload = teste.upload()
print(f'A velocidade de upload é: {velocidade_upload / 10**6:.2f} MB/s')

# ping
ping = teste.results.ping
print(f'O ping é: {ping:.2f} ms')