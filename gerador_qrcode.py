import qrcode

informacao_qrcode = input("Insira o texto ou link para criar o QR Code: ")

imagem = qrcode.make(informacao_qrcode)
imagem.save("qrcode_generated.png")
imagem.show()
print("O QR Code foi criado e guardado!")