import openai

# Function to summarize business emails using OpenAI

def summarize_email(email_content):
    """
    Summarizes the provided email content using OpenAI's API.

    Args:
        email_content (str): The content of the email to be summarized.

    Returns:
        str: A summary of the email content.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes emails."},
            {"role": "user", "content": email_content}
        ],
        max_tokens=100
    )
    summary = response.choices[0].message['content']
    return summary


# Example usage
if __name__ == '__main__':
    email = "Dear team,\n\nI wanted to remind you about the meeting scheduled for tomorrow at 10 AM. Please ensure that you have all the necessary documents prepared.\n\nBest regards,\nJohn"
    print("Summary:", summarize_email(email))