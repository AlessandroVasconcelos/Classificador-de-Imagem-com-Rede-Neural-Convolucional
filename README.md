# Classificador de Imagem com Rede Neural Convolucional

## Visão Geral
Esse repositório é baseado na implementação do vídeo sobre Redes Neurais Convolucionais no Youtube do [Canal Let's Datah](https://www.youtube.com/@letsdataAI).

- Link para o vídeo tutorial: (https://youtu.be/n1TUIvazOCg)

O tutorial aborda a aprendizagem de máquina, concentrando-se nas Redes Neurais Convolucionais(CNN), proporcionando uma base sólida para a implementação em projetos. Explora-se a teoria por trás das CNNs, destacando suas diferenças em relação às redes neurais totalmente conectadas, e é apresentado o conceito de transfer learning. Além disso, é demonstrado uma aplicação prática utilizando o Streamlit para implementar um classificador de imagens. O vídeo fornece explicações detalhadas do código, passo a passo, para garantir uma compreensão completa. No exemplo prático, a aplicação visa ajudar o lendário cantor de soul Tim Maia a distinguir imagens entre chocolate, guaraná e Coca-Cola, **entretanto nesse repositório é utilizada a rede neural para aprender a diferenciar imagens de pizza e hambúrguer, como também imagens aleatórias.**

## Dependências

Certifique-se de ter o Python instalado. Instale as dependências usando o seguinte comando:

```bash
pip install notebook torch torchvision torchaudio matplotlib streamlit
```

**Download de Imagens:**<br>
Utilize a extensão do Chrome [Bulk Image Downloader](https://chrome.google.com/webstore/detail/bulk-image-downloader/lamfengpphafgjdgacmmnpakdphmjlji?hl=en) para baixar muitas imagens. Armazene as imagens nas pastas teste, treino e validacao.

## Executando o Projeto
- Faça o download do repositório [aqui](https://github.com/AlessandroVasconcelos/Classificador-de-Imagem-com-Rede-Neural-Convolucional/archive/refs/heads/main.zip), extraia o conteúdo do arquivo zip para o diretório raiz do seu sistema. Isso facilitará a manipulação dos dados e garantirá que a estrutura do projeto seja preservada.
- Execute o notebook jupyter [Image_Classifier_with_Convolutional_Neural_Network.ipynb](https://github.com/AlessandroVasconcelos/Classificador-de-Imagem-com-Rede-Neural-Convolucional/blob/41aab81b1b7f957ca3b12d02c90358b1f1f43641/Image_Classifier_with_Convolutional_Neural_Network.ipynb) em sua máquina para treinar o modelo da CNN.<br>
- Para visualizar os resultados, execute [timmaia_app.py](https://github.com/AlessandroVasconcelos/Classificador-de-Imagem-com-Rede-Neural-Convolucional/blob/e82bec10679771c7ef445058ffa702052cf724dd/timmaia_app.py) com o aplicativo Streamlit no terminal:
```bash
streamlit run timmaia_app.py
```
- Acesse o aplicativo no navegador em localhost e faça os testes com as imagens.


## Professor/Orientador:
Gilzamir Ferreira Gomes.

## Ferramentas Utilizadas

- <a href ="https://colab.google/"><img src="https://img.shields.io/badge/google_colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"></a>
<a href ="https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/jupyter/index.html"><img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"></a>
<a href ="https://www.anaconda.com/download"><img src="https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white"></a>
- <a href = "https://code.visualstudio.com/"><img src="https://img.shields.io/badge/-Visual%20Studio%20Code-%23333?style=for-the-badge&logo=visual-studio-code&logoColor=%22red%22%20arget=%22_blank"></a>
<a href = "https://www.python.org/"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></a>
