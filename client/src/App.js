import React, { useState } from 'react';
import Login from 'login.js';
import CreateAccount from 'create-account.js'; 


function App() {
  return (
    <div className = "App">
      <Login />
      <CreateAccount />
    </div>
  );
}
export default App;
