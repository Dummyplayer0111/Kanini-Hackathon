import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function DoctorDashboard() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Protect route
  useEffect(() => {
    fetch("http://192.168.18.207:8000/api/user-role/", {
      credentials: "include",
    })
      .then(res => {
        if (!res.ok) navigate("/");
        return res.json();
      })
      .then(roleData => {
        if (roleData.role !== "doctor") navigate("/");
      });
  }, [navigate]);

  // Load data
  useEffect(() => {
    fetch("http://192.168.18.207:8000/api/doctor-dashboard/", {
      credentials: "include",
    })
      .then(res => res.json())
      .then(result => {
        if (Array.isArray(result)) setData(result);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const handleLogout = async () => {
    const csrfToken = getCookie("csrftoken");

    await fetch("http://192.168.18.207:8000/api/logout/", {
      method: "POST",
      credentials: "include",
      headers: {
        "X-CSRFToken": csrfToken,
      },
    });

    navigate("/");
  };

  if (loading) return <h3 style={{ padding: "20px" }}>Loading...</h3>;

  return (
    <div style={{ padding: "20px" }}>
      <h2>Doctor Dashboard</h2>
      <button onClick={handleLogout}>Logout</button>

      {data.length === 0 ? (
        <p>No assigned patients.</p>
      ) : (
        data.map(item => (
          <div key={item.id} style={{
            marginTop: "15px",
            border: "1px solid #ccc",
            padding: "10px",
            borderRadius: "5px"
          }}>
            <p><strong>Symptoms:</strong> {item.symptoms}</p>
            <p><strong>Risk:</strong> {item.predicted_risk}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default DoctorDashboard;
