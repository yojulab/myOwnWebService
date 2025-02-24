import streamlit as st
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
api_key = os.getenv("GROQ_API_KEY")


# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state["page"] = "checklist"
if "selected_sections" not in st.session_state:
    st.session_state["selected_sections"] = []
if "user_data" not in st.session_state:
    st.session_state["user_data"] = {}
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def utf8_text(pdf, x, y, text):
    pdf.set_xy(x, y)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=text.encode('utf-8', 'replace').decode('utf-8'), ln=True, align="L")

# 1. 체크리스트 페이지
def checklist_page():
    st.title("📋 항목 선택")
    st.write("원하는 항목을 선택하세요:")
    options = ["세금 관리", "투자 관리", "연금 관리", "보험 관리"]
    selected = st.multiselect("항목 선택", options, default=st.session_state["selected_sections"])
    st.session_state["selected_sections"] = selected
    if st.button("다음 단계로"):
        if selected:
            st.session_state["page"] = "input_form"
        else:
            st.warning("최소 하나의 항목을 선택해주세요.")

# 2. 입력 폼 페이지
def input_form_page():
    st.title("📝 입력 폼")
    st.write("선택한 항목에 대한 정보를 입력하세요:")
    
    for section in st.session_state["selected_sections"]:
        st.subheader(section)
        if section == "세금 관리":
            income = st.number_input("연소득 (만원):", min_value=0, step=100)
            tax_rate = st.slider("세율 (%)", 0, 50, 15)
            st.session_state["user_data"]["세금 관리"] = {"연소득": income, "세율": tax_rate}
        elif section == "투자 관리":
            stock_name = st.text_input("종목 이름:")
            shares = st.number_input("보유 주식 수:", min_value=0, step=1)
            price_per_share = st.number_input("주당 가격 (만원):", min_value=0.0, step=0.1)
            st.session_state["user_data"]["투자 관리"] = {
                "종목 이름": stock_name,
                "보유 주식 수": shares,
                "주당 가격": price_per_share,
            }
        elif section == "연금 관리":
            monthly_contribution = st.number_input("월 납입액 (만원):", min_value=0, step=1)
            years = st.number_input("납입 기간 (년):", min_value=0, step=1)
            interest_rate = st.slider("연 이자율 (%)", 0.0, 10.0, 3.0)
            st.session_state["user_data"]["연금 관리"] = {
                "월 납입액": monthly_contribution,
                "납입 기간": years,
                "연 이자율": interest_rate,
            }
        elif section == "보험 관리":
            insurance_name = st.text_input("보험 이름:")
            monthly_premium = st.number_input("월 보험료 (만원):", min_value=0, step=1)
            coverage_amount = st.number_input("보장 금액 (만원):", min_value=0, step=100)
            st.session_state["user_data"]["보험 관리"] = {
                "보험 이름": insurance_name,
                "월 보험료": monthly_premium,
                "보장 금액": coverage_amount,
            }
    
    if st.button("보고서 생성"):
        if st.session_state["user_data"]:
            st.session_state["page"] = "report"
        else:
            st.warning("모든 선택 항목에 대해 데이터를 입력해주세요.")

# 3. 보고서 생성 페이지
def report_page():
    st.title("📄 생성된 보고서")
    st.write("입력된 데이터를 기반으로 보고서를 생성했습니다.")
    
    for section, data in st.session_state["user_data"].items():
        st.subheader(section)
        for key, value in data.items():
            st.write(f"- **{key}**: {value}")
    
    if st.button("GPT와 상담 시작"):
        st.session_state["page"] = "chat"

# 4. GPT 상담 페이지
# def chat_page():
#     st.title("💬 GPT 상담")
#     st.write("생성된 보고서를 바탕으로 GPT와 상담하세요.")
    
#     user_input = st.text_input("질문을 입력하세요:")
#     if user_input:
#         # 사용자 입력 저장
#         st.session_state["chat_history"].append({"role": "user", "content": user_input})
        
#         # Groq API를 사용하여 GPT 응답 생성
#         from groq import Groq
#         import os

#         client = Groq(api_key=api_key)

#         try:
#             # Groq API 호출
#             chat_completion = client.chat.completions.create(
#                 messages=st.session_state["chat_history"],  # 이전 채팅 기록 포함
#                 model="llama-3.3-70b-versatile"  # 사용할 모델
#             )
#             gpt_response = chat_completion.choices[0].message.content
#         except Exception as e:
#             gpt_response = f"Groq API 호출 중 오류가 발생했습니다: {e}"
        
#         # GPT 응답 저장
#         st.session_state["chat_history"].append({"role": "assistant", "content": gpt_response})
    
#     # 채팅 기록 표시
#     for chat in st.session_state["chat_history"]:
#         if chat["role"] == "user":
#             st.write(f"👤 사용자: {chat['content']}")
#         else:
#             st.write(f"🤖 GPT: {chat['content']}")
    
#     if st.button("최종 보고서 다운로드"):
#         st.session_state["page"] = "download"


def chat_page():
    st.title("💬 GPT 상담")
    st.write("생성된 보고서를 바탕으로 GPT와 상담하세요.")
    
    user_input = st.text_input("질문을 입력하세요:")
    if user_input:
        # 사용자 입력 저장
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        
        # Groq API를 사용하여 GPT 응답 생성
        from groq import Groq
        import os

        client = Groq(api_key=api_key)

        try:
            # Groq API 호출
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "너는 사람들에게 유능한 Wrap Account를 해주는 펀드 매니저야, 너의 고객은 한국 사람밖에 없으니 한국말로만 대답을 해야해 그렇지 않으면 너의 직업은 위태로워"},
                    *st.session_state["chat_history"]  # 이전 채팅 기록 포함
                ],
                model="llama-3.3-70b-versatile"  # 사용할 모델
            )
            gpt_response = chat_completion.choices[0].message.content
        except Exception as e:
            gpt_response = f"Groq API 호출 중 오류가 발생했습니다: {e}"
        
        # GPT 응답 저장
        st.session_state["chat_history"].append({"role": "assistant", "content": gpt_response})
    
    # 채팅 기록 표시
    for chat in st.session_state["chat_history"]:
        if chat["role"] == "user":
            st.write(f"👤 사용자: {chat['content']}")
        else:
            st.write(f"🤖 GPT: {chat['content']}")
    
    if st.button("최종 보고서 다운로드"):
        st.session_state["page"] = "download"



# 5. PDF 다운로드 페이지
# PDF 다운로드 페이지

def download_page():
    st.title("📥 최종 보고서 다운로드")
    st.write("최종 보고서를 PDF로 다운로드하세요.")

    # PDF 생성
    pdf = FPDF()
    pdf.add_page()

    # 유니코드 폰트 추가 (절대 경로 설정)
    font_path = os.path.abspath('Jo2-j/myOwnWebService/NotoSans-Italic-VariableFont_wdth,wght.ttf')  # 절대 경로 사용
    
    pdf.add_font('NotoSans', '', font_path, uni=True)
    pdf.set_font('NotoSans', size=12)

    # 제목 추가
    pdf.cell(200, 10, txt="최종 보고서", ln=True, align="C")
    pdf.ln(10)

    # 사용자 데이터 추가
    if "user_data" in st.session_state:
        for section, data in st.session_state["user_data"].items():
            pdf.cell(200, 10, txt=section, ln=True, align="L")
            for key, value in data.items():
                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align="L")
            pdf.ln(5)

    # GPT 상담 내용 추가
    if "chat_history" in st.session_state:
        pdf.ln(10)
        pdf.cell(200, 10, txt="GPT 상담 내용", ln=True, align="L")
        for chat in st.session_state["chat_history"]:
            if chat["role"] == "user":
                pdf.cell(200, 10, txt=f"사용자: {chat['content']}", ln=True, align="L")
            else:
                pdf.cell(200, 10, txt=f"GPT: {chat['content']}", ln=True, align="L")

    # PDF 저장
    pdf_output = "final_report.pdf"
    pdf.output(pdf_output)

    # PDF 다운로드 버튼 생성
    with open(pdf_output, "rb") as f:
        st.download_button(
            label="📄 PDF 다운로드",
            data=f,
            file_name="final_report.pdf",
            mime="application/pdf"
        )


# 메인 함수
def main():
    if st.session_state["page"] == "checklist":
        checklist_page()
    elif st.session_state["page"] == "input_form":
        input_form_page()
    elif st.session_state["page"] == "report":
        report_page()
    elif st.session_state["page"] == "chat":
        chat_page()
    elif st.session_state["page"] == "download":
        download_page()

if __name__ == "__main__":
    main()

