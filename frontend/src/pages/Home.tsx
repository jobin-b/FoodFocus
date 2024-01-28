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
    <div className="">
      <LoginButton />
      <p className="text-2xl font-bold underline">Hello world!</p>
      <p>PLEASE PLEASE USE THE WEBSITE!!!</p>
    </div>
  );
}
