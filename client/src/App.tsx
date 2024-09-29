import './App.css'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from './Dashboard/Dashboard.tsx';
import Login from './Login/Login.tsx';
import Signup from './Signup/Signup.tsx';
import FlashCard from './FlashCard/FlashCard.tsx';

interface FlashCardType {
  id: number;
  question: string;
  answer: string;
  options: string[];
}

// Define the sample flashcards using the FlashCardType
const def_sample_card: FlashCardType[] = [
  {
    id: 1,
    question: 'What does OOP stand for?',
    answer: 'Object Oriented Programming',
    options: [
      'Oopsie',
      'Object Oriented Programming',
      'One One Pain',
      'I do not know',
    ],
  },
  {
    id: 2,
    question: 'What are the 4 Principles of OOP?',
    answer: 'Abstraction, Encapsulation, Inheritance, Polymorphism',
    options: [
      'Classes, Methods, Constructors, Instances',
      'Ice cream, yogurt, cheese, burgers',
      'ints, doubles, strings, char',
      'Abstraction, Encapsulation, Inheritance, Polymorphism'
    ],
  },
  {
    id: 3,
    question: 'Is this code correct (y is an integer): double divide = (double) x / y',
    answer: 'Yes',
    options: [
      'Yes',
      'No'
    ],
  },
  {
    id: 4,
    question: 'Can you make your own data types with OOP languages such as Java?',
    answer: 'Yes, making objects by referencing classes',
    options: [
      'Yes, making objects by referencing classes',
      'No',
      'I do not know'
    ],
  },
  {
    id: 5,
    question: 'How many popular operating systems are in use today?',
    answer: '3: Windows, Apple, Linux',
    options: [
      '1: only Apple!',
      '2: Windows and Apple',
      '3: Windows, Apple, Linux'
    ],
  }
];

function App() {
  // const {user} = useAuthContext();
  
  return (
    <div className="App">
      <div>
        
      </div>
      <BrowserRouter>
        <Routes>
          <Route path="/Dashboard" element={<Dashboard/>} />
          <Route path='/FlashCards' element={<FlashCard flashcards={def_sample_card}/>} />
          <Route path="/Login" element={<Login/>} />
          <Route path = "/Signup" element={<Signup/>} />

        {/* When we have user */}

          {/* <Route path="/Dashboard" element={user ? <Dashboard/>: <Navigate to="/Dashboard"/>} />
          <Route path="/Login" element={user ? <Dashboard/>: <Navigate to="/Login"/>} /> */}

        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App
