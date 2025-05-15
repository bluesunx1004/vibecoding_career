import streamlit as st
import io

# MBTI별 추천 직업 + 상세 진로 정보
mbti_data = {
    "INTJ": {
        "famous": "일론 머스크 (추정)",
        "jobs": [
            {
                "name": "데이터 과학자",
                "major": "통계학, 컴퓨터공학",
                "description": "데이터를 기반으로 문제를 분석하고 해결책을 제시하는 전문가. AI 시대의 핵심 직업 중 하나입니다.",
                "roadmap": [
                    "고등학교: 수학, 과학 집중, Python 등 기초 코딩",
                    "대학교: 통계학/컴퓨터공학 전공 → 데이터 분석 및 머신러닝 과목 수강",
                    "진로 활동: Kaggle 대회, 인턴십, 데이터 분석 동아리 활동"
                ]
            },
            {
                "name": "전략 컨설턴트",
                "major": "경영학, 경제학",
                "description": "기업의 문제를 진단하고 전략적으로 해결 방안을 제시하는 전문가입니다.",
                "roadmap": [
                    "고등학교: 논리력 강화, 시사토론 활동 참여",
                    "대학교: 경영학 또는 경제학 전공, 케이스 스터디 및 컨설팅 학회 활동",
                    "진로 활동: 기업 인턴, 컨설팅 공모전 참여"
                ]
            },
            {
                "name": "시스템 설계자",
                "major": "소프트웨어공학, 산업공학",
                "description": "복잡한 시스템의 구조를 설계하고 효율화를 이끄는 직업입니다.",
                "roadmap": [
                    "고등학교: 정보, 수학 교과 집중",
                    "대학교: 시스템 공학, 소프트웨어 설계 전공 수강",
                    "진로 활동: 프로젝트 기반 학습, 공정 분석 관련 활동"
                ]
            }
        ]
    },
    # 예시로 ENFP만 더 추가합니다. (나머지는 동일 방식으로 확장 가능)
    "ENFP": {
        "famous": "로버트 다우니 주니어 (추정)",
        "jobs": [
            {
                "name": "광고 기획자",
                "major": "광고홍보학, 디자인학",
                "description": "사람의 감성을 자극하는 광고를 기획하고 실행하는 크리에이티브 전문가입니다.",
                "roadmap": [
                    "고등학교: 미술, 국어, 사회 계열 관심",
                    "대학교: 광고홍보학 전공 + 포트폴리오 제작",
                    "진로 활동: 광고 공모전, SNS 콘텐츠 제작"
                ]
            },
            {
                "name": "심리상담사",
                "major": "심리학, 아동가족학",
                "description": "타인의 감정을 이해하고 문제를 상담으로 치유하는 직업입니다.",
                "roadmap": [
                    "고등학교: 생윤, 사회문화 등 인문 교과 집중",
                    "대학교: 심리학과 진학 후 상담 심화 과목 이수",
                    "진로 활동: 멘토링 활동, 자원봉사 경험 쌓기"
                ]
            },
            {
                "name": "콘텐츠 크리에이터",
                "major": "미디어학, 영상학",
                "description": "자신만의 콘텐츠를 제작하고 플랫폼을 통해 대중과 소통하는 직업입니다.",
                "roadmap": [
                    "고등학교: 영상 편집, 글쓰기, 발표력 향상",
                    "대학교: 미디어/영상 관련 전공 및 포트폴리오 제작",
                    "진로 활동: 유튜브 채널 운영, 영상제 출품"
                ]
            }
        ]
    }
}

# UI 시작
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
