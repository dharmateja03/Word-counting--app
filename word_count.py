import streamlit as st
# Function to read and update view count from a file
def get_view_count():
    try:
        with open("view_count.txt", "r") as f:
            view_count = int(f.read())
    except FileNotFoundError:
        view_count = 0  # Initialize to 0 if the file does not exist
    return view_count

def update_view_count(view_count):
    with open("view_count.txt", "w") as f:
        f.write(str(view_count))

# Get the current view count
# view_count = get_view_count()

# # Increment the view count
# view_count += 1

# Update the file with the new view count
# update_view_count(view_count)
# Function to count words
def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Streamlit app
def main():
    # Title
    st.title("Word Count App ")

    # Apply custom CSS to set the width of the text area and output box
    

    # Input box for text with fixed width
    st.subheader("Paste your text here:")
    input_text = st.text_area("Input Text", height=300)

    # If text is entered
    if input_text:
        # Count the words
        word_counts = count_words(input_text)
        
        # Sort the word count dictionary by frequency in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Display word count directly below the input text box in a boxed format
        st.subheader("Word Count Result:")
        st.markdown('<div class="output-box">', unsafe_allow_html=True)  # Boxed output start
        for word, count in sorted_word_counts:
            st.write(f"{word}: {count}")
        st.markdown('</div>', unsafe_allow_html=True)  # Boxed output end

        # Display summary below word count
        st.subheader("Summary:")
        st.write(f"Total unique words: {len(word_counts)}")
        st.write(f"Total words: {sum(word_counts.values())}")

if __name__ == "__main__":
    main()
