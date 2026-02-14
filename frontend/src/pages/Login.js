import { useState, useEffect } from "react";
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

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  // Auto redirect if already logged in
  useEffect(() => {
    fetch("http://192.168.18.207:8000/api/user-role/", {
      credentials: "include",
    })
      .then(res => {
        if (!res.ok) return null;
        return res.json();
      })
      .then(data => {
        if (!data) return;

        if (data.role === "nurse") navigate("/nurse");
        if (data.role === "doctor") navigate("/doctor");
      })
      .catch(() => {});
  }, [navigate]);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const csrfToken = getCookie("csrftoken");

      const response = await fetch("http://192.168.18.207:8000/api/login/", {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (data.error) {
        setError(data.error);
        return;
      }

      const roleResponse = await fetch("http://192.168.18.207:8000/api/user-role/", {
        credentials: "include",
      });

      const roleData = await roleResponse.json();

      if (roleData.role === "nurse") navigate("/nurse");
      else if (roleData.role === "doctor") navigate("/doctor");
      else setError("No role assigned");

    } catch {
      setError("Server error. Try again.");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>Login</h2>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />
        <br /><br />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <br /><br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
