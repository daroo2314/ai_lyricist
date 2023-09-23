# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('인공지능 작사가(국악전문)')

content = st.text_input('국악가요의 주제를 제시해주세요.')

# result = chat_model.predict(content + "국악가사를 써줘")
# print(result)

if st.button('작사 요청하기'):
   with st.spiner('가사 생각중...'):
      result = chat_model.predict(content + '에대한 국악가사를 써줘')
      st.write(result) 

st.link_button("Go to Roar Festival", "http://daroousa.com/en/bbs/board.php?bo_table=en_w4_c&wr_id=1")