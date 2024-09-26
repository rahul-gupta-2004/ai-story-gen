from datetime import datetime

# Function to fetch the current timestamp
def fetch_timestamp():

    # Get the current date and time
    current_datetime = datetime.now()

    # Format the timestamp to 'dd/mm/yyyy hh:mm AM/PM'
    formatted_timestamp = current_datetime.strftime('%d/%m/%Y %I:%M %p')

    # Return the formatted timestamp
    return formatted_timestamp
