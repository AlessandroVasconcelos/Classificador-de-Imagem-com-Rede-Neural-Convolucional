# Classificador de Imagem com Rede Neural Convolucional (CNN) 🖼️🍕🍔

## 📌 Visão Geral
<p align="justify">
Este projeto consiste no treinamento de um modelo de aprendizado profundo para predição de imagens, utilizando Redes Neurais Convolucionais (CNN). O problema foi adaptado para classificar imagens entre duas categorias: pizza e hambúrguer. O repositório apresenta uma abordagem prática de Deep Learning, explorando desde o treinamento do modelo até sua utilização em uma interface interativa. Durante o desenvolvimento, são abordados conceitos fundamentais como:
</p>
  
- Diferenças em relação às redes neurais tradicionais (MLP)
- Extração automática de características em imagens
- Conceito de **Transfer Learning**
- Aplicação prática com interface interativa

---

## 🚀 Como Rodar o Projeto Localmente

Este projeto foi desenvolvido em Python com biblioteca Streamlit para visualização.

### ⚙️ Passo a Passo

**1. Clone o repositório**
```bash
git clone https://github.com/AlessandroVasconcelos/Classificador-de-Imagem-com-Rede-Neural-Convolucional.git
cd Classificador-de-Imagem-com-Rede-Neural-Convolucional
```
**Crie o ambiente virtual**
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```


**4. Treine o modelo**

Execute o notebook:

[Image_Classifier_with_Convolutional_Neural_Network.ipynb](https://github.com/AlessandroVasconcelos/Classificador-de-Imagem-com-Rede-Neural-Convolucional/blob/main/Image_Classifier_with_Convolutional_Neural_Network.ipynb)

**5. Execute a aplicação**
```bash
streamlit run timmaia_app.py
```

🌐 Acesso local

A aplicação será aberta automaticamente no navegador:

👉 http://localhost:8501

---

### **🖼️ Dica - Download de Imagens:**<br>
Se quiser aumentar a quantidade de dados e melhorar o desempenho do modelo, você pode coletar mais imagens para o treinamento. Uma forma prática de fazer isso é utilizando a extensão do Chrome [Bulk Image Downloader](https://chrome.google.com/webstore/detail/bulk-image-downloader/lamfengpphafgjdgacmmnpakdphmjlji?hl=en) , que permite baixar várias imagens rapidamente. Armazene as imagens nas pastas teste, treino e validação.

---

## 👨‍🏫 Professor/Orientador:
Gilzamir Ferreira Gomes.

---

## 📚 Referências:

- 🎥 **Tutorial base utilizado no projeto:**  
  https://youtu.be/n1TUIvazOCg  
- 📺 **Canal:** Let's Datah


## 🛠️ Tecnologias Utilizadas

<a href ="https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/jupyter/index.html"><img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"></a>
<a href="https://streamlit.io/" style="text-decoration:none;"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"></a>
<a href="https://pytorch.org/"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
<a href="https://pytorch.org/vision/stable/index.html"><img src="https://img.shields.io/badge/Torchvision-darkred?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
<a href="https://numpy.org/"><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"></a>
<a href = "https://www.python.org/"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></a>
<a href = "https://code.visualstudio.com/"><img src="https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white"></a>
