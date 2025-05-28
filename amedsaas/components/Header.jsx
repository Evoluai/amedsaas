import React from "react";

const Header = () => (
  <header style={{ padding: "1rem", background: "#007ACC", color: "#fff" }}>
    <h1>AmedSaaS</h1>
    <nav>
      <a href="/" style={{ color: "#fff", marginRight: "1rem" }}>Home</a>
      <a href="/login" style={{ color: "#fff" }}>Login</a>
    </nav>
  </header>
);

export default Header;
