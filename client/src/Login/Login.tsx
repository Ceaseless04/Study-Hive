import './Login.css'
import { FaUser, FaLock } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import DashNavbar from '../Components/navbar';

const Login = () => {
  return (
  <div>
    <DashNavbar/>
    <div className='wrapper'> 
    
    <form action="">
      <h1>Login</h1>
      <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
        <span style={{ marginRight: '8px' }}>
          <FaUser />
        </span>
        <input type="text" placeholder="Username" required />
      </div>
      
      <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
          <span style={{ marginRight: '8px' }}>
            <FaLock />
          </span>
          <input type="password" placeholder='Password' required/>
          


      </div>

      <div className="remember-forgotten">
        <label><input type="checkbox" />Remember me</label>
        <a href="#">Forgot password?</a>
      </div>

      <button type="submit">Login</button>

      <div className="register-link">

        <p>Do not have an account? 
          <Link to="/Signup"> Register</Link>
          </p>
      </div>
    </form>
    
    </div>
    </div>
    
  )
}

export default Login
