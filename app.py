import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG 
st.set_page_config(
    page_title="India Dashboard",
    page_icon="🇮🇳",
    layout="wide"
)

# ---------------- SIDEBAR LOGIN 
st.sidebar.title("🔐 Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username == "kunal" and password == "1234":

    st.sidebar.success("Login Successful ✅")

    # ---------------- LOAD DATA 
    df = pd.read_csv("data.csv")

    # ---------------- MAIN TITLE 
    st.title("🇮🇳 India Analytics Dashboard")

    st.markdown("### Streamlit Dashboard Project")

    # ----------- SIDEBAR MENU 
    st.sidebar.title("📌 Navigation")

    menu = st.sidebar.radio(
        "Go To",
        ["Home", "Data Table", "EDA", "Charts"]
    )

    # ------------ SEARCH 
    search = st.sidebar.text_input("🔍 Search State")

    if search:
        df = df[df["State"].str.contains(search, case=False)]

    # ----------- HOME PAGE 
    if menu == "Home":

        st.header("📊 Dashboard Overview")

        # Metrics
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total States",
            len(df)
        )

        col2.metric(
            "Total Population",
            df["Population"].sum()
        )

        col3.metric(
            "Total IT Companies",
            df["IT_Companies"].sum()
        )

        # Image
        st.image(
            "https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
            width=250
        )

        st.success("Welcome to India Dashboard")

    #  DATA TABLE 
    elif menu == "Data Table":

        st.header("📋 Data Table")

        st.dataframe(df)

    # --EDA -
    elif menu == "EDA":

        st.header("📈 Exploratory Data Analysis")

        st.subheader("Dataset Summary")

        st.write(df.describe())

        st.subheader("Top 5 Rows")

        st.write(df.head())

        st.subheader("Columns")

        st.write(df.columns)

        st.subheader("Missing Values")

        st.write(df.isnull().sum())

    # ---------------- CHARTS ----------------
    elif menu == "Charts":

        st.header("📊 Interactive Charts")

        # Pie Chart
        st.subheader("Population Distribution")

        pie_chart = px.pie(
            df,
            names="State",
            values="Population",
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        st.plotly_chart(pie_chart)

        # Bar Chart
        st.subheader("IT Companies by State")

        bar_chart = px.bar(
            df,
            x="State",
            y="IT_Companies",
            color="State",
            text_auto=True
        )

        st.plotly_chart(bar_chart)

        # Scatter Plot
        st.subheader("Population vs IT Companies")

        scatter_chart = px.scatter(
            df,
            x="Population",
            y="IT_Companies",
            size="Area",
            color="State",
            hover_name="State"
        )

        st.plotly_chart(scatter_chart)

    # --------- LOGOUT
    if st.sidebar.button("Logout"):

        st.sidebar.warning("Logged Out")

else:

    st.warning("❌ Incorrect Username or Password")

    st.info("Username: kunal")
    st.info("Password: 1234")