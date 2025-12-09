import pandas as pd
from langchain.tools import tool

FILE_PATH = "/home/luu-quang-huy/project/chatpetro/services/chat_svc/chat_svc/data/common_question.xlsx"

def load_and_prepare_df():
    df = pd.read_excel(FILE_PATH)
    df.dropna(how='all', inplace=True)

    # fill NA theo từng nhóm câu hỏi
    df['group'] = df['CÂU HỎI (INPUT)'].notna().cumsum()
    df['CÂU HỎI (INPUT)'] = df.groupby('group')['CÂU HỎI (INPUT)'].ffill()
    df.drop(columns=['group'], inplace=True)
    return df


@tool("list_all_questions")
def list_all_questions(_=None) -> str:
    """
    Đây là các câu hỏi thường gặp liên quan đến SAP-PM. 
    Nếu như khách hàng có câu hỏi liên quan đến SAP-PM, hãy sử dụng tool này để tìm câu hỏi thường gặp.
    """
    df = load_and_prepare_df()
    questions = df["CÂU HỎI (INPUT)"].dropna().unique().tolist()

    text = "📌 DANH SÁCH CÂU HỎI:\n"
    text += "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions))
    return text


@tool("get_answers_for_question")
def get_answers_for_question(question: str) -> str:
    """
    Đây là các trả lời cho các câu hỏi liên quan đến SAP-PM.
    Chỉ buộc gọi tool này để lấy các giá trị, chỉ sau khi đã gọi tool list_all_questions
    """
    df = load_and_prepare_df()

    matched_rows = df[df["CÂU HỎI (INPUT)"] == question]

    if matched_rows.empty:
        return f"⚠️ Không tìm thấy câu hỏi: {question}"

    outputs = matched_rows["CÂU TRẢ LỜI (OUTPUT)"].dropna().tolist()

    if not outputs:
        return f"⚠️ Không có OUTPUT nào cho câu hỏi: {question}"

    text = f"📘 CÁC GIÁ TRỊ CỦA CÂU HỎI:\n{question}\n\n"
    text += "\n".join(f"- {o}" for o in outputs)
    return text