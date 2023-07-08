const AllBooksTable = ({ books }) => {
    return (
        <>
        <div className="table-responsive container">
            <table className="table table-striped table-bordered align-middle">
            <thead className="table-light">
                <tr>
                <th scope="col">#</th>
                <th scope="col">Title</th>
                <th scope="col">Author</th>
                <th scope="col">Price</th>
                <th scope="col">Pages</th>
                <th scope="col">Category</th>
                <th scope="col">Contact</th>
                </tr>
            </thead>
            <tbody>
                {
                    books.map(book => (
                        <tr key={crypto.randomUUID()}>
                            <th scope="row"></th>
                            <td>{book[1]}</td>
                            <td>{book[2]}</td>
                            <td>{book[3]}</td>
                            <td>{book[4]}</td>
                            <td>{book[5]}</td>
                            <td>{book[6]}</td>
                        </tr>
                    ))
                }
            </tbody>
            </table>
        </div>
        </>
    );
};

export default AllBooksTable;