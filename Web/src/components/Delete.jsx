import app from '../firebase.js';
import { Button } from 'react-bootstrap';
import { getFirestore, doc, deleteDoc } from 'firebase/firestore/lite';
import { getAuth } from 'firebase/auth';

const Delete = () => {

    const auth = getAuth();
    const user = auth.currentUser;
    const email = user.email;

    function handleSubmit(e){
        e.preventDefault();

        deleteDoc(doc(getFirestore(app), "settings", email));

        alert('User deleted');
    }

    return (
        <>
        <div className="delete-container">
            <div style={{maxWidth: '550px'}}>
                <h2>Are you sure you want to delete?</h2>
                <br></br>
                <Button onClick={handleSubmit} className="w-100" type="submit" variant="dark">Delete</Button>
            </div>
        </div>
        </>
    )
}

export default Delete;
