import React, { useState } from 'react'; 


function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); 

    const payload = { username, password }

    console.log("payload being sent: ", payload);
    // send our post request
    fetch("http://127.0.0.1:5000/api/create-account", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.message) {
        setMessage(data.message);
      } else if (data.error) {
        setMessage(data.error);
      }
    })
    .catch((error) => console.error("Error:", error));
  };


  return (
    <div className="App">
      <h1>Create Account</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={username} 
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter username"
        />
        <input 
          type="password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Enter password"
        />
        <button type="submit">Create Account</button> 
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
export default App;
