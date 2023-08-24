import React, { useState } from 'react';
import { getAuth } from 'firebase/auth';
import app from '../firebase.js';
import { getFirestore, getDoc, doc } from 'firebase/firestore/lite';
import { Card } from 'react-bootstrap';

const View = () => {

    const auth = getAuth();
    const user = auth.currentUser;
    const [ origin, setOrigin ] = useState("");
    const [ dest, setDest ] = useState("");
    const [ startTime, setStartTime ] = useState("");
    const [ endTime, setEndTime ] = useState("");
    const [ wantCar, setWantCar ] = useState("");

    getDoc(doc(getFirestore(app), "settings", user.email)).then(docSnap => {
        let data = docSnap.data();
        setOrigin(data.origin);
        setDest(data.destination);
        setStartTime(data.start_hour);
        setEndTime(data.end_hour);
        setWantCar(String(data.should_consider_car));
    })

    return (
        <div className="view-container">
            <h1>Your Settings</h1>
            <Card border="dark" style={{maxWidth: "500px"}}>
                <Card.Body>
                    <h3>Origin: {origin}</h3>
                    <h3>Destination: {dest}</h3>
                    <h3>Start Time: {startTime}</h3>
                    <h3>End Time: {endTime}</h3>
                    <h3>Should Consider Car: {wantCar}</h3>
                </Card.Body>
            </Card>
        </div>
    )
}

export default View;
