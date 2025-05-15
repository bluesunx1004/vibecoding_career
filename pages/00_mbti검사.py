import streamlit as st
import pandas as pd
import os

# 질문 리스트
questions = [
    ("나는 사람들과 함께 있을 때 에너지가 생긴다.", "E", "I"),
    ("나는 혼자 있는 시간이 필요하다.", "I", "E"),
    ("나는 실제적인 것에 관심이 많다.", "S", "N"),
    ("나는 상상하는 것을 즐긴다.", "N", "S"),
    ("나는 논리적으로 사고한다.", "T", "F"),
    ("나는 감정을 중시한다.", "F", "T"),
    ("나는 계획 세우기를 좋아한다.", "J", "P"),
    ("나는 유연하고 즉흥적인 것을 선호한다.", "P", "J"),
    ("나는 여러 사람과 어울리는 걸 좋아한다.", "E", "I"),
    ("나는 직감에 의존하는 편이다.", "N", "S"),
    ("나는 결정을 내릴 때 감정을 고려한다.", "F", "T"),
    ("나는 일정을 정해두는 걸 좋아한다.", "J", "P"),
]

mbti_descriptions = {
    "ISTJ": "신중하고 책임감 있는 관리자형",
    "ISFJ": "성실하고 따뜻한 보호자형",
    "INFJ": "통찰력 있고 헌신적인 이상주의자형",
    "INTJ": "전략적이고 논리적인 사색가형",
    "ISTP": "과묵하고 논리적인 실용주의자형",
    "ISFP": "온화하고 겸손한 예술가형",
    "INFP": "이상적이고 성실한 중재자형",
    "INTP": "논리적이고 호기심 많은 사색가형",
    "ESTP": "친화력 있고 에너지 넘치는 활동가형",
    "ESFP": "사교적이고 수용적인 연예인형",
    "ENFP": "열정적이고 창의적인 활동가형",
    "ENTP": "재치 있고 풍부한 아이디어형",
    "ESTJ": "현실적이고 조직적인 관리자형",
    "ESFJ": "사람을 잘 돌보는 사교적인 조정자형",
    "ENFJ": "따뜻하고 책임감 있는 지도자형",
    "ENTJ": "단호하고 지도력 있는 통솔자형",
}

# 결과 통계 파일
stats_file = "mbti_stats.csv"

# 통계 파일 초기화 함수
def initialize_stats():
    if not os.path.exists(stats_file):
        all_types = list(mbti_descriptions.keys())
        df = pd.DataFrame({"type": all_types, "count": [0] * len(all_types)})
        df.to_csv(stats_file, index=False)

# 통계 업데이트 함수
def update_stats(mbti_type):
    df = pd.read_csv(stats_file)
    if mbti_type in df["type"].values:
        df.loc[df["type"] == mbti_type, "count"] += 1
    else:
        new_row = pd.DataFrame({"type": [mbti_type], "count": [1]})
        df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(stats_file, index=False)

# 점수 초기화
scores = {letter: 0 for letter in "EISNTFJP"}

# UI
st.title("🧠 MBTI 성격유형 검사 + 통계")

st.write("총 12개의 질문에 답하고 본인의 성격 유형을 확인해보세요.")

# 질문 출력
for i, (question, a, b) in enumerate(questions):
    answer = st.radio(f"{i+1}. {question}", (a, b), key=i)
    scores[answer] += 1

# 결과 계산 및 저장
if st.button("결과 보기"):
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"

    st.subheader(f"📌 당신의 MBTI는: {mbti}")
    st.write(f"👉 {mbti_descriptions.get(mbti, '설명이 없습니다.')}")

    # 통계 처리
    initialize_stats()
    update_stats(mbti)

    # 통계 시각화
    st.markdown("---")
    st.subheader("📊 전체 검사 통계")

    stats_df = pd.read_csv(stats_file).sort_values(by="count", ascending=False)
    st.bar_chart(data=stats_df, x="type", y="count")

