import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return None
        return df
    return None

# Initialize the app
def main():
    st.title('Data Visualization and Analysis App')

    # File uploader
    uploaded_file = st.file_uploader("Choose a file (CSV format)")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            # Display the dataframe
            if st.checkbox('Show dataframe'):
                st.write(df)
            
            # Show descriptive statistics
            if st.checkbox('Show Descriptive Statistics'):
                st.subheader("Descriptive Statistics")
                st.write(df.describe())

            # Sidebar for choosing the plot type
            plot_type = st.sidebar.selectbox("Choose the type of plot", 
                                             ["Histogram", "Line Plot", "Bar Plot", "Box Plot", "Scatter Plot"])
            
            # Get the list of columns
            columns = df.columns.tolist()
            
            # Choose the column to plot
            selected_column = st.sidebar.selectbox("Select the column to plot", columns)

            if plot_type == "Histogram":
                # Display histogram
                st.subheader(f"Histogram of {selected_column}")
                plt.figure(figsize=(10,4))
                plt.hist(df[selected_column].dropna(), bins=30)
                plt.xlabel(selected_column)
                plt.ylabel("Count")
                st.pyplot(plt)
                
            elif plot_type == "Line Plot":
                # Display line plot
                st.subheader(f"Line Plot of {selected_column}")
                plt.figure(figsize=(10,4))
                plt.plot(df[selected_column].dropna())
                plt.xlabel("Index")
                plt.ylabel(selected_column)
                st.pyplot(plt)
                
            elif plot_type == "Bar Plot":
                # Display bar plot
                st.subheader(f"Bar Plot of {selected_column}")
                plt.figure(figsize=(10,4))
                plt.bar(df.index, df[selected_column].dropna())
                plt.xlabel("Index")
                plt.ylabel(selected_column)
                st.pyplot(plt)
                
            elif plot_type == "Box Plot":
                # Display box plot
                st.subheader(f"Box Plot of {selected_column}")
                sns.boxplot(df[selected_column].dropna())
                st.pyplot(plt)
                
            elif plot_type == "Scatter Plot":
                # Display scatter plot
                st.subheader("Scatter Plot")
                x_axis = st.sidebar.selectbox("Choose the X-axis", columns, index=0)
                y_axis = st.sidebar.selectbox("Choose the Y-axis", columns, index=1)
                plt.figure(figsize=(10,4))
                sns.scatterplot(x=df[x_axis], y=df[y_axis])
                st.pyplot(plt)
                
if __name__ == "__main__":
    main()
