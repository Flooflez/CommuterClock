import React from 'react'
import { Form, Button, Card, Alert } from 'react-bootstrap'
import './index.js';

export default function Settings() {

    async function handleSubmit(){

    }
    
    return (
    <Card>
        <Card.Body>
        <div className="App">
            <div className="container">
                <h1>Settings</h1>
                <Form id="form" onSubmit={handleSubmit}> 
                    <label>Username</label>
                    <input type="text" placeholder="Username" id="user"></input>
                    <br></br>
                    <label>Starting Point</label>
                    <input type="text" placeholder="Starting Point" id="start"></input>
                    <br></br>
                    <label>Destination</label>
                    <input type="text" placeholder="Destination" id="end"></input>
                    <br></br>
                    <label>Start Time</label>
                    <input type="time" id="start_time"></input>
                    <br></br>
                    <label>End Time</label>
                    <input type="time" id="end_time"></input>
                    <br></br>
                    <label>Wait Time</label>
                    <input type="number" placeholder="Wait Time" min="1" id="wait_time"></input>
                    <br></br>
                </Form>
            </div>
        </div>
        </Card.Body>
    </Card>
    )
}
