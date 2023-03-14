import React, { useRef, useState } from 'react'
import db from '../firebase.js';
import { Form, Button, Card, Alert } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { setDoc, doc} from 'firebase/firestore/lite';

export default function Settings() {

    const userRef = useRef()
    const startPtRef = useRef()
    const destRef = useRef()
    const startTimeRef = useRef()
    const endTimeRef = useRef()
    const waitTimeRef = useRef()

    function handleSubmit(e) {

        e.preventDefault()

        setDoc(doc(db, "settings", userRef.current.value), {
            destination: destRef.current.value,
            end_hour: endTimeRef.current.value,
            origin: startPtRef.current.value,
            start_hour: startTimeRef.current.value,
            wait_seconds: waitTimeRef.current.value
        });
            alert('User added');

        e.target.reset()
        
    }
    
    return (
    <>
        <Card>
            <Card.Body>
                <h1 className="text-center mb-4">Settings</h1>
                    <Form id="form" onSubmit={handleSubmit}> 
                        <Form.Group id="user">
                            <Form.Label>Username</Form.Label>
                            <Form.Control type="text" ref={userRef} required></Form.Control>
                        </Form.Group>
                        <Form.Group id="start">
                            <Form.Label>Starting Point</Form.Label>
                            <Form.Control type="text" ref={startPtRef} required></Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Destination</Form.Label>
                            <Form.Control id="end" type="text" ref={destRef}required></Form.Control>
                        </Form.Group>
                        <Form.Group >
                            <Form.Label>Start Time</Form.Label>
                            <Form.Control id="start_time" type="time" ref={startTimeRef} required></Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>End Time</Form.Label>
                            <Form.Control id="end_time" type="time" ref={endTimeRef} required></Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Wait Time</Form.Label>
                            <Form.Control id="wait_time" type="number" ref={waitTimeRef}required></Form.Control>
                        </Form.Group>
                        <Form.Group>
                            <Form.Label>Car</Form.Label>
                            <Form.Check></Form.Check>
                        </Form.Group>
                        <br></br>
                        <Button className="w-100" type="submit">Submit</Button>
                    </Form>
            </Card.Body>
        </Card>
        <div className="w-100 text-center mt-2">
            Want to delete your settings? <Link to="/delete">Delete</Link>
        </div>

    </>
    
    )
}
