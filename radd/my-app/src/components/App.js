import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container } from 'react-bootstrap'
import Delete from './Delete.js'
import Settings from './Settings.js'

function App() {
  return (
    <Container
    className="d-flex align-items-center justify-content-center"
    style={{ minHeight: "100vh" }}
    >
      <div className="w-100" style={{ maxWidth: "500px" }}> 
      <Router>
        <Routes>
          <Route exact path="/" element={<Settings />} />
          <Route path="/delete" element={<Delete />} />
        </Routes>
      </Router>
      </div>
    </Container>
  );
}

export default App;
