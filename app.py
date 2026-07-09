import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================================
# Page Configuration & Styling
# ==========================================================================
st.set_page_config(
    page_title="John Parente Jr. | Interactive Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection for premium aesthetics (Dark/Light responsive elements)
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .metric-container {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
</style>
""", unsafe_html=True)

# ==========================================================================
# Projects Database (Mirroring HTML database for consistency)
# ==========================================================================
projects_data = [
    {
        "title": "AI-Business-Analyst-Demo",
        "description": "An AI-powered business analyst demo leveraging language models to automate complex reporting, analysis, and dashboard generation.",
        "category": "AI & ML",
        "language": "TypeScript",
        "link": "https://github.com/johnparente97/AI-Business-Analyst-Demo",
        "tech": ["TypeScript", "LLM APIs", "JSON Data Modeling"],
        "value": "Demonstrates practical integration of generative AI into business analysis workflows, automating data interpretation and turning raw metrics into stakeholder-ready summaries."
    },
    {
        "title": "aep-customer-identity-pipeline",
        "description": "Customer identity resolution pipeline tailored for Adobe Experience Platform (AEP), consolidating cross-device profiles into single customer schemas.",
        "category": "Pipelines",
        "language": "JavaScript",
        "link": "https://github.com/johnparente97/aep-customer-identity-pipeline",
        "tech": ["JavaScript", "AEP API", "Identity Resolution"],
        "value": "Solves critical customer identity gaps by merging fragmented event streams, enabling marketers and analysts to view accurate client journey profiles."
    },
    {
        "title": "aep-web-tracking-lab",
        "description": "Implementation sandbox for web tracking SDKs, capturing customer touchpoints, clicks, and page behaviors for analytics databases.",
        "category": "Pipelines",
        "language": "HTML",
        "link": "https://github.com/johnparente97/aep-web-tracking-lab",
        "tech": ["HTML", "JavaScript", "Adobe SDKs"],
        "value": "Validates tracking structures, data layers, and custom event tracking. Reduces data reconciliation errors before production deployment."
    },
    {
        "title": "Python-Banking-Suite",
        "description": "Modular banking simulator designed to manage savings, compound interest calculations, and CD account growth with high precision.",
        "category": "Software Development",
        "language": "Python",
        "link": "https://github.com/johnparente97/Python-Banking-Suite-Managing-Savings-CD-Accounts-with-Modular-Design",
        "tech": ["Python", "OOP", "Financial Math"],
        "value": "Built with modular design principles (OOP). Provides clear code structures that automate interest projections and demonstrate software architecture fundamentals."
    },
    {
        "title": "Geo-Retail-Analytics-Footwear",
        "description": "Geographic retail analytics notebook tracking regional sales volumes, consumer trends, and stock adjustments for athletic footwear.",
        "category": "Data Analytics",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Geo-Retail-Analytics-Regional-Sales-and-Trends-in-Athletic-Footwear",
        "tech": ["Jupyter Notebook", "Pandas", "Matplotlib", "Geopandas"],
        "value": "Applies supply chain and marketing insights to regional sales data. Creates visual geographic maps highlighting product demand hotspots."
    },
    {
        "title": "E-Commerce-Strategic-Analysis",
        "description": "Advanced analysis optimizing client portfolios, spend behaviors, and product pricing models to maximize profit margin.",
        "category": "Data Analytics",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/E-Commerce-Strategic-Analysis-for-Client-and-Profit-Optimization",
        "tech": ["Python", "Pandas", "Profit Modeling"],
        "value": "Models supplier costs and customer purchase size to identify off-contract leakage. Directly reflects skills used in procurement and spend reconciliation."
    },
    {
        "title": "QuickServe-Ordering-System",
        "description": "Interactive ordering and transaction system simulation built to optimize customer flow, checkout speed, and kitchen queue processing.",
        "category": "Software Development",
        "language": "Python",
        "link": "https://github.com/johnparente97/QuickServe-Ordering-System",
        "tech": ["Python", "Queue Simulation", "UI"],
        "value": "Utilizes event-based design to model physical business operations, validating optimization of supply chain logistics at point of sale."
    },
    {
        "title": "Search-Trends-Stock-Forecasting",
        "description": "Time-series study correlating Google search volume patterns against stock price variations to generate predictive forecasting signals.",
        "category": "Data Analytics",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Patterns-in-Search-Data-and-Stock-Prices-for-Strategic-Forecasting",
        "tech": ["Jupyter Notebook", "Prophet", "Statsmodels", "Pandas"],
        "value": "Leverages predictive modeling (Prophet) to reveal seasonal search trends and their market implications, helping businesses anticipate consumer focus shifts."
    },
    {
        "title": "CryptoClustering-K-Means-PCA",
        "description": "Machine learning application classifying cryptocurrency market performance using Principal Component Analysis (PCA) and K-Means clustering.",
        "category": "AI & ML",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/CryptoClustering-K-Means-PCA-Driven-Cryptocurrency-Market-Analysis",
        "tech": ["Python", "Scikit-Learn", "K-Means", "PCA"],
        "value": "Simplifies high-dimensional market data into clear clusters. Proves ability to deploy statistical techniques to segment financial assets."
    },
    {
        "title": "Email-Guardian-ML-Filter",
        "description": "Supervised machine learning pipeline evaluating text token frequencies to classify and filter spam emails.",
        "category": "AI & ML",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Email-Guardian-Harnessing-Machine-Learning-to-Filter-the-Inbox",
        "tech": ["Python", "NLP", "Naive Bayes", "Scikit-Learn"],
        "value": "Implements security and automation in communications. Turns unstructured text data into actionable routing decisions using machine learning."
    },
    {
        "title": "Employee-Attrition-Neural-Network",
        "description": "Deep learning neural network modeling employee attributes to predict turnover probabilities and appropriate department placement.",
        "category": "AI & ML",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Employee-Attrition-Department-Prediction-Neural-Network",
        "tech": ["TensorFlow", "Keras", "Deep Learning"],
        "value": "Provides HR and operations teams with predictive attrition foresight. Enables preventative retention actions by flagging departments at risk."
    },
    {
        "title": "Spam-or-Ham-Text-Classification",
        "description": "Natural Language Processing (NLP) text classification model targeting SMS data to identify messages as ham or spam.",
        "category": "AI & ML",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Spam-or-Ham-Text-Message-Classification-with-Machine-Learning",
        "tech": ["Python", "NLP", "TF-IDF", "Random Forest"],
        "value": "Demonstrates text preprocessing, feature engineering (TF-IDF vectorizer), and model evaluation metrics for business automation."
    },
    {
        "title": "Sourcing-Movie-Data-With-APIs",
        "description": "Data collection engine connecting to external REST APIs, downloading metadata, cleaning schemas, and outputting clean database records.",
        "category": "Pipelines",
        "language": "Jupyter Notebook",
        "link": "https://github.com/johnparente97/Sourcing-Movie-Data-With-APIs",
        "tech": ["API Integration", "JSON Extraction", "Pandas"],
        "value": "Showcases ETL (Extract, Transform, Load) pipelines. Translates nested API payloads into flat, normalized tables prepared for dashboarding."
    },
    {
        "title": "Solana-Case-Study",
        "description": "Thorough market research and technical evaluation of the Solana blockchain framework, network costs, and scalability metrics.",
        "category": "Data Analytics",
        "language": "Rich Text Format",
        "link": "https://github.com/johnparente97/Solana-Case-Study",
        "tech": ["Market Analysis", "Blockchain Research", "Strategy"],
        "value": "Highlights strategic technology evaluation skills. Explains complex blockchain performance data to help operators assess adoption opportunities."
    }
]

# ==========================================================================
# Sidebar Profile Information
# ==========================================================================
with st.sidebar:
    st.title("John Parente, Jr.")
    st.caption("Account Management | Operations | Analytics")
    st.markdown("📍 Cleveland, OH")
    st.markdown("✉️ jrjohnparente@gmail.com")
    st.markdown("📞 216-925-6825")
    
    st.divider()
    
    st.markdown("### Education")
    st.markdown("**John Carroll University**")
    st.caption("B.S.B.A. in Marketing & Supply Chain Management")
    st.caption("Boler College of Business")
    
    st.markdown("**The Ohio State University**")
    st.caption("AI & Machine Learning Bootcamp Certification")
    st.caption("College of Engineering")
    
    st.divider()
    st.markdown("### Profiles")
    st.markdown("[LinkedIn](https://linkedin.com/in/johnparentejr)")
    st.markdown("[GitHub](https://github.com/johnparente97)")

# ==========================================================================
# Main Content Area
# ==========================================================================
st.title("John Parente Jr. — Interactive Portfolio")
st.markdown("""
Welcome to my interactive dashboard. This application showcases my background in **GPO operations**, **procurement spend analytics**, and **machine learning workflows**. 
""")

tab_overview, tab_experience, tab_projects, tab_expertise = st.tabs([
    "📈 Overview & Impact", 
    "💼 Professional Experience", 
    "📁 GitHub Projects", 
    "🧠 Core Expertise"
])

# ==========================================================================
# Tab 1: Overview & Impact Dashboard
# ==========================================================================
with tab_overview:
    st.header("Portfolio Impact Snapshot")
    
    # Grid of Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Active Accounts Managed", value="50+", delta="HealthTrust/Foodbuy")
    with col2:
        st.metric(label="Spend Analyzed", value="$10M+", delta="GPO Portfolio")
    with col3:
        st.metric(label="Rebates Reported", value="$150K+", delta="Reconciliation")
    with col4:
        st.metric(label="CRM Account Views", value="100+", delta="Account Tracking")
    with col5:
        st.metric(label="Instagram Scale", value="37K ➔ 42.5K", delta="+5,500 Followers")
        
    st.divider()
    
    st.subheader("GPO Portfolio Spend & Savings Simulator")
    st.markdown("""
    Below is a breakdown simulator reflecting typical spend categories, GPO contract compliance ratios, and potential savings projections. 
    *Adjust variables using the interactive sidebar inputs inside this card to model savings recovery.*
    """)
    
    # Mock GPO Data
    gpo_data = pd.DataFrame({
        'Category': ['Medical/Surgical', 'Food Services', 'Facilities & Maintenance', 'Office & IT Supplies'],
        'Spend_Volume_USD': [4500000, 3200000, 1300000, 1000000],
        'Compliance_Rate': [0.92, 0.88, 0.78, 0.85],
        'Average_Rebate_Rate': [0.015, 0.012, 0.010, 0.018]
    })
    
    # Visualizations Columns
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Spend Chart
        fig_spend = px.bar(
            gpo_data, 
            x='Category', 
            y='Spend_Volume_USD',
            title="Spend Volume by GPO Category",
            labels={'Spend_Volume_USD': 'Spend Volume ($)', 'Category': 'Category'},
            color='Category',
            color_discrete_sequence=px.colors.sequential.Indigo
        )
        st.plotly_chart(fig_spend, use_container_width=True)
        
    with col_chart2:
        # Compliance Chart
        fig_comp = px.bar(
            gpo_data,
            y='Category',
            x='Compliance_Rate',
            title="Contract Compliance Utilization (%)",
            labels={'Compliance_Rate': 'Compliance Utilization', 'Category': 'Category'},
            orientation='h',
            color='Category',
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig_comp.update_layout(xaxis_tickformat=',.0%')
        st.plotly_chart(fig_comp, use_container_width=True)
        
    # Interactive Savings Calculator card
    st.markdown("### Interactive Off-Contract Leakage Calculator")
    calc_col1, calc_col2, calc_col3 = st.columns(3)
    
    with calc_col1:
        selected_cat = st.selectbox("Select Spend Category", gpo_data['Category'])
        row = gpo_data[gpo_data['Category'] == selected_cat].iloc[0]
        
    with calc_col2:
        input_spend = st.number_input(
            "Modify Category Spend Volume ($)", 
            min_value=10000, 
            max_value=10000000, 
            value=int(row['Spend_Volume_USD']),
            step=50000
        )
        
    with calc_col3:
        input_comp = st.slider(
            "Target Contract Compliance (%)", 
            min_value=50, 
            max_value=100, 
            value=int(row['Compliance_Rate'] * 100)
        ) / 100
        
    # Calculations
    current_leakage = input_spend * (1 - row['Compliance_Rate'])
    target_leakage = input_spend * (1 - input_comp)
    savings_recovery = current_leakage - target_leakage
    rebate_gain = savings_recovery * row['Average_Rebate_Rate']
    
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric(
            label="Current Off-Contract Leakage", 
            value=f"${current_leakage:,.2f}",
            delta="- Leakage"
        )
    with metric_col2:
        st.metric(
            label="Projected Savings Recovery", 
            value=f"${savings_recovery:,.2f}", 
            delta=f"+{input_comp - row['Compliance_Rate']:.1%} compliance",
            delta_color="normal"
        )
    with metric_col3:
        st.metric(
            label="Additional Projected Rebate Earned", 
            value=f"${rebate_gain:,.2f}",
            delta=f"+{row['Average_Rebate_Rate']:.1%} rebate rate",
            delta_color="normal"
        )

# ==========================================================================
# Tab 2: Professional Experience
# ==========================================================================
with tab_experience:
    st.header("Professional Experience Details")
    
    # Catholic Community Connection
    with st.expander("💼 GPO Account Manager — Catholic Community Connection (May 2022 - Present)", expanded=True):
        st.markdown("""
        **Cleveland, OH** | *Managed HealthTrust, AdvantageTrust, and Foodbuy portfolios for healthcare, senior living, nonprofit, diocesan, and educational accounts.*
        
        *   **Portfolio Management:** Managed and optimized a 50+ member portfolio structure, ensuring prompt onboarding and dispute resolution.
        *   **Spend Optimization:** Analyzed $10M+ in purchasing volumes to discover contract conversion opportunities and identify off-contract spend leakage.
        *   **Executive Reporting:** Designed utilization dashboards, executive-ready presentations, and Board reports detailing spend indicators.
        *   **Process Improvement:** Improved reporting operations by building SharePoint folders, Excel Power Query pipelines, and CRM workbooks to reduce manual reporting efforts.
        *   **Outreach & Adoption:** Developed marketing outreach strategies, website descriptions, print collateral, and event updates to support vendor coordination.
        """)
        
    # June Incorporated
    with st.expander("🚀 Founder & E-Commerce Director — June Incorporated (Jul 2019 - Nov 2025)"):
        st.markdown("""
        **Brooklyn, OH** | *Built a student digital marketing concept into a launched brand and e-commerce venture.*
        
        *   **Business Operations:** Sourced product manufacturers, negotiated unit pricing, controlled fulfillment workflows, and managed strategic brand growth.
        *   **Audience Growth:** Scaled Instagram audience from 37,000 to over 42,500+ followers through visual design, contents curation, and targeted ad campaigns.
        *   **Tech Infrastructure:** Maintained online web presence, payment gateway pipelines, shipping workflows, and client support channels.
        """)
        
    # Additional
    with st.expander("📄 Additional Experience (SEO, Operations & Logistics)"):
        st.markdown("""
        *   **CO-AX Technology Inc. (Marketing/SEO Support):** Maintained keywords registries, analyzed page speeds and page-performance metrics, and parsed website visitor traffic metrics for industrial hardware portfolios.
        *   **Fulfillment & Operations Roles:** Strengthened order processing metrics, inventory accuracy, client communications, and vendor scheduling in busy supply environments.
        """)

# ==========================================================================
# Tab 3: GitHub Projects Portfolio
# ==========================================================================
with tab_projects:
    st.header("GitHub Repository Explorer")
    st.markdown("Search, filter, and drill into my active GitHub repositories to evaluate their business values and tech frameworks.")
    
    # Filter Controls
    search_query = st.text_input("🔍 Search Repositories", "", placeholder="Enter keyword (e.g., K-Means, AEP, simulator, Pandas)...")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        categories = ["All"] + sorted(list(set([p['category'] for p in projects_data])))
        selected_category = st.selectbox("Filter by Category", categories)
        
    with col_f2:
        languages = ["All"] + sorted(list(set([p['language'] for p in projects_data])))
        selected_lang = st.selectbox("Filter by Language", languages)
        
    # Filtering Logic
    filtered_projects = []
    for p in projects_data:
        # Category Filter
        if selected_category != "All" and p['category'] != selected_category:
            continue
        # Language Filter
        if selected_lang != "All" and p['language'] != selected_lang:
            continue
        # Search Filter
        if search_query:
            query = search_query.lower()
            in_title = query in p['title'].lower()
            in_desc = query in p['description'].lower()
            in_tech = any(query in t.lower() for t in p['tech'])
            in_lang = query in p['language'].lower()
            if not (in_title or in_desc or in_tech or in_lang):
                continue
        filtered_projects.append(p)
        
    # Rendering grid
    st.markdown(f"**Showing {len(filtered_projects)} of {len(projects_data)} projects**")
    
    for project in filtered_projects:
        with st.container():
            col_card1, col_card2 = st.columns([3, 1])
            with col_card1:
                st.subheader(project['title'])
                st.caption(f"📁 {project['category']}  |  💻 {project['language']}")
                st.write(project['description'])
                
                # Expandable details
                with st.expander("🔎 View Business Value & Technical Stack"):
                    st.markdown("**Core Technologies:**")
                    st.write(", ".join(project['tech']))
                    st.markdown("**Business Value & Real-world Impact:**")
                    st.info(project['value'])
            with col_card2:
                st.write("") # Spacer
                st.write("") # Spacer
                st.write("") # Spacer
                st.markdown(f"[Go to GitHub Repo ↗]({project['link']})")
                
            st.divider()

# ==========================================================================
# Tab 4: Core Expertise
# ==========================================================================
with tab_expertise:
    st.header("Core Competencies & Toolkit Mapping")
    
    col_exp1, col_exp2 = st.columns(2)
    
    with col_exp1:
        st.subheader("Professional Expertise")
        st.markdown("""
        *   **Account Portfolio Management:** Onboarding operations, CRM integration, client retention strategies.
        *   **Spend & Rebate Analytics:** Purchasing volume modeling, margin leakage identification, rebate validation.
        *   **Process Improvement & Automation:** SharePoint infrastructure, Excel Power Query, automated Power Automate flows.
        *   **Digital Marketing & Content Strategy:** Visual branding campaigns, social media logistics, traffic audit.
        """)
        
    with col_exp2:
        st.subheader("Technical Toolbox")
        st.markdown("**Data Pipelines & Operations:**")
        st.write("Excel (Power Query), SharePoint, Power Automate, Google Analytics, SEO, CRM Workbooks.")
        
        st.markdown("**Coding Languages:**")
        st.write("Python, SQL, TypeScript, JavaScript, HTML/CSS.")
        
        st.markdown("**AI, Modeling & Science Libraries:**")
        st.write("Google AI Studio, Streamlit, TensorFlow, Keras, Scikit-Learn, Pandas, NumPy, Plotly.")
