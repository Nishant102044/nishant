<<<<<<< HEAD
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Analytics Dashboard",
    layout="wide"
)

st.title("📊 Data Analytics Dashboard")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Select columns
    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    # Sidebar Filters
    st.sidebar.header("Filters")

    if categorical_cols:

        filter_col = st.sidebar.selectbox(
            "Select Category Column",
            categorical_cols
        )

        values = st.sidebar.multiselect(
            "Select Values",
            df[filter_col].unique(),
            default=df[filter_col].unique()
        )

        filtered_df = df[
            df[filter_col].isin(values)
        ]

    else:
        filtered_df = df

    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # KPI Cards
    st.subheader("KPIs")

    col1, col2, col3 = st.columns(3)

    if numeric_cols:

        col1.metric(
            "Total Records",
            len(filtered_df)
        )

        col2.metric(
            "Total Sales",
            round(filtered_df[numeric_cols[0]].sum(), 2)
        )

        col3.metric(
            "Average Value",
            round(filtered_df[numeric_cols[0]].mean(), 2)
        )

    # Chart 1
    st.subheader("Bar Chart")

    if categorical_cols and numeric_cols:

        fig = px.bar(
            filtered_df,
            x=categorical_cols[0],
            y=numeric_cols[0],
            title="Category Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Chart 2
    st.subheader("Pie Chart")

    if categorical_cols:

        pie_df = (
            filtered_df[categorical_cols[0]]
            .value_counts()
            .reset_index()
        )

        pie_df.columns = ["Category", "Count"]

        fig2 = px.pie(
            pie_df,
            names="Category",
            values="Count"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # Chart 3
    st.subheader("Histogram")

    if numeric_cols:

        fig3 = px.histogram(
            filtered_df,
            x=numeric_cols[0]
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # Download Data
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        "Download Filtered Data",
        csv,
        "filtered_data.csv",
        "text/csv"
    )

else:
    st.info("Please upload a CSV file.")

=======
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Analytics Dashboard",
    layout="wide"
)

st.title("📊 Data Analytics Dashboard")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Select columns
    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    # Sidebar Filters
    st.sidebar.header("Filters")

    if categorical_cols:

        filter_col = st.sidebar.selectbox(
            "Select Category Column",
            categorical_cols
        )

        values = st.sidebar.multiselect(
            "Select Values",
            df[filter_col].unique(),
            default=df[filter_col].unique()
        )

        filtered_df = df[
            df[filter_col].isin(values)
        ]

    else:
        filtered_df = df

    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # KPI Cards
    st.subheader("KPIs")

    col1, col2, col3 = st.columns(3)

    if numeric_cols:

        col1.metric(
            "Total Records",
            len(filtered_df)
        )

        col2.metric(
            "Total Sales",
            round(filtered_df[numeric_cols[0]].sum(), 2)
        )

        col3.metric(
            "Average Value",
            round(filtered_df[numeric_cols[0]].mean(), 2)
        )

    # Chart 1
    st.subheader("Bar Chart")

    if categorical_cols and numeric_cols:

        fig = px.bar(
            filtered_df,
            x=categorical_cols[0],
            y=numeric_cols[0],
            title="Category Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Chart 2
    st.subheader("Pie Chart")

    if categorical_cols:

        pie_df = (
            filtered_df[categorical_cols[0]]
            .value_counts()
            .reset_index()
        )

        pie_df.columns = ["Category", "Count"]

        fig2 = px.pie(
            pie_df,
            names="Category",
            values="Count"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # Chart 3
    st.subheader("Histogram")

    if numeric_cols:

        fig3 = px.histogram(
            filtered_df,
            x=numeric_cols[0]
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # Download Data
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        "Download Filtered Data",
        csv,
        "filtered_data.csv",
        "text/csv"
    )

else:
    st.info("Please upload a CSV file.")

>>>>>>> 6442826c615e90312781ce7636378122ee1c4d54
