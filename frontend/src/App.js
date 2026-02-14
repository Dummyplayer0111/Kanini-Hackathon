import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NurseDashboard from "./pages/NurseDashboard";
import DoctorDashboard from "./pages/DoctorDashboard";
import Home from "./pages/Home";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/nurse" element={<NurseDashboard />} />
        <Route path="/doctor" element={<DoctorDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
