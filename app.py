import streamlit as st

st.title("Приложение")

# Създаваме списък, ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# + Добавяне на книга
st.header("+ Добави книга")

title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

# Покажи всички книги
if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("-----")

        # намиране на най-евтината книга
        cheapest_book = min(st.session_state.books, key=lambda x: x["price"])

        st.subheader("📉 Най-евтината книга")
        st.write("Заглавие:", cheapest_book["title"])
        st.write("Автор:", cheapest_book["author"])
        st.write("Цена:", cheapest_book["price"])

# Търсене по автор
st.header("Търсене по автор")

search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):
    found = False

    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write("Заглавие:", book["title"])
            st.write("Цена:", book["price"])
            st.write("-----")
            found = True

    if not found:
        st.write("Няма намерени книги от този автор.")
