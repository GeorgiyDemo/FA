import React from 'react';
import ReactDOM from 'react-dom/client';
import './style.css';
import App1 from './App1';
import App2 from './App2';
import MyClicker from './click';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <App1 />
      <App2 />
      <MyClicker/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
