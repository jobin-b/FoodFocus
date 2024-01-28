import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { redirect } from "react-router-dom";
import Navbar from "../components/navbar"
import ProgBar from "../components/progbar";

export default function Profile(): JSX.Element {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } = useAuth0();

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  getAccessTokenSilently().then((token) => {localStorage.setItem("token", token); console.log(token);});

  if (!user) {
    redirect("/");
  }  

  return (
    <div>
      {
        isAuthenticated && user && (
          <div className="w-full h-full">
            <Navbar name={user.name ?? ""} image={user.picture ?? ""} />

            <div className="flex flex-col md:grid md:grid-cols-2 p-10">
              <div className="flex flex-col w-full">
                <h1 className="text-2xl">Today's Totals</h1>
                <ProgBar label="Calories" percent={0.5} />
                <ProgBar label="Protein" percent={0.2} />
                <ProgBar label="Carbs" percent={0.25} />
                <ProgBar label="CO2" percent={0.4} />
              </div>
              <div className="flex flex-col w-full">
                <h2>You've Eaten</h2>
              </div>
              <div className="flex flex-col">
                <button className="w-full rounded-lg bg-orange-400 hover:bg-orange-500 transition-all duration-200 text-white py-2">New Meal</button>
                <form>
                  <label>Item</label>
                  <input name="foodItem"></input>
                  <label>Calories</label>
                  <input name="calories"></input>
                  <label>CO2 Released</label>
                  <input name="co2release"></input>
                </form>
              </div>
            </div>
          </div>
        )
      }
    </div>
  );
}
