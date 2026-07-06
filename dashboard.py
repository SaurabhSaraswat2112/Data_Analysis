import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="Employee Data Dashboard", layout="wide")

st.title("📊 Employee Data Cleaning & Visualization Dashboard")

# Load Dataset
df = pd.read_csv("cleaned_data.csv")

# Show Dataset
if st.checkbox("Show Dataset"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filters")
department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

filtered_df = df[df["Department"].isin(department)]

# Metrics
st.subheader("Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Employees", len(filtered_df))
col2.metric("Average Salary", f"{filtered_df['Salary'].mean():,.0f}")
col3.metric("Average Performance", f"{filtered_df['Performance'].mean():.1f}")

# Histogram
st.subheader("Salary Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df["Salary"], bins=10, color="skyblue", edgecolor="black")
ax.set_xlabel("Salary")
ax.set_ylabel("Count")
st.pyplot(fig)

# Department Count
st.subheader("Employees by Department")

dept = filtered_df["Department"].value_counts()

fig2, ax2 = plt.subplots()
dept.plot(kind="bar", color="orange", ax=ax2)
ax2.set_xlabel("Department")
ax2.set_ylabel("Employees")
st.pyplot(fig2)

# Scatter Plot
st.subheader("Experience vs Salary")

fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Experience"], filtered_df["Salary"], color="green")
ax3.set_xlabel("Experience (Years)")
ax3.set_ylabel("Salary")
st.pyplot(fig3)

# Box Plot
st.subheader("Salary Box Plot")

fig4, ax4 = plt.subplots()
ax4.boxplot(filtered_df["Salary"])
ax4.set_ylabel("Salary")
st.pyplot(fig4)

# Data Summary
st.subheader("Statistical Summary")
st.write(filtered_df.describe())