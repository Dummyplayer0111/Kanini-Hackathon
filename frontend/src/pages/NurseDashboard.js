import { useEffect, useState } from "react";

function NurseDashboard() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");


  useEffect(() => {
    fetch("http://localhost:8000/api/nurse-dashboard/", {
      credentials: "include"
    })
          .then(res => res.json())
      .then(result => {
        if (Array.isArray(result)) {
          setData(result);
        } else {
          setError(result.error || "Not authorized");
        }
        setLoading(false);
      })
      .catch(err => {
        setError("Server error");
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <h3 style={{ padding: "20px" }}>Loading...</h3>;
  }

  if (error) {
    return <h3 style={{ padding: "20px", color: "red" }}>{error}</h3>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Nurse Dashboard</h2>

      {data.length === 0 ? (
        <p>No triage requests found.</p>
      ) : (
        data.map(item => (
          <div
            key={item.id}
            style={{
              marginBottom: "15px",
              border: "1px solid #ccc",
              padding: "10px",
              borderRadius: "5px"
            }}
          >
            <p><strong>Symptoms:</strong> {item.symptoms}</p>
            <p><strong>Blood Pressure:</strong> {item.blood_pressure}</p>
            <p><strong>Heart Rate:</strong> {item.heart_rate}</p>
            <p><strong>Temperature:</strong> {item.temperature}</p>
            <p><strong>Risk:</strong> {item.predicted_risk}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default NurseDashboard;
