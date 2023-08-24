import { Button } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const Settings = () => {

    const navigate = useNavigate();

    function goAdd(e){
        e.preventDefault();
        navigate('/add');
    }

    function goUpdate(e){
        e.preventDefault();
        navigate('/update');
    }

    function goDelete(e){
        e.preventDefault();
        navigate('/delete');
    }

    function goView(e){
        e.preventDefault();
        navigate('/view');
    }

    return (
        <>
        <div className="settings-container">
            <div className="settings-buttons">
                <h1>Settings</h1>
                <br></br>
                <Button onClick={goAdd} variant="dark">Add Settings</Button>
                <br></br>
                <Button onClick={goUpdate} variant="dark">Update Settings</Button>
                <br></br>
                <Button onClick={goDelete} variant="dark">Delete Settings</Button>
                <br></br>
                <Button onClick={goView} variant="info">View Settings</Button>
            </div>
        </div>
        </>

    )
}

export default Settings;



