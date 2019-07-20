# Transcoor
Transcoor é um programa desenvolvido em python 3 para cálculo de caderneta de campo. Aqui é utilizado o formato proveniente do software topograph, o .M21, o Transcoor consegue calcular poligonais abertas com utilização de pontarias diretas e cria arquivo .dxf com os pontos, separando cada feição em uma camada diferente.

Utilizo a estação total Topcon 236w.

Funcionamento:

Abrir o programa:
![transcoor 01](https://user-images.githubusercontent.com/995209/61579167-0f6d7400-aad8-11e9-8afb-6d721e274ca6.png)

Abrir o arquivo M21:
![transcoor 02](https://user-images.githubusercontent.com/995209/61579166-0ed4dd80-aad8-11e9-9bdb-7ae621362b60.png)

Calcular a caderneta de campo usando "2 pontos" que procura as estações e os pontos de ré, calculando o azimute por elas. Ou calcular por hz, aqui ele vai calculando os azimutes por partes, Az = Az0 + Hz - 180.
![transcoor 03](https://user-images.githubusercontent.com/995209/61579165-0ed4dd80-aad8-11e9-8a03-43819a2b9d40.png)

Exemplo da visualização grosseira, apenas para ter uma ideai do desenho final:
![transcoor 04](https://user-images.githubusercontent.com/995209/61579164-0ed4dd80-aad8-11e9-89b7-47e1ff1e14a3.png)

Arquivo dxf gerado, aberto no Draftsight:
![transcoor 05](https://user-images.githubusercontent.com/995209/61579163-0ed4dd80-aad8-11e9-9570-f8c913f3c126.png)
