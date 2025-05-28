import React from "react";
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="bg-blue-600 text-white p-4">
      <h1 className="text-xl font-bold">AmedSaaS</h1>
      <nav className="mt-2">
        <Link to="/" className="mr-4">Home</Link>
      </nav>
    </header>
  );
}