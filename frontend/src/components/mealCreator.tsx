import React, { useState } from "react";
import axios from "axios";
import { format } from "date-fns";
import { useAuth0 } from "@auth0/auth0-react";

export interface MealCreationProps {
  name: string;
  calories: number;
  protein: number;
  carbs: number;
  co2: number;
}

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL ?? "";

const MealCreator: React.FC<MealCreationProps> = (props) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  return (
    <div className="flex flex-col">
      <form
        encType="multipart/form_data"
        id="image_upload_form"
        action={`http://localhost:5000/day_in`}
        method="post"
        onSubmit={async (event) => {
          event.preventDefault();
          try {
            const response = await axios.post(
              "http://localhost:5000/day_in",
              event.target,
              {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
              }
            );
            console.log("Got response: ", response);
          } catch (e) {
            console.log("Failed to upload image: ", e);
          }
        }}
      >
        <div className="flex flex-row justify-between gap-10">
          <input
            type="file"
            id="img_path"
            name="file"
            className="text-center w-full rounded-lg bg-orange-400 hover:bg-orange-500 transition-all duration-200 text-white py-2"
            onChange={async (event) => {
              setSelectedImage(event.target.files[0]);
            }}
          />
          <input type="text" name="user_id" value={user.email ?? ""} />
          <input
            type="text"
            name="day"
            value={format(new Date(), "MM-dd-yyyy")}
          />
          <button
            type="submit"
            form="image_upload_form"
            className="w-full rounded-lg bg-green-500 hover:bg-green-600 transition-all duration-200 text-white py-2"
          >
            Detect Food
          </button>
        </div>
      </form>
    </div>
  );
};

export default MealCreator;
