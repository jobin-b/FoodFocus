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

            <div className="flex flex-col p-10">
              <h1 className="text-2xl">Today</h1>
              <ProgBar label="Calories" percent={0.5} />
              <button className="w-full rounded-lg bg-orange-400 hover:bg-orange-500 transition-all duration-200 text-white py-2">New Meal</button>
            </div>
          </div>
        )
      }
    </div>
  );
}
