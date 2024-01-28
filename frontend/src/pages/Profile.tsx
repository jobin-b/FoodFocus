import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { redirect } from "react-router-dom";

export default function Profile(): JSX.Element {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (!user) {
    redirect("/");
  }

  if (isLoading) {
    return <div>Loading ...</div>;
  }

  return (
    <div>
      {isAuthenticated && user && (
        <div>
          <img src={user.picture} alt={user.name} />
          <h2>{user.name}</h2>
          <p>{user.email}</p>
        </div>
      )}
    </div>
  );
}
