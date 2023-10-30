import React from 'react';
import { Button } from 'react-bootstrap';
import { useNavigate, Link } from 'react-router-dom';
import vid from '../assets/video/train.mov';

const Home = () => {

    const navigate = useNavigate();

    function login(e){
        e.preventDefault();
        navigate("/login");
    }

    function signup(e){
        e.preventDefault();
        navigate("/signup");
    }
    
    return (
        <>
            <div className="cont">
                <div className="header">
                    <div className="left">
                        <h1 className="company" style={{fontFamily: "nanum", fontSize: "50px"}}>Commuter Clock</h1>
                    </div>
                    <div className="center">
                        <Link to="/about" style={{color: "black", fontWeight: "bold", fontSize: "25px"}}>About Us</Link>
                    </div>
                    <div className="right">
                        <Button className="login" variant="dark" onClick={login}>Login</Button>
                        <Button variant="dark" onClick={signup}>Sign Up</Button>
                    </div>
                </div>
                <div className="video">
                    <iframe title="product_ad" width="600" height="400" 
                    src="https://www.youtube.com/embed/1_z6RN1Q_qg?si=bfZ5kGbjLsBnudlc"></iframe>
                </div>
                <div className="mission-container">
                    <h4 style={{ fontWeight: "bold", marginTop: "4rem"}}>Our Mission</h4>
                    <h2 style={{ marginBottom: "4rem" }}>Empowering people to use transportation more efficiently and sustainably</h2>
                </div>
                <br></br>
                <br></br>
                <div>
                </div>
            </div>
        </>
    )
}

export default Home;
