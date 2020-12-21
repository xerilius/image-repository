import React, { useState, useEffect } from 'react';
import { BrowserRouter, Switch,Route, Link } from 'react-router-dom';
import './App.css';

export default function App() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    fetch('/api/time')
    .then(res => res.json())
    .then(data => setTime(data.time))
  }, [])

  return (
    <BrowserRouter>
    <Switch>
      <Route exact path="/">
        <div> 
          hi
        </div>
      </Route>
   
      <Route path="/api/time">
        {time}
      </Route>
    </Switch>
    </BrowserRouter>

  );
}


