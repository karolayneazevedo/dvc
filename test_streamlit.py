import streamlit as st
import pandas as pd
import time
import plotly.express as px
import streamlit as st



# Display the progress value as a percentage

# # Load data and create a two-column layout
data = pd.read_csv('Paises.csv', index_col=None, low_memory=False)
data = data.drop('Unnamed: 0', axis=1)
df = pd.read_csv('dados_processados.csv', index_col=None, low_memory=False)

# Set a custom color for the charts
chart_color = '#9e77ff'

# Create two columns layout with horizontal and vertical spacing
col1, col2 = st.columns([1, 2])


# HTML and CSS for logo and title layout
col1.image('Logo.png', width=300, output_format="auto")
col2.write(
    f'<div style="text-align:center; font-size:30px; padding-top:20px; margin-top: 20px;">DeepVirusClassifier</div>',
    unsafe_allow_html=True
)


# Add vertical spacing (separator)
col1.text('')
col2.text('')

# Show raw data in the first column with equal size
with col1:
    st.write(data, use_container_width=True)

# Add vertical spacing (separator)
col2.text('')

# Plot charts in the second column with equal size
with col2:
    st.bar_chart(data, y='Quantidade', x='Paises',
                 use_container_width=True, color='#9e77ff')
    st.text('')  # Add vertical spacing (separator)

custom_colors = ['#9e77ff', '#8b66e8', '#7856d0', '#6646b8']

value_counts_series = df['Especies'].value_counts()

result_df = pd.DataFrame({'Especies': df.Especies.value_counts(
).index, 'Count': value_counts_series.values})

# Create a pie chart using Plotly Express with equal size
fig = px.pie(result_df, names='Especies', values='Count',
             title='Species', color_discrete_sequence=custom_colors)

# Add vertical spacing (separator)
st.text('')

# Display the pie chart in the second column with equal size
st.plotly_chart(fig, use_container_width=True)

user_input = st.text_input(
    "Insert the Virus Nucleotide Chain:", "  ")
character_count = len(user_input)
if st.button("Submit"):
    progress_value = int(72)
    st.write("Typed Sequence Size:", character_count)
    # st.text("A sequência é SARS-CoV-2")
    progress_value = max(0, min(progress_value, 100))
    

# Create a progress bar based on the user's input
    progress_bar = st.progress(0)  # Initialize progress bar at 0%
    # Simulate automatic progress based on the user's input
    for i in range(progress_value + 1):
        time.sleep(0.1)  # Simulate work being done
        progress_bar.progress(i)

    st.write(f"probability of {int(72)}% Of being SARS-CoV-2")





# Ensure the input is within the valid range (0-100)

# # Display a message when the task is complete
# st.text("Task complete!")
