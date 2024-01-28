import React from "react";
import LoginButton from "../components/login";
import { useAuth0 } from "@auth0/auth0-react";
import { redirect } from "react-router-dom";

export default function Home() {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isAuthenticated) {
    redirect("/profile");
    console.log("redirected");
  }
  console.log(isAuthenticated);
  return (
    <div className="w-screen h-screen p-20 bg-stone-50">
      <div className="bg-white h-full w-full flex flex-col justify-center items-center gap-20 shadow-[0_0_5px_5px] shadow-stone-100 rounded-3xl">
        <div className="flex flex-col items-center">
          <h1 className="text-6xl font-bold py-2">Food Focus</h1>
          <h2 className="text-2xl">Nutrition tracking made <span className="underline">easier</span></h2>
        </div>
        <LoginButton/>
      </div>
    </div>
  );
}
