import streamlit as st

books = [
  #"Joe Mama",
  #"Mein Kampf",
  #"To catch a predator"
  #"Tequitla"
  
]
st.title("Library App")
st.write("enter a book title to check if it exists in the database.")
userInput = st.text_input("Book Title")
if st.button("Check Book"):
  if userInput.strip() == "":
    st.warning("Please enter title")
  elif userInput in books:
    st.success("The book exists")
  else:
    st.error("THE BOOK DOESNT EXIST IDIOT!!!")
    title = st.text_input("Enter title")
    author = st.text_input("Enter author")
    price = st.number_input("Enter price")
    if st.button("Confirm"):
      book = {
        "title": title,
        "author": author,
        "price": price
      }
      st.session_state.books.append(book)
      st.success("Added")
      
