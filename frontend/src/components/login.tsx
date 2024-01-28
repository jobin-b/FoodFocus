import { useAuth0 } from "@auth0/auth0-react";
import React from "react";

const LoginButton = () => {
  const { loginWithRedirect } = useAuth0();

  return <button className="bg-orange-400 hover:bg-orange-500 transition-all duration-200 text-2xl text-white font-bold py-2 px-10 rounded" onClick={() => loginWithRedirect()}>Log In</button>;
};

export default LoginButton;
