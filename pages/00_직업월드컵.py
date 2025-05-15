import streamlit as st
import pandas as pd
import random

# ----------------------------------------------------------------------------
# 1. 데이터 로드 함수
# ----------------------------------------------------------------------------
def load_job_data(path="jobs.csv") -> pd.DataFrame:
    """
    jobs.csv 예시 컬럼:
      - job_id
      - job_name
      - image_url
      - mbti_types (예: 'INTJ,ENTP')
      - description
      - related_majors (예: 'Computer Science;AI Engineering')
      - university_curriculum (JSON 형식 문자열)
      - required_highschool_subjects (예: 'Math;Physics;English')
    """
    df = pd.read_csv(path)
    # university_curriculum 컬럼을 딕셔너리로 변환
    df['university_curriculum'] = df['university_curriculum'].apply(pd.eval)
    df['related_majors'] = df['related_majors'].str.split(';')
    df['required_highschool_subjects'] = df['required_highschool_subjects'].str.split(';')
    df['mbti_types'] = df['mbti_types'].str.split(',')
    return df

# ----------------------------------------------------------------------------
# 2. 경기 매치업 생성
# ----------------------------------------------------------------------------
def make_bracket(jobs: list) -> list:
    """16개의 직업을 랜덤 혹은 MBTI 필터 후 토너먼트 대진표로 변환"""
    random.shuffle(jobs)
    # 8경기씩 16강
    matches = [(jobs[i], jobs[i+1]) for i in range(0, len(jobs), 2)]
    return matches

# ----------------------------------------------------------------------------
# 3. 메인 앱
# ----------------------------------------------------------------------------
def main():
    st.set_page_config(page_title="직업 월드컵", layout="wide")
    st.title("🎉 직업 월드컵")

    # 유저 MBTI 선택
    mbti = st.sidebar.selectbox("내 MBTI를 선택하세요", [
        'ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP',
        'ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ'
    ])

    # 데이터 불러오기
    df = load_job_data()
    # MBTI 필터
    filtered = df[df['mbti_types'].apply(lambda mbtis: mbti in mbtis)]
    # 16개로 추출
    if len(filtered) >= 16:
        candidates = filtered.sample(16)
    else:
        candidates = df.sample(16)

    # 대진표 생성
    if 'matches' not in st.session_state:
        st.session_state.matches = make_bracket(candidates['job_id'].tolist())
        st.session_state.winners = []
        st.session_state.round = 0

    # 토너먼트 진행
    rounds = ['16강', '8강', '4강', '결승']
    current_round = rounds[st.session_state.round]
    st.header(f"현재 단계: {current_round}")

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
        # 승자를 다음 라운드로 세션 스테이트에 저장
        st.session_state.matches = [(next_winners[i], next_winners[i+1]) 
                                     for i in range(0, len(next_winners), 2)]
        st.session_state.round += 1
        # 4강 이후엔 matches 크기를 줄임
        if st.session_state.round >= len(rounds):
            # 최종 우승자
            champion_id = next_winners[0]
            show_job_detail(df, champion_id)
        st.experimental_rerun()

# ----------------------------------------------------------------------------
# 4. 상세 정보 표시
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
    curriculum: dict = job.university_curriculum
    for year, courses in curriculum.items():
        st.write(f"**{year}학년**")
        for course in courses:
            st.write(f" - {course}")

    st.subheader("필수 고등학교 과목")
    for subj in job.required_highschool_subjects:
        st.write(f"- {subj}")

# ----------------------------------------------------------------------------
# 앱 실행
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
