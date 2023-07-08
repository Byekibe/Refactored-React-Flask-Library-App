import { createContext, useEffect, useState } from "react";

const BookContext = createContext();

const BookContextProvider = ({ children }) => {
    const [allBooks, setAllBooks] = useState()

    const url = "http://localhost:7001/data"
    useEffect(() => {
        const fetchAllBooks = async () => {
            const response = await fetch(url);
            const data = await response.json();

            setAllBooks(data)
        }

        fetchAllBooks()
    }, []);

    const values = {
        allBooks
    }

    return (
        <BookContext.Provider value={values}>
            {children}
        </BookContext.Provider>
    )
}

export {BookContext, BookContextProvider }