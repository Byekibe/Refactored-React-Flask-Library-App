import { useContext } from "react";
import { BookContext } from "../context/BookContext.jsx";
import Spinner from "./Spinner.jsx";
import AllBooksTable from "./tables/AllBooksTable.jsx";

const AllBooks = () => {
    const allBooks = useContext(BookContext);

    return (
        <>
            {
                typeof(allBooks.allBooks) === "undefined" ? <Spinner /> : (
                    <AllBooksTable books={allBooks.allBooks.data} />
                )
            }
        </>
    );
};

export default AllBooks;