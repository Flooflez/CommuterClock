import { HashRouter, Routes, Route } from 'react-router-dom';
import Add from './Add.jsx';
import Delete from './Delete.jsx';
import Update from './Update.jsx';
import Settings from './Settings.jsx';
import Signup from './Signup.jsx';
import Login from './Login.jsx';
import Home from './Home.jsx';
import { UserAuthContextProvider } from '../context/UserAuthContext.js';
import '../styles/styles.css';
import PrivateRoute from './PrivateRoute.jsx';
import About from './About.jsx';
import View from './View.jsx';

function App() {
  return (
    <div className="box" style={{fontFamily: "ptsans"}}>
        <div>
          <HashRouter>
            <UserAuthContextProvider>
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/settings" element={
                <PrivateRoute>
                  <Settings />
                </PrivateRoute>
              } 
              />
                <Route path="/add" element={<Add />} />
                <Route path="/delete" element={<Delete />} />
                <Route path="/update" element={<Update />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/about" element={<About />} />
                <Route path="/view" element={<View />} />
              </Routes>
            </UserAuthContextProvider>
          </HashRouter>
          </div>
      </div>
  );
}

export default App;


