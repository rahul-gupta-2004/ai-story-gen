# Import necessary libraries
import streamlit as st
import fetch_data  # Module to fetch data from API
import pandas as pd  # Library for data manipulation
import numpy as np  # Library for numerical operations

# Define the app function that handles the analytics page
def app():
    st.title('Story Frequency Analysis')  # Set the title of the page
    
    # Fetch the JSON data from the API
    json_data = fetch_data.fetch_json_data()  # Get story data in JSON format
    timestamps = fetch_data.get_timestamp(json_data)  # Extract list of timestamps
    
    # Extracting dates and times from timestamps
    dates = [timestamp.split(' ')[0] for timestamp in timestamps]  # Get only the date part
    times = [timestamp.split(' ')[1] for timestamp in timestamps]  # Get only the time part (hour)
    
    # Fetch story lengths from the API data
    story_len = fetch_data.get_story_len(json_data)

    # Create a DataFrame for easier data manipulation
    df = pd.DataFrame({'date': dates, 'time': times})

    # Calculate the frequency of stories per date
    date_counts = df['date'].value_counts().sort_index()  # Count and sort by date
    
    # Calculate the frequency of stories per hour
    time_counts = df['time'].value_counts().sort_index()  # Count and sort by time

    # Plotting the frequency of stories per date using a bar chart
    st.subheader('Frequency of Stories by Date')  # Subheader for date frequency
    st.bar_chart(date_counts)  # Display bar chart for date counts

    # Plotting the frequency of stories by hour using a bar chart
    st.subheader('Frequency of Stories by Hour')  # Subheader for time frequency
    st.bar_chart(time_counts)  # Display bar chart for time counts

    # Plotting the story length distribution with bins of 300
    st.subheader('Story Length Distribution')  # Subheader for story length distribution
    
    # Create bins for story lengths with a range increment of 300
    bins = np.arange(0, max(story_len) + 300, 300)  # Create bins from 0 to max length + 300

    # Use np.histogram to get the count of stories in each bin
    counts, bin_edges = np.histogram(story_len, bins=bins)

    # Create a DataFrame for plotting story length distribution
    story_length_df = pd.DataFrame({
        'Length Range': [f"{int(bin_edges[i])} - {int(bin_edges[i+1])}" for i in range(len(counts))],  # Label bins
        'Count': counts  # Story count in each bin
    })

    # Display a bar chart for story lengths grouped by bins
    st.bar_chart(story_length_df.set_index('Length Range'))  # Set index as length range for chart

# Run the app if this file is executed directly
if __name__ == "__main__":
    app()  # Call the app function to run the analytics page
