import React, { useRef, useState } from 'react'
import db from '../firebase.js'
import { Link } from 'react-router-dom'
import { Form, Button, Card, Alert } from 'react-bootstrap'
import { doc, deleteDoc } from 'firebase/firestore/lite';

export default function Delete() {

    const userRef = useRef()

    function handleSubmit(e){
        e.preventDefault()

        deleteDoc(doc(db, "settings", userRef.current.value));

        e.target.reset()

    }

    return (
        <>
            <Card>
                <Card.Body>
                <Form onSubmit={handleSubmit}> 
                    <Form.Group id="user">
                        <Form.Label>Username</Form.Label>
                            <Form.Control type="text" ref={userRef} required></Form.Control>
                    </Form.Group>
                    <Button size="sm" className="w-100" type="submit">Delete</Button>
                </Form>
                </Card.Body>
            </Card>
            <div className="w-100 text-center mt-2">
                Want to add a setting? <Link to="/">Add Setting</Link>
            </div>
        </>
    )
}
