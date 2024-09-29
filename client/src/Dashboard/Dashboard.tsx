import './Dashboard.css'
import 'react-icons/fa';
import DashNavbar from '../Components/navbar';
import { Link } from 'react-router-dom';


const Dashboard = () => {
  return (
    <div className='home-page'>
        <DashNavbar/>

        <div>
            <h1>Welcome to Study Hive</h1>
        </div>

        <div className="intro">
            <h2 id="title">Your AI Study Companion and Helper</h2>
            <p id="description">
            Have Flashcard decks based on your university <br/>
            and class in seconds. Save them and jump to Studying!
            </p>
            <Link to="/Signup" className="link">
              <button className="sign-up-button">
                <span>Start my Journey</span>
              </button>
            </Link>
        </div>

    </div>
    
  )
}

export default Dashboard
