# SystemMessage : AI에게 상황을 지정하거나 역활 부여 - 페르소나 , Hummesage가 같아도 상황이 다르면 다른 메시지로 인식함 
# HumanMessage : 사용자 입력 메시지, 질문 전달 
# AIMessage: AI 답변 메시지 

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = "AIzaSyAKwlrrPs7Wl_Wqz5t6mCjujxU56HXUgNc"

model = ChatGoogleGenerativeAI(
    model="gemini-pro",  # 사용할 모델을 지정합니다.
    convert_system_message_to_human=True,  # 시스템 메시지를 사람 메시지로 변환할지 여부를 설정합니다.
    google_api_key=GOOGLE_API_KEY
)

chat_model_response = model.invoke(
    [
        # 시스템 메시지로 "yes 또는 no로만 대답하세요."라는 내용을 전달합니다.
        SystemMessage(content="당신은 농장에서 일하는  전문가입니다."),
        # 사람 메시지로 "사과는 과일인가요?"라는 질문을 전달합니다.
        HumanMessage(content="토마토는 과일인가요?"),
    ]
)

print(chat_model_response.content)