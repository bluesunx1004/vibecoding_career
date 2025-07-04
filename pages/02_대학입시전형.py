import streamlit as st
import pandas as pd

# -------------------- 대학별 요약표 데이터 --------------------
admission_data = [
    # 수도권 주요 대학
    {"대학": "서울대", "수시 비율": "78%", "정시 비율": "22%", "수시 주요 전형": "일반전형(학종)", "정시 전형": "수능 100%", "최저기준": "3개 영역 등급 합 5"},
    {"대학": "연세대", "수시 비율": "60%", "정시 비율": "40%", "수시 주요 전형": "활동우수형, 국제형", "정시 전형": "수능 100% (가산점)", "최저기준": "일부 전형 제외하고 없음"},
    {"대학": "고려대", "수시 비율": "65%", "정시 비율": "35%", "수시 주요 전형": "학업우수형, 계열적합형", "정시 전형": "수능 + 학생부 10%", "최저기준": "국/수/탐 3합 6"},
    {"대학": "서강대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "자기주도형", "정시 전형": "수능 100%", "최저기준": "최저학력 기준 없음"},
    {"대학": "성균관대", "수시 비율": "67%", "정시 비율": "33%", "수시 주요 전형": "계열모집, 종합", "정시 전형": "수능 100%", "최저기준": "전형에 따라 적용"},
    {"대학": "경희대", "수시 비율": "75%", "정시 비율": "25%", "수시 주요 전형": "교과, 네오르네상스", "정시 전형": "수능 100%", "최저기준": "교과 전형 일부 적용"},
    {"대학": "서울시립대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "교과, 종합", "정시 전형": "수능 100%", "최저기준": "일부 전형만 적용"},
    {"대학": "이화여대", "수시 비율": "73%", "정시 비율": "27%", "수시 주요 전형": "미래인재, 고교추천", "정시 전형": "수능 100%", "최저기준": "전형별 상이"},
    {"대학": "건국대", "수시 비율": "72%", "정시 비율": "28%", "수시 주요 전형": "KU논술, 학교추천", "정시 전형": "수능 100%", "최저기준": "논술 제외 일부 적용"},
    {"대학": "동국대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "Do Dream, 추천", "정시 전형": "수능 100%", "최저기준": "전형에 따라 상이"},
    {"대학": "홍익대", "수시 비율": "69%", "정시 비율": "31%", "수시 주요 전형": "교과, 논술", "정시 전형": "수능 100%", "최저기준": "논술형 최저 있음"},
    {"대학": "숙명여대", "수시 비율": "74%", "정시 비율": "26%", "수시 주요 전형": "숙명인재, 교과우수자", "정시 전형": "수능 100%", "최저기준": "숙명인재 적용"},
    {"대학": "인하대", "수시 비율": "72%", "정시 비율": "28%", "수시 주요 전형": "교과, 종합", "정시 전형": "수능 100%", "최저기준": "전형별 상이"},
    {"대학": "아주대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "ACE전형, 다산인재", "정시 전형": "수능 100%", "최저기준": "일부 전형만 적용"},
    {"대학": "단국대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "DKU인재, 학교추천", "정시 전형": "수능 100%", "최저기준": "전형별 상이"},
    {"대학": "가톨릭대", "수시 비율": "68%", "정시 비율": "32%", "수시 주요 전형": "학교추천, 가톨릭인재", "정시 전형": "수능 100%", "최저기준": "교과 전형 적용"},
    {"대학": "인천대", "수시 비율": "75%", "정시 비율": "25%", "수시 주요 전형": "지역인재, 교과우수자", "정시 전형": "수능 100%", "최저기준": "일부 전형만 적용"},
    {"대학": "경기대", "수시 비율": "73%", "정시 비율": "27%", "수시 주요 전형": "교과우수자, 일반학생", "정시 전형": "수능 100%", "최저기준": "교과 일부 적용"},
    # 지역거점국립대
    {"대학": "부산대", "수시 비율": "70%", "정시 비율": "30%", "수시 주요 전형": "교과성적우수자, 지역인재", "정시 전형": "수능 100%", "최저기준": "계열별 등급 기준 상이"},
    {"대학": "경북대", "수시 비율": "73%", "정시 비율": "27%", "수시 주요 전형": "교과, 종합", "정시 전형": "수능 100%", "최저기준": "일부 전형 적용"},
    {"대학": "전남대", "수시 비율": "75%", "정시 비율": "25%", "수시 주요 전형": "교과, 전공적합", "정시 전형": "수능 100%", "최저기준": "전형에 따라 상이"},
    {"대학": "충북대", "수시 비율": "74%", "정시 비율": "26%", "수시 주요 전형": "교과, 지역인재", "정시 전형": "수능 100%", "최저기준": "대부분 전형 없음"},
    {"대학": "강원대", "수시 비율": "76%", "정시 비율": "24%", "수시 주요 전형": "교과(일반), 지역인재", "정시 전형": "수능 100%", "최저기준": "전형별 상이"}
]

# 데이터프레임으로 변환
df = pd.DataFrame(admission_data)

# -------------------- UI 구성 --------------------
st.title("🎓 대학 입시 통합 안내 대시보드")

menu = st.sidebar.radio("🔎 메뉴 선택", [
    "📘 전형별 안내",
    "📊 대학별 수시/정시 요약표",
    "🎯 맞춤형 지원 가능성 분석"
])

# -------------------- 전형별 안내 --------------------
if menu == "📘 전형별 안내":
    selected_type = st.radio("전형을 선택하세요", ["📌 수시 전형", "📌 정시 전형"])

    if selected_type == "📌 수시 전형":
        st.header("📌 수시 전형이란?")
        st.write("""
        수시 전형은 **수능 이전에 선발**하는 대학 입학 전형으로, 다양한 서류와 활동을 바탕으로 학생의 가능성과 과정을 평가합니다.
        """)

        st.subheader("✅ 수시 전형 세부 유형")

        with st.expander("📘 학생부 교과 전형"):
            st.write("""
            - **내신 성적(교과 성적)** 중심으로 선발하는 전형입니다.
            - 비교과(동아리, 봉사 등)는 반영하지 않거나 최소한만 반영합니다.
            - 일부 대학은 **수능 최저학력기준**을 적용합니다.
            """)

        with st.expander("📙 학생부 종합 전형"):
            st.write("""
            - **내신 + 비교과 활동 + 자기소개서 + 면접** 등을 종합적으로 평가합니다.
            - 전공적합성, 발전 가능성, 인성 등을 중요하게 봅니다.
            - 수능 최저를 **적용하지 않는 학교도 많지만**, 일부 상위권 대학은 적용합니다.
            """)

        st.subheader("🔍 수능 최저학력기준이란?")
        st.write("""
        - 대학이 요구하는 **수능 성적의 최소 기준**입니다.
        - 예: "국어, 수학, 영어 중 2과목 등급 합 4 이내"
        - **기준을 충족하지 못하면** 서류와 면접이 아무리 좋아도 불합격 처리됩니다.
        """)

        st.subheader("🎯 수시 지원 전략 팁")
        st.markdown("""
        - 📚 **내신이 우수한 학생** → 교과 전형 중심으로 준비  
        - 🧠 **전공 활동이나 비교과가 강한 학생** → 종합 전형 공략  
        - 🧾 **자기소개서 준비는 미리** (작성 시기와 첨삭 중요)  
        - 🧪 **면접 준비는 대학별 기출 확인 필수**  
        - 🎯 **최저가 높은 대학은 수능 대비 병행 필요**  
        - 🔄 **6회 지원 기회를 전략적으로 분산** (교과+종합 조합 추천)  
        """)

    elif selected_type == "📌 정시 전형":
        st.header("📌 정시 전형이란?")
        st.write("""
        정시 전형은 **수능 이후에 실시되는 전형**으로, 대부분의 대학이 수능 성적을 가장 주요하게 반영합니다.
        """)

        st.subheader("✅ 정시 전형의 특징")
        st.markdown("""
        - 📊 **수능 100% or 수능+학생부 소폭 반영**  
        - 📆 **12~1월 중 모집**, 수능 성적 확인 후 지원 가능  
        - 🎭 **실기 반영**: 예체능 계열은 실기고사 포함  
        - 🧭 **모집군 분할**: 가군, 나군, 다군 중 각각 1개씩 지원 가능  
        """)

        st.subheader("🎯 정시 지원 전략 팁")
        st.markdown("""
        - 🧠 **정확한 백분위/표준점수 확인** → 대학별 반영 방법 차이 분석  
        - 📊 **과목별 가산점/가중치 반영 대학 확인**  
        - 🎯 **군별 분산 지원 전략** (안정/적정/소신 조합)  
        - 📝 **모의지원 활용**: 진학사, 유웨이 등 사설사이트 모의지원 활용 추천  
        - 🧾 **전년도 입결 참고**: 단순 점수보다 모집단위별 유불리 확인  
        """)
        st.info("💡 수능이 강한 학생은 정시를 중심 전략으로 세우는 것이 효과적입니다.")

# -------------------- 요약표 --------------------
elif menu == "📊 대학별 수시/정시 요약표":
    st.title("📊 대학별 수시/정시 전형 요약표")
    st.markdown("수도권 주요 대학 및 지역거점국립대의 **수시/정시 비율, 전형 종류, 최저학력 기준** 정보를 요약합니다.")
    st.dataframe(df)

    st.warning("📌 위 표는 참고용 정보입니다. 반드시 각 대학의 **입학처 홈페이지 또는 최신 입시요강**을 통해 정확한 내용을 확인하세요.")

# -------------------- 맞춤형 분석 --------------------
elif menu == "🎯 맞춤형 지원 가능성 분석":
    st.header("🎯 성적 기반 지원 가능성 분석")

    st.markdown("#### ✍️ 성적을 입력하세요")
    st.warning("📌 이 정보는 참고용입니다. 반드시 각 담임 선생님과의 상담을 통해 정확한 내용을 확인하세요.")
    admission_type = st.radio("전형 선택", ["수시", "정시"])

    if admission_type == "수시":
        avg_grade = st.slider("평균 내신 등급", 1.0, 9.0, 3.0, 0.1)
        st.write(f"🧾 입력된 내신: {avg_grade:.1f}등급")

        if avg_grade <= 2.5:
            st.success("👍 중상위권 대학의 교과/종합 전형 도전 가능!")
            st.markdown("- 고려대 학업우수형\n- 중앙대 학생부교과\n- 이화여대 고교추천형 등")
        elif avg_grade <= 3.5:
            st.warning("⚠️ 일부 종합전형 위주 지원 권장 (내신 경쟁 있음)")
            st.markdown("- 국민대, 숙명여대, 아주대 등의 종합 전형")
        else:
            st.info("📌 최저학력 없는 종합전형 또는 전문대학 지원 고려")
            st.markdown("- 수능최저 없는 대학 위주 지원 필요")

    elif admission_type == "정시":
        score = st.slider("수능 백분위 평균", 50, 100, 75)
        st.write(f"📊 수능 백분위 평균: {score}%")
    

        if score >= 95:
            st.success("🔥 상위권 대학 정시 충분히 도전 가능!")
            st.markdown("- 서울대, 연세대, 고려대 등")
        elif score >= 85:
            st.warning("⚡ 중위권~상위권 대학 적극 도전")
            st.markdown("- 중앙대, 경희대, 이화여대 등")
        else:
            st.info("📌 수도권/지방국립대 위주 전략 필요")
            st.markdown("- 인하대, 세종대, 충북대 등")
