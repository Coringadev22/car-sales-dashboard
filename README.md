📊 Car Sales Dashboard – Streamlit App
Este projeto é um dashboard interativo criado com Python, Pandas, Plotly Express e Streamlit, com objetivo de realizar uma análise exploratória dos anúncios de carros usados nos Estados Unidos.

Você pode acessar o app online aqui:
🔗 https://car-sales-dashboard-x6wa.onrender.com/

✅ Funcionalidades
O aplicativo permite ao usuário:

Visualizar um histograma interativo da quilometragem dos carros (odômetro)

Gerar um gráfico de dispersão entre o ano do modelo e o preço dos carros

Usar caixas de seleção (checkbox) para ativar os gráficos

Ver os dados renderizados dinamicamente usando Plotly

📸 Imagens do App
Histograma do Hodômetro

Gráfico de Dispersão: Preço vs Ano

🗂 Estrutura do Projeto
car-sales-dashboard/
├── app.py → Arquivo principal do Streamlit
├── vehicles.csv → Base de dados
├── requirements.txt → Lista de dependências
├── README.md → Este arquivo
├── .streamlit/
│ └── config.toml → Configuração para deploy no Render
└── notebooks/
  └── EDA.ipynb → Análise exploratória em Jupyter Notebook

🚀 Tecnologias Utilizadas
Python 3.11+

Pandas

Plotly Express

Streamlit

Git & GitHub

Render.com (deploy gratuito)

▶️ Como Executar Localmente
Crie e ative o ambiente virtual:

Windows:

nginx
Copiar
Editar
python -m venv venv
venv\Scripts\activate
Linux/Mac:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

nginx
Copiar
Editar
pip install -r requirements.txt
Rode o app:

arduino
Copiar
Editar
streamlit run app.py
🌐 Deploy no Render
Este projeto foi publicado gratuitamente no Render.com, utilizando as seguintes configurações:

Build Command: pip install --upgrade pip && pip install -r requirements.txt

Start Command: streamlit run app.py

Root Directory: (deixado em branco)

✍️ Autor
Desenvolvido por Lucas Coelho 🚀
Entre em contato: https://www.linkedin.com/in/lucas-coelho-ba756318b/

