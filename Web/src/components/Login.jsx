import React, { useState } from 'react';
import { Form, Button, Alert } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom';
import { useUserAuth } from '../context/UserAuthContext.js';

const Login = () => {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const { logIn } = useUserAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            await logIn(email, password);
            navigate("/settings");
        } catch (err){
            setError("User not found");
        }
    }

    return (
    <div className="login-container">
        <Form className="login-form" onSubmit={handleSubmit}>
            <h1 style={{fontWeight: "bold"}}>Log In</h1>
            {error && <Alert variant="danger">{error}</Alert>}
            <br></br>
            <Form.Control
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            ></Form.Control>
            <br></br>
            <Form.Control
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            ></Form.Control>
            <br></br>
            <Button variant="dark" type="submit">Log In</Button>
        </Form>
        {/* <div className="lines">
                <div className="vl"></div>
                <br></br>
                <div>
                    OR
                </div>
                <br></br>
                <div className="vl"></div>
        </div>
        <GoogleButton onClick={handleClick}></GoogleButton> */}
    </div>
    )
}

export default Login;