import streamlit as st

st.title("曖昧な指示に対話的に応答するLLMベースのロボット行動計画生成システムデモアプリ")
st.markdown("ユーザーの指示に応じて、性格ごとに対話を行い、最終的に行動計画を生成します。")

personality_numbers = list(range(1, 4))
personality_prompts = ["prompt1", "prompt2", "prompt3", "prompt4"]

personality = st.selectbox("好きな数字を選んでください", personality_numbers)
system_prompt = personality_prompts[int(personality)]

# 状態管理
if "chat_history" not in st.session_state:
    st.session_state.history = [system_prompt] # ユーザーには非表示の初期プロンプト
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []
if "latest_plan" not in st.session_state:
    st.session_state.latest_plan = None

st.subheader("ロボットとの会話")
for entry in st.session_state.chat_log:
    st.chat_message(entry["role"]).write(entry["content"])

user_input = st.chat_input("指示を入力してください")