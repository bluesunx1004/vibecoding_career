
import streamlit as st
import io
import json

mbti_data = {
  "INTJ": {
    "famous": "일론 머스크 (추정)",
    "jobs": [
      {
        "name": "데이터 과학자",
        "major": "통계학, 컴퓨터공학",
        "description": "데이터를 수집·분석하고 패턴을 발견해 의사결정을 지원하는 전문가입니다.",
        "roadmap": [
          "고등학교: 수학, 과학 집중, Python 등 코딩 시작",
          "대학교: 통계학, 컴퓨터공학 전공 → 인공지능, 데이터마이닝 수강",
          "활동: Kaggle 대회 참여, 데이터 분석 인턴십"
        ]
      },
      {
        "name": "전략 컨설턴트",
        "major": "경영학, 경제학",
        "description": "기업의 경영 문제를 진단하고 해결 방안을 제시하는 전문가입니다.",
        "roadmap": [
          "고등학교: 시사 토론, 논술 능력 향상",
          "대학교: 경영학 또는 경제학 전공 + 케이스 스터디 활동",
          "활동: 기업 인턴, 컨설팅 공모전 참가"
        ]
      },
      {
        "name": "시스템 엔지니어",
        "major": "산업공학, 소프트웨어공학",
        "description": "복잡한 시스템을 설계하고 최적화하여 효율성을 높이는 직업입니다.",
        "roadmap": [
          "고등학교: 수학, 과학, 정보과목 중심",
          "대학교: 시스템 분석/설계, 프로그래밍 수강",
          "활동: 프로젝트 실습, 시스템 설계 인턴"
        ]
      }
    ]
  },
  "ENFP": {
    "famous": "로버트 다우니 주니어 (추정)",
    "jobs": [
      {
        "name": "광고 기획자",
        "major": "광고홍보학, 미디어커뮤니케이션학",
        "description": "소비자의 관심을 끌 수 있는 광고를 기획·전략적으로 설계하는 전문가입니다.",
        "roadmap": [
          "고등학교: 미술, 사회탐구, 글쓰기 활동",
          "대학교: 광고홍보학 전공 후 포트폴리오 제작",
          "활동: 광고 공모전, 브랜드 캠페인 참여"
        ]
      },
      {
        "name": "심리상담사",
        "major": "심리학, 아동가족학",
        "description": "개인의 심리적 문제를 진단하고 상담을 통해 치유를 돕는 전문가입니다.",
        "roadmap": [
          "고등학교: 생윤, 사회문화 중심 수강",
          "대학교: 심리학과 진학 후 상담 실습과목 이수",
          "활동: 자원봉사, 또래 상담 동아리 활동"
        ]
      },
      {
        "name": "콘텐츠 크리에이터",
        "major": "디지털미디어학, 영상학",
        "description": "온라인 플랫폼에서 영상·이미지·텍스트 콘텐츠를 제작하고 운영하는 창작자입니다.",
        "roadmap": [
          "고등학교: 영상 편집, 발표력 강화",
          "대학교: 콘텐츠 제작 관련 전공 및 실습 수강",
          "활동: 유튜브 채널 운영, 콘텐츠 공모전 참여"
        ]
      }
    ]
  },
  "INFJ": {
    "famous": "마틴 루터 킹 주니어 (추정)",
    "jobs": [
      {
        "name": "상담심리사",
        "major": "심리학, 상담학",
        "description": "내담자의 문제를 진단하고 심리적 안정과 성장을 돕는 전문가입니다.",
        "roadmap": [
          "고등학교: 사회문화, 생윤 등 인문계열 과목 중심",
          "대학교: 심리학 전공 → 상담심리 자격 과정 이수",
          "활동: 상담 관련 봉사활동, 사례 연구 세미나 참가"
        ]
      },
      {
        "name": "고등학교 교사",
        "major": "교육학, 전공과목 교육과",
        "description": "청소년의 지적·정서적 성장을 도와주는 교육 전문가입니다.",
        "roadmap": [
          "고등학교: 전공 희망 교과 심화 학습",
          "대학교: 교육과정 + 교직 이수 → 교사 자격증 취득",
          "활동: 멘토링, 교육봉사, 교육 실습 참여"
        ]
      },
      {
        "name": "비영리단체 활동가",
        "major": "사회복지학, 국제개발학",
        "description": "사회적 약자를 지원하고 공동체를 위한 프로젝트를 수행하는 활동가입니다.",
        "roadmap": [
          "고등학교: 사회문제 탐구 및 모의 유엔 활동",
          "대학교: 국제개발/사회복지학 전공 및 현장 실습",
          "활동: NGO 인턴, 공공기관 봉사활동"
        ]
      }
    ]
  },
  "ISTJ": {
    "famous": "나탈리 포트만 (추정)",
    "jobs": [
      {
        "name": "회계사",
        "major": "회계학, 경영학",
        "description": "기업의 재무 상태를 관리하고 세무보고를 수행하는 재무 전문가입니다.",
        "roadmap": [
          "고등학교: 수학, 경제 과목 중심 학습",
          "대학교: 회계학 전공 → CPA 자격 준비",
          "활동: 재무 동아리, 모의 기업 경영 대회"
        ]
      },
      {
        "name": "공무원",
        "major": "행정학, 정치외교학",
        "description": "국가 및 지방 행정을 수행하고 정책 집행에 참여하는 직업입니다.",
        "roadmap": [
          "고등학교: 한국사, 사회 교과 집중",
          "대학교: 행정학과 전공 + 공무원 시험 대비",
          "활동: 시사탐구 토론, 공공기관 인턴"
        ]
      },
      {
        "name": "군무원",
        "major": "전산학, 기계공학 등 이공계열",
        "description": "국방 업무를 지원하는 민간 군무 전문가입니다.",
        "roadmap": [
          "고등학교: 이과 계열 수학·과학 집중",
          "대학교: 전산, 기계 등 군무직렬 전공",
          "활동: 국방부 연계 교육 프로그램 참여"
        ]
      }
    ]
  }
}

st.title("🎯 MBTI 기반 진로 탐색 앱")

mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", sorted(mbti_data.keys()))

if mbti_type:
    selected = mbti_data[mbti_type]
    st.subheader(f"✅ {mbti_type} 유형 추천 직업")
    st.markdown(f"📌 유명한 {mbti_type} 유형 인물: **{selected['famous']}**")

    result_text = f"[MBTI 유형: {mbti_type}]\n추천 직업:\n"

    for job in selected["jobs"]:
        with st.expander(f"🔍 {job['name']} (관련 학과: {job['major']})"):
            st.markdown(f"**직업 설명**: {job['description']}")
            st.markdown("**🗺️ 진학 로드맵:**")
            for step in job["roadmap"]:
                st.write(f"• {step}")

        result_text += f"\n🔹 {job['name']} (관련 학과: {job['major']})\n"
        result_text += f"설명: {job['description']}\n"
        result_text += "진학 로드맵:\n" + "\n".join(f"- {step}" for step in job["roadmap"]) + "\n"

    txt_file = io.StringIO(result_text)
    st.download_button(
        label="📥 추천 결과 TXT 다운로드",
        data=txt_file.getvalue(),
        file_name=f"{mbti_type}_진로추천_상세정보.txt",
        mime="text/plain"
    )
