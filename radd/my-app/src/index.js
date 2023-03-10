import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App.js';
import { initializeApp } from 'firebase/app';
import 'bootstrap/dist/css/bootstrap.min.css'
import { getFirestore, collection, getDocs, deleteDoc, setDoc, doc} from 'firebase/firestore/lite';

const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
  authDomain: process.env.REACT_APP_AUTH_DOMAIN,
  projectId: process.env.REACT_APP_PROJECT_ID,
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.REACT_APP_FIREBASE_APP_ID
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const settingsCol = collection(db, 'settings');

function SubmitButton(){

  function submit(e) {
    var user = document.getElementById('user').value;
    var start = document.getElementById('start').value;
    var end = document.getElementById('end').value;
    var start_time = document.getElementById('start_time').value;
    var end_time = document.getElementById('end_time').value;
    var wait_time = document.getElementById('wait_time').value;

    setDoc(doc(db, "settings", user), {
      destination: end,
      end_hour: end_time,
      origin: start,
      start_hour: start_time,
      wait_seconds: wait_time
    });
        alert('User added');

    document.getElementById('form').reset();
    
  }

  return (
    <div style={{ display: "flex", justifyContent:'center',}}>
    <button className='submit' type="submit" onClick={submit}>Submit</button>
    </div>
  );
  }

function DeleteButton(){
  function deleteField(e){
    var user = document.getElementById('user').value;

    deleteDoc(doc(db, "settings", user));

    document.getElementById('form').reset();
  }

  return (
    <div style={{ display: "flex", justifyContent:'center',}}>
    <button className='update' type="submit" onClick={deleteField}>Delete</button>
    </div>
  )
}

getDocs(settingsCol)
    .then((snapshot) => {
        let users = []

        snapshot.docs.forEach((doc) => {
            users.push({ ...doc.data(), id: doc.id})
        })
        console.log(users);
    });

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<React.StrictMode>
  <App />
  <SubmitButton />
  <DeleteButton />
</React.StrictMode>);