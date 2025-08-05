import face_recognition
import cv2


imagem1_path = input("Digite o caminho da primeira imagem: ")
imagem1 = face_recognition.load_image_file(imagem1_path)
imagem1_encoding = face_recognition.face_encodings(imagem1)

imagem2_path = input("Digite o caminho da segunda imagem: ")
imagem2 = face_recognition.load_image_file(imagem2_path)
imagem2_encoding = face_recognition.face_encodings(imagem2)

if len(imagem1_encoding) == 0 or len(imagem2_encoding) == 0:
    print("Nao foi encontrado rosto em uma das imagens. Verifique as fotos e tente novamente.")
else:
    resultado = face_recognition.compare_faces([imagem1_encoding[0]], imagem2_encoding[0])

    if resultado[0]:
        print("Resultado: As imagens sao da MESMA PESSOA.")
    else:
        print("Resultado: As imagens sao de PESSOAS DIFERENTES.")
