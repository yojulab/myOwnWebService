import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="2025 핀테크 산업 리서치 보고서",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 기본 스타일 설정
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #1E3A8A;
    }
    .subsection-header {
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        color: #2563EB;
    }
    .caption {
        font-size: 0.8rem;
        font-style: italic;
        color: #6B7280;
    }
    .highlight {
        background-color: #FEF3C7;
        padding: 0.2rem;
        border-radius: 0.2rem;
    }
    .insight-box {
        background-color: #E0F2FE;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .table-wrapper {
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 샘플 데이터 생성
# 시장 규모 데이터
market_data = pd.DataFrame({
    'Year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027],
    'Market_Size': [550, 720, 950, 1200, 1450, 1550, 1850, 2200],
    'Growth_Rate': [24.3, 30.9, 31.9, 26.3, 29.2, 30.1, 19.4, 18.9]
})

# 핀테크 발전 타임라인
timeline_data = pd.DataFrame({
    'Year': [1998, 2005, 2009, 2015, 2020, 2024],
    'Event': ['페이팔 전신 설립', '모바일결제 등장', '비트코인 출현', '한국 규제완화', '코로나19 디지털 가속화', 'CBDC 도입'],
    'Impact': [20, 35, 40, 60, 85, 95],
    'Description': [
        '컨피니티(Confinity) 설립, 이후 페이팔로 발전',
        '모바일결제 시스템 등장 및 확산',
        '비트코인 백서 발표 및 블록체인 기술 부상',
        '한국 정부 IT-금융 융합 지원방안 발표',
        '코로나19로 비대면 금융서비스 급성장',
        '주요국 중앙은행 디지털화폐(CBDC) 도입'
    ]
})

# 기업 비교 데이터
company_data = pd.DataFrame({
    'company': ['카카오페이', '네이버파이낸셜', '토스'],
    'MAU': [3200, 2100, 1800],
    'transactions': [78, 54, 42],
    'partners': [150, 90, 75]
})

# 기술 도입 데이터
tech_data = pd.DataFrame({
    '기술': ['AI 신용평가', '블록체인', '생체인증', '양자암호', '데이터 분석'],
    '도입률(%)': [78, 65, 82, 35, 90],
    '예상성장률(%)': [45, 55, 30, 120, 25]
})

# 위험 요소 데이터
risk_data = pd.DataFrame({
    '위험요소': ['사이버보안 위협', '규제 불확실성', '기술 의존도', '고객신뢰 하락', '시장 포화'],
    '위험도(1-10)': [8.5, 7.2, 6.8, 5.9, 6.3],
    '증가율(%)': [230, 110, 85, 45, 70]
})

# 사이드바 메뉴
st.sidebar.title("2025 핀테크 산업 리서치")
menu = st.sidebar.radio("목차", [
    "1. 서론: 핀테크 발전사",
    "2. 시장 현황 및 트렌드",
    "3. 주요 기업 분석",
    "4. 기술 혁신과 규제 환경",
    "5. 향후 전망 및 리스크",
    "6. 결론 및 참고문헌"
])

# 사이드바에 정보 추가
st.sidebar.divider()
st.sidebar.info("""
**2025년 3월 기준 데이터**
- 글로벌 핀테크 시장: 1,550조 원
- 연간 성장률: 30.1%
- 주요 기업: 카카오페이, 네이버파이낸셜, 토스
""")

st.sidebar.caption("출처: 금융감독원, IDC 글로벌 핀테크 보고서")

# 1. 서론: 핀테크 발전사
if menu == "1. 서론: 핀테크 발전사":
    st.markdown('<p class="main-header">1. 서론: 디지털 금융 생태계의 재편</p>', unsafe_allow_html=True)
    
    # 핀테크 정의 및 역사
    st.markdown('<p class="subsection-header">1.1 핀테크의 정의와 역사적 발전</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        **핀테크(FinTech)**는 금융(Finance)과 기술(Technology)의 합성어로, 정보기술(IT)을 기반으로 한 새로운 형태의 금융 서비스와 산업을 의미합니다. 
        
        1990년대 후반 인터넷의 확산과 함께 시작된 온라인 뱅킹이 초기 핀테크의 모습이라면, 2008년 글로벌 금융위기 이후 금융 산업의 혁신 필요성과 
        스마트폰의 보급이 맞물려 현대적 의미의 핀테크가 본격적으로 성장하기 시작했습니다.
        
        핀테크의 발전은 크게 다음 단계로 구분할 수 있습니다:
        
        - **핀테크 1.0 (1998-2008)**: 인터넷 뱅킹, 온라인 결제 시스템 등장
        - **핀테크 2.0 (2009-2014)**: 모바일 뱅킹, P2P 대출, 비트코인 등장
        - **핀테크 3.0 (2015-2019)**: 간편결제, 로보어드바이저, 인슈어테크 성장
        - **핀테크 4.0 (2020-현재)**: AI 기반 초개인화, 임베디드 파이낸스, CBDC 도입
        
        특히 2020년 코로나19 팬데믹은 비대면 금융 서비스의 수요를 급증시키며 핀테크 산업의 질적·양적 성장을 가속화했습니다. 
        2025년 현재는 AI와 블록체인이 금융 산업의 근본적 변화를 이끌고 있습니다.
        """)

    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 핵심 인사이트
        
        - 2020-2025년 CAGR: **24.3%**
        - 2025년 핵심 기술: AI, 블록체인
        - 주요 성장 동력: 초개인화 금융서비스
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 핀테크 타임라인 시각화
    st.markdown("### 핀테크 주요 발전 단계")
    fig = px.bar(timeline_data, x='Year', y='Impact', 
                 color='Event', hover_data=['Description'],
                 labels={'Impact': '영향력 지수', 'Year': '연도'},
                 title="핀테크 산업 발전 타임라인 (1998-2025)")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: BCiF 리포트, 헥토데이터 핀테크 역사 분석")
    
    # 핀테크 생태계 구성
    st.markdown('<p class="subsection-header">1.2 핀테크 생태계 현황</p>', unsafe_allow_html=True)
    st.write("""
    2025년 현재 핀테크 생태계는 전통 금융기관과 신생 테크 기업, 그리고 빅테크 기업의 복합적인 경쟁과 협력 구도를 형성하고 있습니다.
    특히 주목할 만한 점은 **금융의 임베디드화(Embedded Finance)** 현상으로, 금융 서비스가 비금융 플랫폼 및 앱에 통합되어 
    제공되는 형태가 확산되고 있습니다.
    
    2022년부터 시작된 금리 상승기와 2023-2024년의 글로벌 경기 둔화에도 불구하고, 핀테크 산업은 꾸준히 성장해왔습니다.
    이는 디지털 전환이 선택이 아닌 필수가 된 환경에서 금융 서비스의 혁신이 지속적으로 요구되기 때문입니다.
    
    또한, '초연결 금융(Hyper-connected Finance)' 트렌드가 가속화되면서 다양한 금융 서비스가 API와 오픈뱅킹을 통해
    연결되고 있으며, 이는 소비자에게 통합된 금융 경험을 제공하는 핵심 요소가 되고 있습니다.
    """)

# 2. 시장 현황 및 트렌드
elif menu == "2. 시장 현황 및 트렌드":
    st.markdown('<p class="main-header">2. 시장 현황 및 트렌드 분석</p>', unsafe_allow_html=True)
    
    # 글로벌 시장 규모
    st.markdown('<p class="subsection-header">2.1 글로벌 시장 규모 및 성장 동력</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([6, 4])
    
    with col1:
        st.write("""
        핀테크 글로벌 시장은 2020년 550조 원에서 2025년 1,550조 원으로 폭발적인 성장을 기록했습니다.
        특히 코로나19 이후 비대면 서비스 수요 증가와 디지털 전환 가속화로 인해 연평균 24.3%라는 고성장세를 유지했습니다.
        
        지역별로는 북미와 아시아태평양 지역이 시장을 주도하고 있으며, 특히 인도와 동남아시아에서 급격한 성장세가 두드러집니다.
        이 지역들은 높은 모바일 보급률과 젊은 인구 구성, 그리고 상대적으로 낮은 기존 금융 인프라 보급률이 핀테크 서비스 채택의 
        가속화 요인이 되고 있습니다.
        
        세부 분야별로는 디지털 결제가 여전히 가장 큰 시장 점유율(43%)을 차지하고 있으나, 최근 들어 **임베디드 파이낸스(Embedded Finance)**와
        **디파이(DeFi)** 영역이 빠르게 성장하고 있습니다. 특히 디파이는 2024년부터 규제 프레임워크가 점차 명확해지면서
        기관 투자자들의 참여가 증가하는 추세입니다.
        """)
        
    with col2:
        # 시장 규모 표
        st.markdown('<div class="table-wrapper">', unsafe_allow_html=True)
        market_table = pd.DataFrame({
            '구분': ['시장 규모(조 원)', '성장률(%)'],
            '2023': [1200, 24.3],
            '2024': [1450, 29.2],
            '2025': [1550, 30.1]
        })
        st.table(market_table.set_index('구분'))
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("출처: IDC 글로벌 핀테크 전망 보고서 2025")
    
    # 시장 성장 추이 시각화
    st.markdown("### 핀테크 글로벌 시장 성장 추이 (2020-2027)")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=market_data['Year'],
        y=market_data['Market_Size'],
        name='시장 규모(조 원)',
        marker_color='rgb(55, 83, 109)'
    ))
    fig.add_trace(go.Scatter(
        x=market_data['Year'],
        y=market_data['Growth_Rate'],
        name='성장률(%)',
        mode='lines+markers',
        yaxis='y2',
        line=dict(color='rgb(220, 96, 96)', width=3),
        marker=dict(size=8)
    ))
    fig.update_layout(
        title='핀테크 글로벌 시장 규모 및 성장률 (2020-2027)',
        xaxis=dict(title='연도'),
        yaxis=dict(title='시장 규모(조 원)', side='left', showgrid=True),
        yaxis2=dict(title='성장률(%)', side='right', overlaying='y', showgrid=False),
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255, 255, 255, 0.5)'),
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: IDC 글로벌 핀테크 전망 2025, BCiF 리포트")
    
    # 핵심 트렌드
    st.markdown('<p class="subsection-header">2.2 2025 핵심 트렌드</p>', unsafe_allow_html=True)
    
    st.write("""
    2025년 핀테크 산업의 핵심 트렌드는 다음과 같습니다:
    
    1. **초개인화 금융(Hyper-personalized Finance)**
       - AI와 빅데이터를 활용한 고객별 맞춤형 금융 서비스 제공
       - 행동 패턴 분석을 통한 선제적 금융 솔루션 제안
       - 예: 소비 패턴 기반의 개인화된 보험 상품, 자산 포트폴리오 자동 조정
    
    2. **임베디드 파이낸스(Embedded Finance)**
       - 비금융 플랫폼에 금융 서비스 통합
       - 전자상거래, 모빌리티, 헬스케어 등 다양한 분야에 금융 기능 내재화
       - 예: 전자상거래 플랫폼 내 BNPL(Buy Now Pay Later) 서비스
    
    3. **중앙은행 디지털화폐(CBDC) 도입 확산**
       - 2024년 중국 디지털 위안화 전면 도입 이후 각국 중앙은행 참여 확대
       - 한국은행 2025년 하반기 파일럿 프로그램 확대 예정
       - 디지털화폐 기반 국가간 결제 시스템 표준화 논의 활발
    
    4. **금융 포용성 확대(Financial Inclusion)**
       - 전통 금융시스템에서 소외된 계층을 위한 서비스 강화
       - 신용 평가 다변화를 통한 금융 접근성 향상
       - 예: 한국의 '청년금융특별법' 시행으로 Z세대 특화 금융 상품 확대
    
    5. **그린 핀테크(Green FinTech)**
       - ESG 투자와 지속가능 금융의 디지털화
       - 탄소 배출량 추적 및 오프셋 기능 통합
       - 예: 지속가능한 소비에 보상을 제공하는 그린카드 서비스
    """)
    
    # 트렌드 시각화
    trends = ['초개인화 금융', '임베디드 파이낸스', 'CBDC', '금융 포용성', '그린 핀테크']
    impact = [95, 85, 80, 75, 70]
    maturity = [75, 80, 60, 65, 55]
    
    fig = px.scatter(
        x=maturity, y=impact, text=trends,
        size=[50]*5, color=trends,
        labels={'x': '시장 성숙도', 'y': '영향력'},
        title='2025년 핀테크 핵심 트렌드 맵',
        height=500
    )
    fig.update_traces(textposition='top center')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 삼정KPMG CES 2025 트렌드 보고서, 한국핀테크산업협회")

# 3. 주요 기업 분석
elif menu == "3. 주요 기업 분석":
    st.markdown('<p class="main-header">3. 주요 기업 및 기술 심층 분석</p>', unsafe_allow_html=True)
    
    # 국내 Top 3 플레이어 비교
    st.markdown('<p class="subsection-header">3.1 국내 Top 3 플레이어 비교</p>', unsafe_allow_html=True)
    
    st.write("""
    한국 핀테크 시장은 2021년 이후 빠른 성장을 보이며 2025년 현재 약 68조원 규모로 성장했습니다. 
    특히 3대 메이저 플레이어인 카카오페이, 네이버파이낸셜, 토스는 모바일 결제에서 시작해 종합 금융 플랫폼으로 
    사업영역을 확장하며 시장을 주도하고 있습니다.
    
    세 기업은 각자의 강점을 기반으로 차별화된 전략을 구사하며 경쟁하고 있습니다:
    
    - **카카오페이**: 3,200만 MAU를 보유한 카카오톡 기반의 강력한 사용자 락인(lock-in) 효과를 활용해 
      결제를 넘어 보험, 투자, 대출 등으로 서비스를 확장하고 있습니다. 특히 2024년 인수한 부동산 중개 
      플랫폼과의 시너지를 통해 부동산 금융 시장에 적극 진출했습니다.
    
    - **네이버파이낸셜**: 네이버의 검색-쇼핑-결제로 이어지는 통합 커머스 생태계를 바탕으로 스마트스토어 
      사업자 대상 사업자 금융에 강점을 보이고 있습니다. 2024년 출시한 SME(중소기업) 특화 금융 솔루션이 
      시장에서 좋은 반응을 얻고 있습니다.
    
    - **토스**: 가장 혁신적인 UX로 Z세대와 밀레니얼 세대의 높은 지지를 받고 있으며, 2023년 인터넷전문은행 
      라이센스 획득 이후 예금, 대출 등 뱅킹 서비스를 강화하고 있습니다. 특히 AI 기반 재무관리 서비스에 
      적극 투자하며 차별화를 시도하고 있습니다.
    """)
    
    # 기업 비교 차트
    st.markdown("### 국내 주요 핀테크 기업 비교 (2025년)")
    
    tab1, tab2 = st.tabs(["주요 지표 비교", "상세 분석"])
    
    with tab1:
        # MAU 비교 차트
        fig = px.bar(
            company_data,
            x='company',
            y='MAU',
            color='company',
            title='월간 활성 사용자 수 (MAU, 만 명)',
            labels={'company': '기업', 'MAU': 'MAU (만 명)'},
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # 거래액 및 제휴사 비교
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(
                company_data,
                x='company',
                y='transactions',
                color='company',
                title='연간 거래액 (조 원)',
                labels={'company': '기업', 'transactions': '거래액 (조 원)'},
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            fig = px.bar(
                company_data,
                x='company',
                y='partners',
                color='company',
                title='제휴사 수',
                labels={'company': '기업', 'partners': '제휴사 수'},
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.write("""
        ### 카카오페이 분석
        2025년 1분기 기준 카카오페이는 결제·금융 부문을 포함해 총 4천억원의 분기 매출을 달성했으며, 
        특히 보험 중개 사업의 성장이 두드러졌습니다. 미래 성장 동력으로는 2024년 말부터 시작한 
        '카카오페이 모기지' 서비스가 주목받고 있으며, 6개월 만에 5천억원의 대출 취급액을 달성했습니다.
        
        ### 네이버파이낸셜 분석
        네이버파이낸셜은 스마트스토어 사업자 대상 선정산, 대출 서비스를 중심으로 사업자 금융에 강점을 
        보이고 있습니다. 특히 네이버의 방대한 데이터를 활용한 대안신용평가시스템(ACSS)을 통해 
        기존 금융권에서 충분한 평가를 받지 못했던 소상공인들에게 금융 기회를 제공하고 있습니다.
        
        ### 토스 분석
        토스는 2023년 인터넷전문은행 라이센스 획득 후 예금 및 대출 상품을 확대하며 뱅킹 서비스를 
        강화하고 있습니다. 특히 2024년 출시한 '토스 AI 재무코치'는 출시 3개월 만에 300만 명의 
        사용자를 확보하며 시장의 주목을 받았습니다. 현재 증권, 보험 등 자산관리 서비스로의 
        확장을 적극 추진 중입니다.
        """)
    
    st.caption("출처: 카카오페이·네이버파이낸셜·토스 IR 자료, 한국핀테크산업협회")
    
    # 글로벌 핀테크 기업 동향
    st.markdown('<p class="subsection-header">3.2 글로벌 핀테크 동향</p>', unsafe_allow_html=True)
    
    # 3.2 글로벌 핀테크 동향 (이어서)
    st.write("""
    글로벌 핀테크 시장은 2025년 현재 다음과 같은 주요 흐름을 보이고 있습니다:
    
    1. **빅테크의 금융 진출 가속화**
       - 애플: 애플카드 출시 이후 2024년 애플 세이빙스(Apple Savings) 서비스로 예금 시장 진출
       - 메타(구 페이스북): 2023년 메타페이 출시 이후 암호화폐 결제 시스템 확장
       - 아마존: 아마존페이 외에도 2024년부터 소상공인 대상 '아마존 비즈니스 캐피털' 서비스 강화
    
    2. **슈퍼앱(Super App) 경쟁 심화**
       - 중국 위챗페이, 알리페이의 성공 모델을 벤치마킹한 슈퍼앱 전략이 글로벌로 확산
       - 동남아시아의 그랩(Grab)과 고젝(Gojek)은 라이드헤일링에서 시작해 금융, 식품배달 등으로 확장
       - 브라질 누뱅크(Nubank)는 2024년 1억 사용자를 돌파하며 남미 최대 디지털 뱅크로 성장
    
    3. **핀테크 투자 재개**
       - 2022-2023년 긴축 환경에서 주춤했던 글로벌 핀테크 투자가 2024년부터 회복세
       - 특히 B2B 핀테크, 임베디드 파이낸스, 레그텍(RegTech) 분야에 투자 집중
       - 2025년 1분기 글로벌 핀테크 투자액은 전년 동기 대비 28% 증가한 157억 달러 기록
    
    4. **IPO 및 M&A 활성화**
       - 2024년 핀테크 유니콘의 IPO 러시 (스트라이프, 클라르나 등)
       - 2025년 1분기 핀테크 분야 M&A 건수 87건으로 전년 동기 대비 35% 증가
       - 핀테크-전통금융 간 인수합병 증가 추세
    """)

    # 글로벌 핀테크 투자 트렌드 시각화
    investment_data = pd.DataFrame({
        'Quarter': ['2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1'],
        'Investment': [8.2, 9.1, 10.3, 11.5, 12.3, 13.2, 14.5, 15.1, 15.7],
        'Deals': [210, 225, 245, 260, 275, 290, 310, 330, 345]
    })
    
    st.markdown("### 글로벌 핀테크 투자 추이")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=investment_data['Quarter'],
        y=investment_data['Investment'],
        name='투자액(십억$)',
        marker_color='rgb(26, 118, 255)'
    ))
    fig.add_trace(go.Scatter(
        x=investment_data['Quarter'],
        y=investment_data['Deals'],
        name='거래 건수',
        mode='lines+markers',
        yaxis='y2',
        line=dict(color='rgb(219, 64, 82)', width=3),
        marker=dict(size=8)
    ))
    fig.update_layout(
        title='글로벌 핀테크 투자 및 거래 건수 (2023-2025)',
        xaxis=dict(title='분기'),
        yaxis=dict(title='투자액(십억$)', side='left'),
        yaxis2=dict(title='거래 건수', side='right', overlaying='y'),
        legend=dict(x=0.01, y=0.99),
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: KPMG Pulse of Fintech 2025 Q1")

# 4. 기술 혁신과 규제 환경
elif menu == "4. 기술 혁신과 규제 환경":
    st.markdown('<p class="main-header">4. 기술 혁신 및 규제 환경</p>', unsafe_allow_html=True)
    
    # 핵심 기술 도입 현황
    st.markdown('<p class="subsection-header">4.1 핵심 기술 도입 현황</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([6, 4])
    
    with col1:
        st.write("""
        2025년 현재 핀테크 산업의 핵심 기술은 **인공지능(AI)**, **블록체인**, **생체인증** 등이 주도하고 있습니다.
        
        **인공지능(AI) 신용평가 시스템**은 기존 신용평가 모델이 포착하지 못했던 다양한 데이터 포인트를 활용해
        더 정교하고 포용적인 신용평가를 가능하게 하고 있습니다. 이는 특히 신용 이력이 부족한 젊은 세대와
        금융 소외계층에게 혜택을 제공하고 있습니다.
        
        **블록체인 기술**은 중앙은행 디지털화폐(CBDC), 디지털 자산 관리, 그리고 스마트 계약을 통한 보험금
        자동 지급 등의 분야에 적용되고 있습니다. 특히 2023년 이후 규제 프레임워크가 구체화되면서
        기관 투자자의 참여가 크게 증가했습니다.
        
        **생체인증 기술**은 모바일 금융 앱의 보안성과 편의성을 동시에 향상시키는 핵심 요소로 자리잡았습니다. 
        얼굴 인식, 지문 인식을 넘어 음성 인식, 행동 패턴 분석 등 다중 생체인증 방식이 확산되고 있습니다.
        
        특히 2024년부터는 **양자암호** 기술이 금융 보안 분야에 적용되기 시작했으며, 이는 양자컴퓨팅 시대에 대비한
        선제적 보안 강화 조치로 평가받고 있습니다.
        """)
        
    with col2:
        # 기술 도입률 표
        st.markdown('<div class="table-wrapper">', unsafe_allow_html=True)
        tech_table = pd.DataFrame({
            '기술': ['AI 신용평가', '블록체인', '생체인증', '양자암호', '데이터 분석'],
            '도입률(%)': [78, 65, 82, 35, 90],
            '주요 응용 분야': ['신용평가, 리스크 관리', 'CBDC, 스마트 계약', '모바일 인증', '보안 강화', '고객 세분화']
        })
        st.table(tech_table.set_index('기술'))
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("출처: 금융감독원 핀테크 기술 동향 보고서 2025")
        
    # 기술 도입 추이 시각화
    st.markdown("### 핵심 기술 도입률 및 예상 성장률")
    fig = px.scatter(
        tech_data, 
        x='도입률(%)', 
        y='예상성장률(%)', 
        size=[50]*5,
        color='기술',
        text='기술',
        labels={'도입률(%)': '현재 도입률(%)', '예상성장률(%)': '향후 3년 예상 성장률(%)'},
        title='핀테크 핵심 기술 성장 매트릭스 (2025년 기준)'
    )
    fig.update_traces(textposition='top center')
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)
    
    # 규제 환경
    st.markdown('<p class="subsection-header">4.2 규제 환경 변화</p>', unsafe_allow_html=True)
    
    st.write("""
    핀테크 산업의 규제 환경은 지속적으로 변화하고 있으며, 2025년 주요 규제 동향은 다음과 같습니다:
    
    1. **규제 샌드박스 확대**
       - 한국은 2023년 '디지털금융혁신법' 제정으로 기존 규제 샌드박스를 확대
       - 2025년 현재 총 127개 서비스가 규제 샌드박스를 통해 테스트 중
       - 특히 AI 금융 상담, P2P 대출, 대체 신용평가 분야에 집중
    
    2. **오픈뱅킹 고도화**
       - 2024년 '오픈뱅킹 2.0' 출범으로 데이터 공유 범위 확대
       - 은행 계좌 정보뿐만 아니라 보험, 증권, 카드 데이터까지 API로 연동
       - 2025년 3월 기준 오픈뱅킹 참여기관 118개, 등록 이용자 6,750만 명 돌파
    
    3. **CBDC 규제 프레임워크 구축**
       - 한국은행의 '디지털 원화' 파일럿 프로그램 단계적 확대
       - 2025년 상반기 금융기관 대상 테스트를 거쳐 하반기 일반 사용자 대상 확대 예정
       - CBDC 운영을 위한 법적 근거 마련 ('한국은행법' 개정안 2024년 통과)
    
    4. **개인정보보호 강화**
       - 2024년 개인정보보호법 개정으로 '마이데이터 2.0' 시행
       - 정보주체의 데이터 이동권 및 통제권 강화
       - 금융회사의 데이터 보호 책임 강화 (위반 시 매출액 5%까지 과징금 부과)
    
    5. **금융지주회사법 개정**
       - 2024년 개정으로 핀테크 기업 지분 보유 한도 5% → 15% 확대
       - 금융그룹과 핀테크 기업 간 합종연횡 가속화 예상
    """)
    
    # 주요 규제 변화 타임라인
    regulation_timeline = pd.DataFrame({
        'Year': [2020, 2021, 2022, 2023, 2024, 2025],
        'Event': [
            '데이터3법 시행', 
            '마이데이터 서비스 출범', 
            '가상자산 규제 프레임워크',
            '디지털금융혁신법 제정',
            '금융지주회사법 개정',
            '한국은행법 개정 (CBDC)'
        ],
        'Impact': [65, 70, 75, 85, 90, 95]
    })
    
    st.markdown("### 핀테크 규제 환경 주요 변화")
    fig = px.line(
        regulation_timeline,
        x='Year', 
        y='Impact',
        text='Event',
        markers=True,
        labels={'Year': '연도', 'Impact': '산업 영향도', 'Event': '주요 규제 변화'},
        title='핀테크 규제 환경 변화 타임라인 (2020-2025)'
    )
    fig.update_traces(textposition='top center')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 금융감독원, 한국은행, 금융위원회 자료 종합")

# 5. 향후 전망 및 리스크
elif menu == "5. 향후 전망 및 리스크":
    st.markdown('<p class="main-header">5. 향후 전망 및 리스크 관리</p>', unsafe_allow_html=True)
    
    # 2027년 예측 시나리오
    st.markdown('<p class="subsection-header">5.1 2027년 예측 시나리오</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        핀테크 산업은 2025년 이후에도 지속적인 성장이 예상되며, 2027년까지의 전망은 다음과 같습니다:
        
        **긍정적 시나리오 (성장 가속화)**
        - **시장 규모**: 글로벌 시장 2,200조 원 돌파
        - **주요 성장 동력**: 
          - AI 기반 초개인화 금융 서비스 보편화
          - 금융과 비금융 경계의 완전한 붕괴 (임베디드 파이낸스 확산)
          - CBDC의 본격적인 상용화와 국가간 호환성 확보
          - 마이데이터 기반 맞춤형 보험, 투자 상품 확대
        - **기업 환경**:
          - 핀테크-전통 금융 간 대규모 M&A 활성화
          - 2027년까지 글로벌 Top 10 은행 중 3개는 핀테크 출신 기업으로 대체
        
        **중립적 시나리오 (안정적 성장)**
        - **시장 규모**: 글로벌 시장 2,000조 원 달성
        - **주요 특징**:
          - 일부 핀테크 영역에서의 수익성 문제 지속
          - 규제 환경의 불확실성으로 일부 서비스 출시 지연
          - 빅테크와 전통 금융 기관의 디지털 전환으로 경쟁 심화
        
        **부정적 시나리오 (성장 둔화)**
        - **시장 규모**: 글로벌 시장 1,850조 원 수준
        - **주요 위험 요소**:
          - 대규모 사이버 보안 사고에 따른 소비자 신뢰 하락
          - 글로벌 경기침체로 인한 투자 감소
          - 규제 강화로 인한 혁신 서비스 출시 제약
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 2027년 핵심 예측
        
        - 시장 규모: 2,000-2,200조 원
        - 연평균 성장률: 15-20%
        - 최대 성장 분야: DeFi, 임베디드 파이낸스
        - 신규 사용자: 20억 명 이상
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 시나리오별 시장 규모 전망
    scenario_data = pd.DataFrame({
        'Year': [2025, 2026, 2027],
        'Optimistic': [1550, 1850, 2200],
        'Base': [1550, 1750, 2000],
        'Pessimistic': [1550, 1680, 1850]
    })
    
    st.markdown("### 시나리오별 핀테크 시장 규모 전망")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=scenario_data['Year'], 
        y=scenario_data['Optimistic'],
        name='긍정적 시나리오',
        mode='lines+markers',
        line=dict(color='rgb(0, 176, 80)', width=3),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=scenario_data['Year'], 
        y=scenario_data['Base'],
        name='중립적 시나리오',
        mode='lines+markers',
        line=dict(color='rgb(255, 192, 0)', width=3),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=scenario_data['Year'], 
        y=scenario_data['Pessimistic'],
        name='부정적 시나리오',
        mode='lines+markers',
        line=dict(color='rgb(192, 0, 0)', width=3),
        marker=dict(size=8)
    ))
    fig.update_layout(
        title='핀테크 글로벌 시장 시나리오별 전망 (2025-2027)',
        xaxis=dict(title='연도'),
        yaxis=dict(title='시장 규모(조 원)'),
        legend=dict(x=0.01, y=0.99),
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 리스크 요인
    st.markdown('<p class="subsection-header">5.2 주요 리스크 요인</p>', unsafe_allow_html=True)
    
    st.write("""
    핀테크 산업이 직면한 주요 리스크 요인은 다음과 같습니다:
    
    1. **사이버 보안 위협**
       - 2023-2025년 핀테크 대상 해킹 시도 230% 증가
       - 특히 AI 기반 딥페이크를 활용한 신원 도용 위협 급증
       - 클라우드 기반 금융 서비스의 취약점 악용 사례 증가
    
    2. **규제 불확실성**
       - 글로벌 규제 프레임워크의 비일관성으로 인한 국가간 서비스 확장 어려움
       - 데이터 주권 관련 규제 강화로 국경간 데이터 이동 제약 가능성
       - 탈중앙화 금융(DeFi)에 대한 규제 프레임워크 불확실성 지속
    
    3. **기술 의존도 심화**
       - 핵심 기술 공급업체에 대한 의존도 증가로 시스템 리스크 확대
       - 오픈소스 및 API 의존성으로 인한 공급망 보안 위험
       - AI 알고리즘의 '블랙박스' 문제로 인한 설명가능성 이슈
    
    4. **고객 신뢰 확보**
       - 디지털 신원 관리 및 개인정보 보호에 대한 우려 증가
       - 금융 소비자 보호 관점에서의 책임 소재 불명확성
       - 디지털 격차(Digital Divide)로 인한 금융 소외 위험
    """)
    
    # 리스크 요소 시각화
    st.markdown("### 주요 리스크 요소 분석")
    fig = px.bar(
        risk_data.sort_values(by='위험도(1-10)', ascending=False),
        x='위험요소',
        y='위험도(1-10)',
        color='증가율(%)',
        color_continuous_scale='Reds',
        text='증가율(%)',
        labels={'위험요소': '주요 리스크', '위험도(1-10)': '위험도 점수'},
        title='핀테크 산업 주요 리스크 요인 및 증가율 (2025년)'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: KISA 사이버보안 동향 보고서, 금융감독원 리스크 평가")
    
    # 리스크 대응 전략
    st.markdown('<p class="subsection-header">5.3 리스크 대응 전략</p>', unsafe_allow_html=True)
    
    st.write("""
    향후 핀테크 산업의 지속가능한 성장을 위한 리스크 대응 전략은 다음과 같습니다:
    
    1. **사이버 보안 강화**
       - 제로트러스트(Zero Trust) 아키텍처 도입 확대
       - AI 기반 이상탐지 시스템 고도화
       - 양자암호 도입을 통한 미래 보안 위협 대비
       - 업계 공동의 사이버 위협 인텔리전스 공유 플랫폼 구축
    
    2. **규제 대응 체계 구축**
       - 선제적 규제 모니터링 및 컴플라이언스 자동화
       - 레그텍(RegTech) 솔루션 고도화
       - 규제당국과의 개방적 커뮤니케이션 채널 유지
       - 자율규제 체계 확립을 통한 산업 신뢰 제고
    
    3. **기술 리스크 관리**
       - 핵심 기술에 대한 멀티벤더 전략 구축
       - 온프레미스-클라우드 하이브리드 아키텍처 운영
       - 오픈소스 의존성 관리 및 취약점 모니터링 강화
       - 상시 재해복구 훈련 및 비즈니스 연속성 계획 고도화
    
    4. **소비자 신뢰 확보**
       - 투명한 정보 제공 및 금융 교육 강화
       - 디지털 취약계층을 위한 접근성 개선
       - 고객 데이터 사용에 대한 옵트인(opt-in) 원칙 강화
       - 분쟁 해결 프로세스 간소화 및 신속화
    """)

# 6. 결론 및 참고문헌
elif menu == "6. 결론 및 참고문헌":
    st.markdown('<p class="main-header">6. 결론: 금융의 미래를 위한 제언</p>', unsafe_allow_html=True)
    
    st.write("""
    핀테크 산업은 2025년 현재 금융 서비스의 본질을 근본적으로 변화시키고 있으며, 
    이러한 혁신의 물결은 향후에도 지속될 것으로 예상됩니다. 본 보고서의 분석을 토대로 
    핀테크의 미래를 준비하기 위한 주요 제언은 다음과 같습니다:
    
    1. **기술 투자 확대**
       - AI와 블록체인 등 핵심 기술 R&D 예산 2배 이상 확대
       - 특히 금융 서비스의 초개인화를 위한 AI 응용 연구에 집중
       - 양자내성암호(PQC) 등 미래 보안 기술에 선제적 투자
    
    2. **규제 샌드박스 강화**
       - 혁신적 금융 서비스를 실험할 수 있는 테스트베드 확대
       - 국가간 규제 조화를 위한 글로벌 협력 채널 구축
       - 민간 주도의 자율규제와 공적 규제의 균형점 모색
    
    3. **소비자 교육 강화**
       - 디지털 금융 리터러시 프로그램 의무화
       - 금융소비자 보호를 위한 알기 쉬운 정보 제공 표준화
       - 디지털 금융 사기 예방을 위한 인식 제고 캠페인 실시
    
    4. **생태계 협력 강화**
       - 핀테크 스타트업-금융기관-빅테크 간 협력 모델 다각화
       - 오픈API와 표준화를 통한 상호운용성 확대
       - 공공-민간 파트너십을 통한 금융 혁신 기반 구축
    
    5. **포용적 금융 실현**
       - 디지털 소외계층을 위한 접근성 개선 방안 마련
       - 대안 신용평가 모델을 통한 금융 접근성 확대
       - 지역 기반 금융 서비스와 핀테크의 결합 모델 발굴
    """)
    
        # 핵심 제언 시각화
    recommendations = [
        '기술 투자 확대', '규제 샌드박스 강화', '소비자 교육 강화',
        '생태계 협력 강화', '포용적 금융 실현'
    ]
    importance = [95, 88, 82, 90, 85]
    urgency = [90, 85, 75, 80, 88]
    
    # 핵심 제언 시각화
    rec_data = pd.DataFrame({
        '제언': recommendations,
        '중요도': importance,
        '시급성': urgency
    })
    
    st.markdown("### 핀테크 발전을 위한 핵심 제언")
    fig = px.scatter(
        rec_data,
        x='중요도',
        y='시급성',
        text='제언',
        size=[50]*5,
        color='제언',
        labels={'중요도': '중요도(100점 만점)', '시급성': '시급성(100점 만점)'},
        title='핀테크 산업 발전을 위한 5대 제언 매트릭스'
    )
    fig.update_traces(textposition='top center')
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)
    
    # 맺음말
    st.markdown('<p class="subsection-header">6.1 맺음말: 디지털 금융의 미래</p>', unsafe_allow_html=True)
    
    st.write("""
    핀테크 산업은 2025년을 기점으로 성숙기에 진입하고 있습니다. 초기의 단순 서비스 디지털화에서 벗어나
    금융의 본질적 기능을 재정의하고 혁신하는 단계로 진화하고 있습니다. 특히 주목할 점은 금융과 비금융의
    경계가 빠르게 허물어지고 있다는 점입니다.
    
    금융서비스가 일상 생활의 다양한 영역에 자연스럽게 통합되는 '임베디드 파이낸스'는 이제 단순한 트렌드가
    아닌 핵심 비즈니스 모델로 자리잡고 있습니다. 또한 AI와 빅데이터를 활용한 초개인화 금융 서비스는
    고객 경험을 근본적으로 변화시키고 있습니다.
    
    향후 핀테크 산업의 지속가능한 성장을 위해서는 혁신과 안정성, 포용성과 효율성 사이의 균형이 중요합니다.
    이를 위해 산업계, 정부, 학계, 소비자 간의 긴밀한 소통과 협력이 필수적입니다.
    
    본 보고서가 한국 핀테크 산업의 현재를 진단하고 미래를 준비하는 데 유용한 참고자료가 되기를 바랍니다.
    """)
    
    # 참고문헌
    st.markdown('<p class="subsection-header">6.2 참고문헌</p>', unsafe_allow_html=True)
    
    references = [
        "금융위원회 (2024). 「2025년 금융산업 전망과 과제」. 서울: 금융위원회.",
        "금융감독원 (2025). 「핀테크 산업 동향 분석」. 서울: 금융감독원.",
        "한국은행 (2025). 「중앙은행 디지털화폐(CBDC) 추진 현황」. 서울: 한국은행.",
        "한국핀테크산업협회 (2024). 「핀테크 기업 실태조사」. 서울: 한국핀테크산업협회.",
        "삼정KPMG (2025). 「글로벌 핀테크 트렌드 리포트」. 서울: 삼정KPMG.",
        "BCiF (2025). 「Blockchain in Finance 2025」. London: BCiF Research.",
        "Gartner (2024). 「금융서비스 기술 전망 2024-2025」. Stanford: Gartner Inc.",
        "IDC (2025). 「Worldwide FinTech Spending Guide」. Framingham: IDC.",
        "McKinsey & Company (2025). 「글로벌 핀테크 리포트」. New York: McKinsey & Company.",
        "PwC (2025). 「핀테크 트렌드 2025」. London: PwC.",
        "World Economic Forum (2024). 「Future of Financial Services 2025」. Geneva: WEF."
    ]
    
    for i, ref in enumerate(references):
        st.write(f"{i+1}. {ref}")

