import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button, Alert } from 'react-bootstrap';
import { useUserAuth } from "../context/UserAuthContext";

const Signup = () => {

    // const provider = new GoogleAuthProvider();
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const { signUp } = useUserAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        try{
            await signUp(email, password);
            navigate("/settings");
        } catch (err){
            setError(err.message);
        }
    }

    return (
        <>
        
        <div className="sign-up-container">
        <h1 style={{fontWeight: "bold"}}>Create Account</h1>
        {error && <Alert variant="danger">{error}</Alert>}
        <br></br>
            <Form className="sign-up-form" onSubmit={handleSubmit}>
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
                <Button variant="dark" type="submit">Sign Up</Button>
            </Form>
        </div>
        </>
    )
}

export default Signup;
