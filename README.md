# Reconhecimento facial utilizando Python e OpenCV

- Esta aplicação consiste em utilizar o Processamento Digital de Imagens (**PDI**) para reconhecer um rosto e aplicar um emoji sobre a face.

- Para a criação dessa aplicação foi necessário a utilização da linguagem de programação **Python**, a biblioteca **OpenCV** e um arquivo **Haarcascade** com as instruções de uma face humana.

- O arquivo **Haarcascade** é um arquivo em formato **XML** com as coordenadas de um objeto a ser examinado. Com técnicas de **machine learning** é possível criar arquivos **harrcascades** para reconhecimento de qualquer objeto. No caso dessa aplicação o arquivo **XML** está funcionando para localizar faces humanas.

- Foi realizado o download de vários emojis na internet e colocados dentro da pastra emoji. Todas essas imagens estão renomeadas com números e no formato **PNG**.

- Através da biblioteca **OpenCV** foi possível capturar a imagem da WebCam do computador e realizar o reconhecimento facial. Dependendo da distância da pessoa as faces podem assumir tamanhos diferentes das do emoji, por isso foi necessário redimencionar o tamanho dos emojis. 

- Divido a todas as imagens estarem no formato PNG cada pixels obtem a variável *alpha* referente a quantidade de transparência, e para deixar a imagem do emoji transparente foi necessário percorrer toda a matriz bidimencional e aplicar o valor respectivo do píxel da WebCam.

- O método *cv2.rectangle* permitiu capturar apenas a imagem facial obtida através do arquivo **haarcascade**.

- O método *img_capturada.shape[0]* retornou a altura da imagem e o método img_capturada.shape[1] retornou a largura.

- Após isso a função *transparentOverlay* sobreescreveu a imagem da WebCam com a do emoji.

- Para que os emojis fossem alterados foi criado a seguinte condição: Se o número de faces fosse alterada é sorteado um novo emoji. Por isso que eles foram renomeados com números, que foi para facilitar o sorteio. 

- Todo o código foi comentado.

# Resultado: 
 
![Image of system](https://raw.githubusercontent.com/Otavio15/reconhecimento_facial_emojis_py/new/PDI.png)

