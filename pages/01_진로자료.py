import streamlit as st

# 샘플 데이터
majors_data = {
    "AI학과": {
        "설명": "인공지능 이론과 응용 기술을 배우는 학과로, 프로그래밍, 데이터 분석, 머신러닝 등을 학습합니다.",
        "주요 과목": ["파이썬 프로그래밍", "머신러닝", "딥러닝", "AI 윤리", "데이터 구조"],
        "졸업 후 진로": ["AI 개발자", "데이터 사이언티스트", "AI 연구원"]
    },
    "로봇공학과": {
        "설명": "로봇 설계, 제어, 인공지능 융합 기술을 배우는 학과입니다.",
        "주요 과목": ["로봇제어", "센서기술", "임베디드 시스템", "AI기초"],
        "졸업 후 진로": ["로봇 엔지니어", "스마트팩토리 전문가", "로봇코치"]
    }
}

future_jobs_data = {
    "AI 윤리전문가": {
        "설명": "AI 기술의 윤리적 사용을 위한 가이드라인을 제시하고 법적 이슈를 분석하는 직업입니다.",
        "주요 역량": ["AI 기술 이해", "윤리학 지식", "정책 분석력"],
        "관련 전공": ["철학", "컴퓨터공학", "법학"],
        "활동 분야": ["정부 정책 기관", "AI 기업", "국제기구"]
    },
    "로봇코치": {
        "설명": "로봇의 학습 및 행동을 훈련시키고 조정하는 역할을 수행하는 미래형 직업입니다.",
        "주요 역량": ["로봇제어", "프로그래밍", "상황판단 능력"],
        "관련 전공": ["로봇공학", "전자공학", "AI학과"],
        "활동 분야": ["로봇 교육기관", "로봇개발 기업", "헬스케어 로봇 분야"]
    }
}

# Streamlit UI
st.title("📘 진로 콘텐츠 대시보드")

menu = st.sidebar.radio("콘텐츠 선택", ["한눈에 보는 학과", "미리보는 미래 직업"])

if menu == "한눈에 보는 학과":
    st.header("📚 한눈에 보는 학과")
    selected_major = st.selectbox("학과를 선택하세요", list(majors_data.keys()))
    
    info = majors_data[selected_major]
    st.subheader(f"✅ {selected_major}")
    st.write(f"**설명:** {info['설명']}")
    st.write(f"**배우는 주요 과목:**")
    for subject in info['주요 과목']:
        st.markdown(f"- {subject}")
    st.write(f"**졸업 후 진로:**")
    for job in info['졸업 후 진로']:
        st.markdown(f"- {job}")

elif menu == "미리보는 미래 직업":
    st.header("🚀 미리보는 미래 직업")
    selected_job = st.selectbox("직업을 선택하세요", list(future_jobs_data.keys()))

    job_info = future_jobs_data[selected_job]
    st.subheader(f"💼 {selected_job}")
    st.write(f"**설명:** {job_info['설명']}")
    st.write(f"**주요 역량:**")
    for skill in job_info['주요 역량']:
        st.markdown(f"- {skill}")
    st.write(f"**관련 전공:**")
    for major in job_info['관련 전공']:
        st.markdown(f"- {major}")
    st.write(f"**활동 분야:**")
    for field in job_info['활동 분야']:
        st.markdown(f"- {field}")
