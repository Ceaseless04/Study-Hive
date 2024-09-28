import React from 'react';
import './Login.css'
import { FaUser, FaLock } from 'react-icons/fa';


import { FaBeer } from 'react-icons/fa';

class Question extends React.Component {
  render() {
    return <h3> Lets go for a <FaBeer />? </h3>
  }
}

const Login = () => {
  return (

    
    <div className='wrapper'> 
    <form action="">
      <h1>Login</h1>
      <div className="input-box">
          <input type="text" placeholder='Username' required/>
          
      </div>
      
      <div className="input-box">
          <input type="password" placeholder='Password' required/>
          


      </div>

      <div className="remember-forgotten">
        <label><input type="checkbox" />Remember me</label>
        <a href="#">Forgot password?</a>
      </div>

      <button type="submit">Login</button>

      <div className="register-link">

        <p>Do not have an account? <a href="#">Register</a></p>
      </div>
    </form>
    
    </div>
    
  )
}

export default Login
