
# streamlit run timmaia_app.py

import streamlit as st
import numpy as np
from PIL import Image
import time
import torch
from torchvision import transforms

# definindo as transformações para imagens novas a serem submetidas ao modelo!
image_size = 100

# Transformando as imagens
redimensionamento_imagem = transforms.Compose([
        transforms.Resize(size=[image_size, image_size]),
        transforms.ToTensor(),
    ])


def predicao_tim_maia_aleatorio(model, test_image):
    transform = redimensionamento_imagem

    test_image_tensor = transform(test_image)

    if torch.cuda.is_available():
        test_image_tensor = test_image_tensor.view(1, 3, image_size, image_size).cuda()
    else:
        test_image_tensor = test_image_tensor.view(1, 3, image_size, image_size)
    with torch.no_grad():
        model.eval()
        out = model(test_image_tensor)
        ps = torch.exp(out)
        topk, topclass = ps.topk(2, dim=1)
        # Calcula a diferença entre as duas maiores probabilidades
        diff_prob = topk[0][0] - topk[0][1]
    return diff_prob.item()


def predicao_tim_maia(model, test_image):
    '''
    Função para realizar a predição do status do AR
    Parâmetros
        :param model: modelo para testar
        :param test_image_name: imagem teste
    '''
    transform = redimensionamento_imagem

    test_image_tensor = transform(test_image)

    if torch.cuda.is_available():
        test_image_tensor = test_image_tensor.view(1, 3, image_size, image_size).cuda()
    else:
        test_image_tensor = test_image_tensor.view(1, 3, image_size, image_size)

    # Não precisa atualizar os coeficientes do modelo
    with torch.no_grad():
        model.eval()

        # Modelo retorna as probabilidades em log (log softmax)
        out = model(test_image_tensor)

        # torch.exp para voltar a probabilidade de log para a probabilidade linear
        ps = torch.exp(out)

        # topk retorna o os k maiores valores do tensor
        # o tensor de probabilidades vai trazer na 1a posição a classe com maior
        # probabilidade de predição
        topk, topclass = ps.topk(2, dim=1)
        
        classe_com_maior_prob = np.argmax(topk.cpu().numpy()[0])

    return topclass[0][0]

# Designing the interface
st.title("Tim Maia - Pytorch 🖼️🍕🍔")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        min-width: 450px; /* Altere esse valor para o tamanho que desejar */
        max-width: 450px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# For newline
st.write('\n')

image = Image.open('./images/tim_maia.png')
show = st.image(image, width=500)

st.sidebar.title("✅ Suba uma imagem de uma pizza ou hambúrguer para nosso querido Tim Maia degustar....")

# Disabling warning
#st.set_option('deprecation.showfileUploaderEncoding', False)
# Choose your own image
uploaded_file = st.sidebar.file_uploader(" ", type=['jpg', 'jpeg'])

if uploaded_file is not None:
    u_img = Image.open(uploaded_file)
    
    show.image(u_img, 'Imagem enviada!', width=500)
    # We preprocess the image to fit in algorithm.

# For newline
st.sidebar.write('\n')

# Carregar o modelo
modelo = torch.load('./data/modelos/melhor_modelo.pt', weights_only=False)

# Design do botão
st.markdown("""
    <style>
    [data-testid="stSidebar"] button[kind="primary"] {
        height: 5em !important; /* Altura bem grande */
        background-color: #FF4B4B !important;
        border-radius: 15px !important;
        border: none !important;
        width: 100% !important;
    }

    [data-testid="stSidebar"] button[kind="primary"] p {
        font-size: 24px !important; 
        font-weight: bold !important;
        color: white !important;
    }

    [data-testid="stSidebar"] button[kind="primary"]:hover {
        background-color: #000000 !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

if st.sidebar.button("🎤 ANALISAR LANCHE DO TIM! ", type="primary", use_container_width=True):
    if uploaded_file is None:
        st.sidebar.write("<h2 style='font-size: 25px;'>Envie uma imagem para o Tim Maia!</h2>", unsafe_allow_html=True)
    else:
        with st.spinner('Tim Maia experimentando...'):
            prediction = predicao_tim_maia(modelo, u_img)
            prediction_random = predicao_tim_maia_aleatorio(modelo, u_img)
            #time.sleep(2)
            st.success('Imagem analisada!')

        st.sidebar.markdown("<h2 style='font-size: 25px;'>Tim Maia disse que a imagem é de ...</h2>", unsafe_allow_html=True)

        if prediction_random < 0.98:
            print(prediction_random)
            st.sidebar.markdown("<h1 style='color: #FF4B4B; font-size: 50px; font-weight: bold; line-height: 1;'>Não queroo!!! 😡</h1>", unsafe_allow_html=True)
            
            show.image('./images/tim_maia_pistola.png', 'Tim Maia tá pistola a imagem não é de pizza nem hambúrguer!', use_container_width=True)
            
        elif prediction == 0:
            print(prediction)
            st.sidebar.markdown("<h1 style='color: #FFA500; font-size: 32px; font-weight: bold; line-height: 1;'>Hambúrguer!!! Querooo!🍔</h1>", unsafe_allow_html=True)
            
            show.image('./images/tim_maia_feliz.png', 'Tim Maia tá felizão o hambúrguer!', use_container_width=True)
            
        elif prediction == 1:
            print(prediction)
            st.sidebar.markdown("<h1 style='color: #2E8B57; font-size: 32px; font-weight: bold; line-height: 1;'>Pizza!!! Adoro pizaa!🍕</h1>", unsafe_allow_html=True)
            
            show.image('./images/tim_maia_feliz.png', 'Tim Maia tá felizão com a pizza!', use_container_width=True)
