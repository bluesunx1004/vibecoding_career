import streamlit as st
import pandas as pd
import random

# ----------------------------------------------------------------------------
# 1. 직업 데이터 정의 (유망·인기 직업 30가지)
# ----------------------------------------------------------------------------
JOB_DEFS = [
    ("AI 엔지니어", ["컴퓨터공학", "AI융합학과"]),
    ("데이터 사이언티스트", ["통계학", "데이터사이언스"]),
    ("UX 디자이너", ["디자인학", "HCI"]),
    ("소프트웨어 엔지니어", ["컴퓨터공학", "소프트웨어공학"]),
    ("클라우드 엔지니어", ["컴퓨터공학", "클라우드컴퓨팅"]),
    ("사이버 보안 전문가", ["정보보호학", "컴퓨터공학"]),
    ("로봇공학 엔지니어", ["로봇공학", "메카트로닉스"]),
    ("바이오인포매틱스 연구원", ["생명공학", "바이오인포매틱스"]),
    ("환경공학자", ["환경공학", "토목공학"]),
    ("금융 분석가", ["경영학", "금융공학"]),
    ("디지털 마케팅 전문가", ["경영학", "광고홍보학"]),
    ("블록체인 개발자", ["컴퓨터공학", "블록체인학과"]),
    ("제품 관리자", ["산업공학", "경영학"]),
    ("의료 데이터 분석가", ["의공학", "데이터사이언스"]),
    ("IT 컨설턴트", ["경영정보학", "컴퓨터공학"]),
    ("VR/AR 개발자", ["컴퓨터공학", "게임공학"]),
    ("게임 개발자", ["게임공학", "컴퓨터공학"]),
    ("SAP 컨설턴트", ["산업공학", "경영정보학"]),
    ("모바일 앱 개발자", ["컴퓨터공학", "소프트웨어융합학과"]),
    ("네트워크 엔지니어", ["전자공학", "통신공학"]),
    ("머신러닝 엔지니어", ["컴퓨터공학", "AI융합학과"]),
    ("전기자동차 엔지니어", ["기계공학", "전기공학"]),
    ("드론 조종사", ["항공우주공학", "무인기공학"]),
    ("우주항공 엔지니어", ["항공우주공학", "기계공학"]),
    ("그린 에너지 연구원", ["신재생에너지공학", "환경공학"]),
    ("스마트 팩토리 엔지니어", ["산업공학", "메카트로닉스"]),
    ("증강 현실 연구원", ["컴퓨터공학", "디자인학"]),
    ("스마트 시티 기획자", ["도시공학", "산업공학"]),
    ("헬스케어 IT 전문가", ["의공학", "정보보호학"]),
    ("IoT 개발자", ["컴퓨터공학", "전기공학"]),
]

MBTI_ALL = ['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP',
            'ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ']
CURRICULUM = {
    "1학년": ["기초수학", "기초프로그래밍"],
    "2학년": ["자료구조", "선형대수"],
    "3학년": ["전공심화", "캡스톤프로젝트"],
    "4학년": ["인턴십", "졸업논문"],
}
HS_SUBJECTS = ["수학", "영어", "과학"]

# Build DataFrame
def load_job_data() -> pd.DataFrame:
    jobs = []
    for idx, (name, majors) in enumerate(JOB_DEFS, start=1):
        jobs.append({
            "job_id": idx,
            "job_name": name,
            "image_url": "https://via.placeholder.com/150",
            "mbti_types": MBTI_ALL,
            "description": f"{name} 직업 설명입니다.",
            "related_majors": majors,
            "university_curriculum": CURRICULUM,
            "required_highschool_subjects": HS_SUBJECTS,
        })
    return pd.DataFrame(jobs)

# ----------------------------------------------------------------------------
# 토너먼트 대진표 생성
# ----------------------------------------------------------------------------
def make_bracket(jobs: list) -> list:
    random.shuffle(jobs)
    return [(jobs[i], jobs[i+1]) for i in range(0, len(jobs), 2)]

# ----------------------------------------------------------------------------
# 메인 앱
# ----------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="직업 월드컵", layout="wide")
    st.title("🎉 직업 월드컵")

    # MBTI 선택
    mbti = st.sidebar.selectbox("내 MBTI를 선택하세요", MBTI_ALL)

    # 데이터 로드
    df = load_job_data()

    # MBTI 필터 후 16개 추출
    filtered = df[df['mbti_types'].apply(lambda mbtis: mbti in mbtis)]
    candidates = filtered.sample(16) if len(filtered) >= 16 else df.sample(16)

    # 세션 초기화
    if 'matches' not in st.session_state:
        st.session_state.matches = make_bracket(candidates['job_id'].tolist())
        st.session_state.round = 0

    rounds = ['16강', '8강', '4강', '결승']
    st.header(f"현재 단계: {rounds[st.session_state.round]}")

    next_winners = []
    for idx, (a, b) in enumerate(st.session_state.matches):
        col1, col2 = st.columns(2)
        job_a = df[df.job_id == a].iloc[0]
        job_b = df[df.job_id == b].iloc[0]
        with col1:
            st.image(job_a.image_url, caption=job_a.job_name)
            if st.button(f"{job_a.job_name} 승리", key=f"a{idx}"):
                next_winners.append(a)
        with col2:
            st.image(job_b.image_url, caption=job_b.job_name)
            if st.button(f"{job_b.job_name} 승리", key=f"b{idx}"):
                next_winners.append(b)
        st.markdown("---")

    if len(next_winners) == len(st.session_state.matches):
        st.session_state.matches = [(next_winners[i], next_winners[i+1]) for i in range(0, len(next_winners), 2)]
        st.session_state.round += 1
        if st.session_state.round >= len(rounds):
            show_job_detail(df, next_winners[0])
        else:
            st.experimental_rerun()

# ----------------------------------------------------------------------------
# 결과 상세 정보
# ----------------------------------------------------------------------------
def show_job_detail(df: pd.DataFrame, job_id: int):
    st.header("🏆 최종 선택된 직업 분석")
    job = df[df.job_id == job_id].iloc[0]

    st.subheader(f"직업: {job.job_name}")
    st.write(job.description)

    st.subheader("관련 학과")
    for major in job.related_majors:
        st.write(f"- {major}")

    st.subheader("대학 교육과정 예시")
    for year, courses in job.university_curriculum.items():
        st.write(f"**{year}**")
        for course in courses:
            st.write(f" - {course}")

    st.subheader("필수 고등학교 과목")
    for subj in job.required_highschool_subjects:
        st.write(f"- {subj}")

# ----------------------------------------------------------------------------
# 실행
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
