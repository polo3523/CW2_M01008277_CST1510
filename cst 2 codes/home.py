import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.express as px
# Week 11 Requirement: Import your OOP Model
from models import Incident
from application import get_db_connection, login_user, register_user

st.set_page_config(page_title="Intelligent Platform", layout="wide")

# 1. Session State (Week 9 Requirement)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""

# 2. Sidebar
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", ["Dashboard", "Cyber Incidents", "Account"])

# --- SECTION: DASHBOARD ---
if choice == "Dashboard":
    st.title("Platform Overview")
    st.write("Welcome to your unified intelligence platform.")
    if st.session_state['logged_in']:
        st.info(f"Logged in as: {st.session_state['username']}")
    else:
        st.warning("Please log in via the Account page.")

# --- SECTION: CYBER INCIDENTS (Refactored with OOP) ---
elif choice == "Cyber Incidents":
    st.title("🚨 Cyber Incidents Dashboard")

    if not st.session_state.get('logged_in', False):
        st.warning("Please log in to access the Incident Management system.")
    else:
        conn = get_db_connection()
        try:
            # READ: Load data from SQLite
            df = pd.read_sql_query("SELECT * FROM cyber_incidents", conn)

            if not df.empty:
                # --- WEEK 11: OOP REFACTORING ---
                # Convert database rows into Incident Objects
                incident_objects = []
                for _, row in df.iterrows():
                    obj = Incident(
                        row['id'], row['title'], row['category'],
                        row['severity'], row['status'],
                        row['date_reported'], row['date_resolved']
                    )
                    incident_objects.append(obj)

                # --- WEEK 9: VISUALIZATIONS ---
                st.subheader("📊 Performance & Trend Analysis")
                tab_trend, tab_bottleneck = st.tabs(["Threat Trends", "Resolution Bottlenecks"])

                with tab_trend:
                    # Identifies "Phishing Surge"
                    fig1 = px.bar(df['category'].value_counts().reset_index(),
                                  x='category', y='count', title="Incident Volume by Type")
                    st.plotly_chart(fig1, use_container_width=True)

                with tab_bottleneck:
                    # Uses OOP Method to calculate resolution hours
                    resolved_data = []
                    for obj in incident_objects:
                        res_time = obj.calculate_resolution_time()
                        if res_time is not None:
                            resolved_data.append({"Category": obj.category, "Hours": res_time})

                    if resolved_data:
                        res_df = pd.DataFrame(resolved_data)
                        avg_res = res_df.groupby("Category")["Hours"].mean().reset_index()
                        fig2 = px.bar(avg_res, x='Category', y='Hours', title="Avg Resolution Time (Hours)",
                                      color='Hours')
                        st.plotly_chart(fig2, use_container_width=True)
                    else:
                        st.info("Mark incidents as 'Resolved' to see bottleneck analysis.")

                # --- WEEK 8: UPDATE (Resolve Feature) ---
                st.subheader("📋 Active Incidents")
                for obj in incident_objects:
                    if obj.status == 'Open':
                        c1, c2, c3 = st.columns([5, 3, 2])
                        c1.write(obj.get_summary())  # Using OOP method
                        c2.write(f"Priority: {obj.severity}")
                        if c3.button("Resolve", key=f"res_{obj.id}"):
                            cursor = conn.cursor()
                            cursor.execute(
                                "UPDATE cyber_incidents SET status='Resolved', date_resolved=CURRENT_TIMESTAMP WHERE id=?",
                                (obj.id,))
                            conn.commit()
                            st.rerun()

                # --- WEEK 10: AI ASSISTANT ---
                st.markdown("---")
                st.subheader("🤖 AI Security Assistant")
                user_q = st.text_input("Ask for advice based on current data:")
                if user_q:
                    summary_stats = df['category'].value_counts().to_dict()
                    st.info("💡 *AI Simulation Mode*")
                    if "Phishing" in str(summary_stats):
                        st.write(
                            f"**Advice:** I detect {summary_stats.get('Phishing')} Phishing cases. Implement MFA immediately.")
                    else:
                        st.write("**Advice:** No critical trends detected in the current log.")

            # --- WEEK 8: CREATE (New Incident Form) ---
            st.markdown("---")
            with st.form("new_incident"):
                st.subheader("🚀 Report New Incident")
                title = st.text_input("Incident Title")
                cat = st.selectbox("Category", ["Phishing", "Malware", "DDoS", "Unauthorized Access"])
                sev = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
                if st.form_submit_button("Submit"):
                    if title:
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO cyber_incidents (title, category, severity, status) VALUES (?, ?, ?, 'Open')",
                            (title, cat, sev))
                        conn.commit()
                        st.rerun()

        finally:
            conn.close()

# --- SECTION: ACCOUNT (Week 7/9) ---
elif choice == "Account":
    st.title("👤 Account Management")
    if st.session_state['logged_in']:
        st.success(f"Logged in as {st.session_state['username']}")
        if st.button("Log Out"):
            st.session_state['logged_in'] = False
            st.rerun()
    else:
        t1, t2 = st.tabs(["Login", "Register"])
        with t1:
            u = st.text_input("Username", key="l_u")
            p = st.text_input("Password", type="password", key="l_p")
            if st.button("Login"):
                success, msg = login_user(u, p)
                if success:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = u
                    st.rerun()
                else:
                    st.error(msg)
        with t2:
            ru = st.text_input("New Username", key="r_u")
            rp = st.text_input("New Password", type="password", key="r_p")
            if st.button("Register"):
                if ru and rp:
                    s, m = register_user(ru, rp)
                    st.success(m) if s else st.error(m)