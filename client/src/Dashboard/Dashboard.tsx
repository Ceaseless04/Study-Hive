import './Dashboard.css'
import 'react-icons/fa';
import DashNavbar from '../Components/navbar';


const Dashboard = () => {
  return (
    <div className='page_container'>
        <div>
            <h1 data-shadow='Welcome to Study Hive'>Welcome to Study Hive</h1>
            <DashNavbar/>
        </div>

    </div>
    
  )
}

export default Dashboard
