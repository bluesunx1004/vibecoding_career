import streamlit as st
import random

# 예시 직업 리스트 (8개)
career_data = {
    "데이터 과학자": {
        "description": "빅데이터를 분석하고 인공지능 모델을 설계하는 전문가.",
        "major": "통계학, 컴퓨터공학",
        "roadmap": [
            "고등학교: 수학, 과학, Python 기초",
            "대학교: 통계학/컴공 전공, 머신러닝 수강",
            "활동: 데이터 분석 대회, 인턴 경험"
        ]
    },
    "광고 기획자": {
        "description": "광고 전략을 기획하고 소비자와 소통하는 콘텐츠를 만드는 직업.",
        "major": "광고홍보학, 미디어커뮤니케이션학",
        "roadmap": [
            "고등학교: 글쓰기, 디자인, 사회 과목",
            "대학교: 미디어 전공 + 포트폴리오",
            "활동: 광고 공모전, 캠페인 기획"
        ]
    },
    "심리상담사": {
        "description": "심리적 문제를 가진 사람들을 상담하고 치유를 돕는 전문가.",
        "major": "심리학, 상담학",
        "roadmap": [
            "고등학교: 생윤, 사회문화 중심",
            "대학교: 심리학 전공 + 상담실습",
            "활동: 또래상담, 상담봉사"
        ]
    },
    "교사": {
        "description": "학생들에게 지식과 가치를 전달하는 교육 전문가.",
        "major": "교육학, 각 교과교육과",
        "roadmap": [
            "고등학교: 국어, 수학, 사회 등 희망 과목",
            "대학교: 교직 이수 → 임용시험 준비",
            "활동: 교육봉사, 멘토링"
        ]
    },
    "간호사": {
        "description": "환자를 돌보고 치료를 보조하는 의료 전문가.",
        "major": "간호학",
        "roadmap": [
            "고등학교: 생명과학, 화학, CPR 실습",
            "대학교: 간호학과 → 국가고시",
            "활동: 병원 실습, 보건소 봉사"
        ]
    },
    "콘텐츠 크리에이터": {
        "description": "영상, 이미지, 글 등을 제작해 온라인에 게시하는 창작자.",
        "major": "미디어학, 영상학",
        "roadmap": [
            "고등학교: 영상편집, 발표력 향상",
            "대학교: 영상 전공 + 포트폴리오",
            "활동: 유튜브 채널, 콘텐츠 대회"
        ]
    },
    "변호사": {
        "description": "법률 자문 및 소송을 담당하는 법률 전문가.",
        "major": "법학, 로스쿨",
        "roadmap": [
            "고등학교: 사회, 논술, 시사탐구",
            "대학교: 법학과 → 로스쿨 진학",
            "활동: 모의재판, 로펌 인턴"
        ]
    },
    "게임 개발자": {
        "description": "게임을 기획·디자인하고 프로그래밍하는 창의적 기술자.",
        "major": "컴퓨터공학, 게임공학",
        "roadmap": [
            "고등학교: 정보과목, C언어, 수학",
            "대학교: 게임전공, 팀 프로젝트 중심",
            "활동: 게임잼, 앱 개발"
        ]
    }
}

# 초기 셋업
if "round" not in st.session_state:
    st.session_state.round = 8
    st.session_state.candidates = random.sample(list(career_data.keys()), 8)
    st.session_state.next_round = []
    st.session_state.winner = None

st.title("🏆 직업 월드컵")

# 월드컵 로직
if st.session_state.round >= 2:
    st.header(f"{st.session_state.round}강")

    cols = st.columns(2)
    for i in range(0, len(st.session_state.candidates), 2):
        left = st.session_state.candidates[i]
        right = st.session_state.candidates[i + 1]

        with cols[0]:
            if st.button(left, key=f"{left}_{st.session_state.round}"):
                st.session_state.next_round.append(left)

        with cols[1]:
            if st.button(right, key=f"{right}_{st.session_state.round}"):
                st.session_state.next_round.append(right)

        # 한 페어만 표시 후 종료
        break

    # 다음 라운드 조건 확인
    if len(st.session_state.next_round) == st.session_state.round // 2:
        st.session_state.candidates = st.session_state.next_round
        st.session_state.next_round = []
        st.session_state.round //= 2

# 우승자 발표
elif st.session_state.round == 1 and len(st.session_state.candidates) == 1:
    st.session_state.winner = st.session_state.candidates[0]
    st.header("🏅 최종 우승 직업!")

    winner = st.session_state.winner
    info = career_data[winner]

    st.subheader(f"🎓 {winner}")
    st.markdown(f"**직업 설명**: {info['description']}")
    st.markdown(f"**관련 전공**: {info['major']}")
    st.markdown("**진학 로드맵:**")
    for step in info["roadmap"]:
        st.write(f"• {step}")

    if st.button("🔁 다시 시작하기"):
        for key in ["round", "candidates", "next_round", "winner"]:
            st.session_state.pop(key)
        st.experimental_rerun()
