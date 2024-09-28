import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from './Dashboard/Dashboard.tsx';
import Login from './Login/Login.tsx';
import { Navigate } from "react-router-dom"; // will use when we have user

function App() {
  // const {user} = useAuthContext();
  
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/Dashboard" element={<Dashboard/>} />
          <Route path="/Login" element={<Login/>} />

        {/* When we have user */}

          {/* <Route path="/Dashboard" element={user ? <Dashboard/>: <Navigate to="/Dashboard"/>} />
          <Route path="/Login" element={user ? <Dashboard/>: <Navigate to="/Login"/>} /> */}

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App
