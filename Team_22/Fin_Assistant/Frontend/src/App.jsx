
import React, { useEffect, useState } from 'react';
import Dashboard from './components/Dashboard.jsx';
import Chatbot from './components/Chatbot.jsx';
import Login from './components/Login.jsx';
import PDFUpload from './components/PDFUpload.jsx';
import Analytics from './components/Analytics.jsx';
import { api } from './components/api.js';

export default function App() {
  const [user, setUser] = useState(null);
  const [section, setSection] = useState('dashboard');

  useEffect(() => {
    const saved = localStorage.getItem('fa_user');
    if (saved) setUser(JSON.parse(saved));
  }, []);

  const onLogin = (u, token) => {
    setUser(u);
    localStorage.setItem('fa_user', JSON.stringify(u));
    localStorage.setItem('fa_token', token);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('fa_user');
    localStorage.removeItem('fa_token');
  };

  if (!user) return <Login onLogin={onLogin} />;

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="header-left"><h2>Fin Assistant</h2></div>
        <div className="header-right">
          <span className="welcome-message">Hi, {user.name}</span>
          <button className="btn btn--outline" onClick={logout}>Logout</button>
        </div>
      </header>

      <div className="app-body">
        <aside className="sidebar">
          <ul className="nav-menu">
            <li><a className={"nav-link " + (section==='dashboard'?'active':'')} onClick={() => setSection('dashboard')}>Dashboard</a></li>
            <li><a className={"nav-link " + (section==='reports'?'active':'')} onClick={() => setSection('reports')}>Reports</a></li>
            <li><a className={"nav-link " + (section==='budgets'?'active':'')} onClick={() => setSection('budgets')}>Budgets</a></li>
            <li><a className={"nav-link " + (section==='upload'?'active':'')} onClick={() => setSection('upload')}>Upload PDF</a></li>
            <li><a className={"nav-link " + (section==='analytics'?'active':'')} onClick={() => setSection('analytics')}>Analytics</a></li>
            <li><a className={"nav-link " + (section==='chat'?'active':'')} onClick={() => setSection('chat')}>Chatbot</a></li>
          </ul>
        </aside>

        <main className="main-content">
          {section === 'dashboard' && <Dashboard user={user} />}
          {section === 'chat' && <Chatbot user={user} />}
          {section === 'reports' && <Dashboard user={user} reportsOnly />}
          {section === 'budgets' && <Dashboard user={user} budgetsOnly />}
          {section === 'upload' && <PDFUpload user={user} />}
          {section === 'analytics' && <Analytics user={user} />}
        </main>
      </div>
    </div>
  );
}

