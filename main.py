import streamlit as st
import io

# 16가지 MBTI 유형을 포함하는 진로 데이터
mbti_data = {
    mbti: {
        "famous": f"유명인 {mbti}형",
        "jobs": [
            {
                "name": "직업 A",
                "major": "전공 A",
                "description": "이 직업은 MBTI 유형에 잘 맞는 특성을 반영합니다.",
                "roadmap": [
                    "고등학교: 관련 과목 학습",
                    "대학교: 전공 심화 수강",
                    "활동: 동아리, 인턴 참여"
                ]
            },
            {
                "name": "직업 B",
                "major": "전공 B",
                "description": "이 직업은 창의력과 문제 해결력을 요구합니다.",
                "roadmap": [
                    "고등학교: 프로젝트 기반 학습",
                    "대학교: 연구 활동 참여",
                    "활동: 포트폴리오 제작"
                ]
            },
            {
                "name": "직업 C",
                "major": "전공 C",
                "description": "이 직업은 대인 관계 능력과 커뮤니케이션이 중요합니다.",
                "roadmap": [
                    "고등학교: 발표 및 토론 활동",
                    "대학교: 현장실습 포함 전공 선택",
                    "활동: 멘토링, 대외활동 참여"
                ]
            }
        ]
    } for mbti in [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
}

# Streamlit 앱 구성
st.title("🎯 MBTI 기반 진로 탐색 앱")

# MBTI 선택
mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", sorted(mbti_data.keys()))

if mbti_type:
    selected = mbti_data[mbti_type]
    st.subheader(f"✅ {mbti_type} 유형 추천 직업")
    st.markdown(f"📌 유명한 {mbti_type} 유형 인물: **{selected['famous']}**")

    result_text = f"[MBTI 유형: {mbti_type}]\n추천 직업:\n"

    for job_info in selected["jobs"]:
        name = job_info["name"]
        major = job_info["major"]
        with st.expander(f"🔍 {name} (관련 학과: {major})"):
            st.markdown(f"**직업 설명**: {job_info['description']}")
            st.markdown("**진학 로드맵:**")
            for step in job_info["roadmap"]:
                st.write(f"• {step}")
        result_text += f"- {name} (관련 학과: {major})\n  설명: {job_info['description']}\n"
        result_text += "  진학 로드맵:\n"
        for step in job_info["roadmap"]:
            result_text += f"    - {step}\n"
        result_text += "\n"

    # 결과 텍스트 저장 및 다운로드
    txt_file = io.StringIO(result_text)
    st.download_button(
        label="📥 추천 결과 TXT 다운로드",
        data=txt_file.getvalue(),
        file_name=f"{mbti_type}_진로추천_상세정보.txt",
        mime="text/plain"
    )
