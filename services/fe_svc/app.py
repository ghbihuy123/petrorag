import streamlit as st
import requests
import json
from fe_svc.settings import common_settings
st.set_page_config(page_title="Q&A Assistant", layout="wide")

from fe_svc.global_css import sidebar_css

st.title("❓ Chatbot hỏi đáp SAP-PM TKNB")
st.write("Hỏi tôi bất cứ câu hỏi nào về phần mềm SAP-PM!")

# FastAPI backend URL
CHAT_ENDPOINT = common_settings.chat_endpoint

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "error" not in st.session_state:
    st.session_state.error = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Display error if exists
if st.session_state.error:
    st.error(st.session_state.error)
    st.session_state.error = None

# Input field for user question
user_input = st.chat_input("Nhập câu hỏi ở đây...")

if user_input:
    sidebar_css = sidebar_css
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Show loading state
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Send request to FastAPI backend
                payload = {"query": user_input}
                response = requests.post(f"{CHAT_ENDPOINT}/api/chat/query", json=payload, timeout=80)
                
                if response.status_code == 200:
                    data = response.json()
                    assistant_response = data.get("response", "No response received")
                    st.write(assistant_response)
                else:
                    error_msg = f"Error: {response.status_code} - {response.text}"
                    st.error(error_msg)
                    st.session_state.error = error_msg
                    assistant_response = error_msg
            
            except requests.exceptions.ConnectionError:
                error_msg = "❌ Cannot connect to backend at localhost:8081. Make sure FastAPI server is running."
                st.error(error_msg)
                st.session_state.error = error_msg
                assistant_response = error_msg
            
            except requests.exceptions.Timeout:
                error_msg = "⏱️ Request timeout. The backend took too long to respond."
                st.error(error_msg)
                st.session_state.error = error_msg
                assistant_response = error_msg
            
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.error = error_msg
                assistant_response = error_msg
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Sidebar with options
with st.sidebar:
    st.image("fe_svc/public/petrologo.png", width=150) 
    # st.header("⚙️ Settings")
    
    st.divider()
    
    # if st.button("🗑️ Clear Chat History"):
    #     st.session_state.messages = []
    #     st.rerun()
    
    # st.divider()
    
    example_queries = [
        "Tìm cho tôi mã object type của máy nén khí",
        "Thuật ngữ trong SAP-PM",
        "Tổng hợp t-code trong SAP-PM"
    ]
    
    for query in example_queries:
        if st.button(query, key=query):
            # Add user message
            with st.spinner("Thinking..."):
                st.session_state.messages.append({"role": "user", "content": query})
                
                # Get response from backend
                try:
                    payload = {"query": query}
                    response = requests.post(f"{CHAT_ENDPOINT}/api/chat/query", json=payload, timeout=30)
                    
                    if response.status_code == 200:
                        data = response.json()
                        assistant_response = data.get("response", "No response received")
                    else:
                        assistant_response = f"Error: {response.status_code}"
                except Exception as e:
                    assistant_response = f"Error: {str(e)}"
                
                # Add assistant response
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                st.rerun()