import { useEffect, useState } from "react";

function DoctorDashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/doctor-dashboard/", {
      credentials: "include"
    })
      .then(res => res.json())
      .then(result => {
        if (Array.isArray(result)) {
          setData(result);
        } else {
          console.log("Not array:", result);
          setData([]);
        }
      })
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Doctor Dashboard</h2>

      {data.length === 0 ? (
        <p>No assigned patients.</p>
      ) : (
        data.map(item => (
          <div key={item.id}>
            {item.symptoms}
          </div>
        ))
      )}
    </div>
  );
}

export default DoctorDashboard;
