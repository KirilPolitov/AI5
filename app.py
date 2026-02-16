import streamlit as st

books = [
  "Joe Mama",
  "Mein Kampf",
  "To catch a predator"
  "Tequitla"]
st.title("Book Checker App")
st.write("enter a book title to check if it exists in the database.")
userInput = st.text_input("Book Title")
if st.button("Check Book"):
  if userInput.strip() == "":
    st.warning("Please enter title")
  elif userInput in books:
    st.success("The book exists")
  else:
    st.error("THE BOOK DOESNT EXIST IDIOT!!!")
    newBook = st.text_input("Add book")
    books.append(newBook)
