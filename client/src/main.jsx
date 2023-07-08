import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';
import { BrowserRouter as Router } from 'react-router-dom';
import { BookContextProvider } from './context/BookContext.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
<BookContextProvider>
    <Router>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </Router>
</BookContextProvider>,
)
