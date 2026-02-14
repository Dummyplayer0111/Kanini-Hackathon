import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import NurseDashboard from "./pages/NurseDashboard";
import DoctorDashboard from "./pages/DoctorDashboard";
import EmergencyCases from "./pages/EmergencyCases";
import Inpatients from "./pages/Inpatients";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/nurse" element={<NurseDashboard />} />
        <Route path="/nurse/emergency" element={<EmergencyCases />} />
        <Route path="/nurse/inpatients" element={<Inpatients />} />
        <Route path="/doctor" element={<DoctorDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
