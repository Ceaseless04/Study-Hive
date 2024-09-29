import './Signup.css'
import { Link } from 'react-router-dom'
const Signup = () => {
    return (
  
      
      <div className='wrapper'> 
      <form action="">
        <h1>Register</h1>
        <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
          <span style={{ marginRight: '8px' }}>
            {/* <FaUser /> */}
          </span>
          <input type="text" placeholder="Username" required />
        </div>
        
        <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
            <span style={{ marginRight: '8px' }}>
              {/* <FaLock /> */}
            </span>
            <input type="text" placeholder='Email' required/>
        </div>

        <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
            <span style={{ marginRight: '8px' }}>
              {/* <FaLock /> */}
            </span>
            <input type="password" placeholder='Password' required/>

        </div>

        <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
            <span style={{ marginRight: '8px' }}>
              {/* <FaLock /> */}
            </span>
            <input type="text" placeholder='University' required/>

        </div>

        <div className="input-box" style={{ display: 'flex', alignItems: 'center' }}>
            <span style={{ marginRight: '8px' }}>
              {/* <FaLock /> */}
            </span>
            <input type="text" placeholder='Courses EX: COP1234, CEN5678' required/>

        </div>
  
        <div className="remember-forgotten">
          <label><input type="checkbox" />Remember me</label>
          
        </div>
  
        <button type="submit">Register</button>
  
        <div className="register-link">
  
          <p>Already have an account? 
            <Link to="/login"> Log In</Link></p>
        </div>
      </form>
      
      </div>
      
    )
  }
  
  export default Signup
  