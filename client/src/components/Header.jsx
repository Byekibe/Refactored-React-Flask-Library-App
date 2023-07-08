const Header = () => {
    return (
        <>
        <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container">
            <a className="navbar-brand" href="#">Navbar</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li className="nav-item">
                <a className="nav-link" href="#">Features</a>
                </li>
                <li className="nav-item">
                <a className="nav-link" href="#">Pricing</a>
                </li>
                <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Categories
                </a>
                <ul className="dropdown-menu">
                    <li><a className="dropdown-item" href="#">Science</a></li>
                    <li><a className="dropdown-item" href="#">History</a></li>
                    <li><a className="dropdown-item" href="#">Geography</a></li>
                    <li><a className="dropdown-item" href="#">Romance</a></li>
                </ul>
                </li>
            </ul>
            </div>
        </div>
        </nav>
        </>
    );
};

export default Header;