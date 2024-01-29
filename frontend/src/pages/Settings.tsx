import React, { FormEvent, useEffect, useState } from "react";
import LoginButton from "../components/login";
import { useAuth0 } from "@auth0/auth0-react";
import { redirect } from "react-router-dom";

export default function Settings() {
  const { user, isAuthenticated, isLoading } = useAuth0();

  const BACKEND_URL = "http://localhost:5000";

  const [settings, setSettings] = useState({
    calories: 0,
    protein: 0,
    carbohydrates: 0,
    fat: 0,
  });

  useEffect(() => {
    if (user) {
      fetch(`${BACKEND_URL}/macros/${user.email}/`)
        .then((response) => response.json())
        .then((data) => setSettings(data));
    }
  }, [user]);

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setSettings((prev) => ({ ...prev, [name]: value }));
    setSettings((prev) => ({
      ...prev,
      calories: prev.fat * 9 + prev.carbohydrates * 4 + prev.protein * 4,
    }));
  };

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (user) {
      try {
        const response = await fetch(`${BACKEND_URL}/macros/${user.email}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(settings),
        });
      } catch (error) {
        console.error("Error during update:", error);
      }
    }
  }

  return (
    <div className="w-screen h-screen p-20 bg-stone-50">
      <div className="bg-white h-full w-full flex flex-col justify-start items-center gap-20 shadow-[0_0_5px_5px] p-24 shadow-stone-100 rounded-3xl">
        <h1 className="text-xl bold">Settings</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-1/2">
          <label htmlFor="protein">Protein: {settings.protein}</label>
          <div className="slidecontainer">
            <input
              type="range"
              name="protein"
              min="0"
              max="200"
              value={settings.protein}
              onChange={onChange}
              className="slider"
            />
          </div>
          <label htmlFor="carbohydrates">
            Carbohydrates: {settings.carbohydrates}
          </label>
          <div className="slidecontainer">
            <input
              type="range"
              name="carbohydrates"
              min="0"
              max="200"
              value={settings.carbohydrates}
              onChange={onChange}
              className="slider"
            />
          </div>
          <label htmlFor="fat">Fat: {settings.fat}</label>
          <div className="slidecontainer">
            <input
              type="range"
              name="fat"
              min="0"
              max="200"
              value={settings.fat}
              onChange={onChange}
              className="slider"
            />
          </div>
          <p>Calories: {settings.calories}</p>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}
