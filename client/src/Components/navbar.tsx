import { Link } from "react-router-dom";
import "./navbar.css";
import { SlHome } from "react-icons/sl";
import { HiOutlineSquares2X2 } from "react-icons/hi2";
import { AiOutlineFileText } from "react-icons/ai";
import { BsChatLeft, BsPerson } from "react-icons/bs";
import { CiSettings } from "react-icons/ci";
import { FC } from "react";

const DashNavbar: FC = () => {
  return (
    <nav className="dashboard-navbar">
      <table className="navbar-table">
        <tbody>
          <tr className="click navbar-item click icon">
            <td>
              <SlHome
                color="white"
                size={"2em"}
              />
            </td>
            <td>
              <Link to="/Dashboard" className="link navbar-item click">
                Dashboard
              </Link>
            </td>
          </tr>
          <tr className="click navbar-item click icon find-icon">
            <td>
              <HiOutlineSquares2X2
                size={"2em"}
              />
            </td>
            <td>
              <Link to="/Flashcards" className="link navbar-item click">
                Flashcards
              </Link>
            </td>
          </tr>
          <tr className="click navbar-item click icon">
            <td>
              <AiOutlineFileText
                size={"2em"}
              />
            </td>
            <td>
            <Link to="/Chatbot" className="link navbar-item click">
                Chatbot
              </Link>
            </td>
          </tr>
          <tr className="click navbar-item click icon resources-icon">
            <td>
              <BsChatLeft
                size={"2em"}
              />
            </td>
            <td>
              <Link to="/Community" className="link navbar-item click">
               Community 
              </Link>
            </td>
          </tr>
          <tr className="click navbar-item click icon">
            <td>
              <BsPerson
                size={"2em"}
              />
            </td>
            <td>
              <Link to="/" className="link navbar-item click">
                Profile
              </Link>
            </td>
          </tr>
          <tr className="click navbar-item click icon settings-icon">
            <td>
              <CiSettings
                size={"2em"}
              />
            </td>
            <td>
              <Link to="/Settings" className="link navbar-item click">
                Settings
              </Link>
            </td>
          </tr>
        </tbody>
      </table>
    </nav>
  );
};

export default DashNavbar;
