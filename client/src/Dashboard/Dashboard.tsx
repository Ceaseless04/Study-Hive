<<<<<<< HEAD
import 'react-icons/fa';
import DashNavbar from '../Components/navbar';
import './Dashboard.css';

const Dashboard = () => {
  // Define the type for a single card


  return (
    <div className='page_container'>
        <div className='content'>
            <DashNavbar/>

            
        </div>

    </div>
    
  )
}

export default Dashboard
=======
import 'react-icons/fa';
import DashNavbar from '../Components/navbar';
import { Link } from 'react-router-dom';

import './Dashboard.css';

const Dashboard = () => {
  // Define the type for a single card


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
    <div className='page_container'>
        <div className='content'>
            <DashNavbar/>

            
        </div>

    </div>
    
  )
}

export default Dashboard
>>>>>>> 840af689db5b1e0402f97148a2dd526649e53137
