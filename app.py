import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Descriptive Statistics & Data Visualization")

# Upload file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"]) 

if uploaded_file is not None:
    # Read file
    df = pd.read_csv(uploaded_file)
    st.write("## Preview of the dataset:")
    st.write(df.head())
    
    # Descriptive statistics
    st.write("## Descriptive Statistics")
    st.write(df.describe())
    
    # Select numerical columns only
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_cols) > 0:
        st.write("## Data Visualization")
        
        # Histogram
        st.write("### 1. Histogram")
        selected_col = st.selectbox("Select column for histogram", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        st.pyplot(fig)
        
        # Boxplot
        st.write("### 2. Boxplot")
        selected_col_box = st.selectbox("Select column for boxplot", numeric_cols, key="boxplot")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_col_box], ax=ax)
        st.pyplot(fig)
        
        # Scatter Plot
        st.write("### 3. Scatter Plot")
        x_col = st.selectbox("Select X column", numeric_cols, key="scatter_x")
        y_col = st.selectbox("Select Y column", numeric_cols, key="scatter_y")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)
        
        # Line Plot
        st.write("### 4. Line Plot")
        selected_col_line = st.selectbox("Select column for line plot", numeric_cols, key="line")
        fig, ax = plt.subplots()
        ax.plot(df[selected_col_line])
        st.pyplot(fig)
        
        # Correlation Heatmap
        st.write("### 5. Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        # Population vs Sample Histogram
        st.write("### 6. Population vs Sample Histogram")
        sample_size = st.slider("Select sample size", min_value=1, max_value=len(df), value=int(len(df) * 0.1))
        sample_df = df.sample(sample_size, random_state=42)
        
        selected_col_pop_sample = st.selectbox("Select column for Population vs Sample Histogram", numeric_cols, key="pop_sample")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col_pop_sample], kde=True, color='blue', label='Population', ax=ax)
        sns.histplot(sample_df[selected_col_pop_sample], kde=True, color='red', label='Sample', ax=ax)
        ax.legend()
        st.pyplot(fig)


    else:
        st.warning("No numerical columns found in the dataset!")


