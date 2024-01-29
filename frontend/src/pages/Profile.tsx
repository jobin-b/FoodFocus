import { useAuth0 } from "@auth0/auth0-react";
import React, { useEffect, useState } from "react";
import { redirect } from "react-router-dom";
import Navbar from "../components/navbar";
import ProgBar from "../components/progbar";
import DailyTotals, { DailyTotalsProps } from "../components/dailyTotals";
import DailyMeals, { Meal } from "../components/dailyMeals";
import MealCreator, { MealCreationProps } from "../components/mealCreator";
import { format } from "date-fns";
import axios from "axios";

const BACKEND_URL = "http://localhost:5000";

export default function Profile(): JSX.Element {
  const { user, isAuthenticated, isLoading, getAccessTokenSilently } =
    useAuth0();

  function loadPage() {
    if (isAuthenticated && !isLoading && user) {
      console.log(isAuthenticated);
      try {
        axios
          .get(`${BACKEND_URL}/user/${user.email}`)
          .then(() => {
            console.log("Got user");
          })
          .catch((err) => {
            console.log("ERROR getting USER: ", err);
          });

        const today = format(new Date(), "MM-dd-yyyy");
        axios
          .get(`${BACKEND_URL}/day_from_date/${user.email}/${today}`)
          .then((response) => {
            console.log("GOT DAILY TOTALS: ", response);
          })
          .catch((err) => {
            console.log("ERR gettig DAILY TOTALS: ", err);
          });

        axios
          .get(`${BACKEND_URL}/meals/${user.email}/${today}`)
          .then((response) => {
            console.log("GOT TODAYS MEALS: ", response);
          })
          .catch((err) => {
            console.log("ERR getting TODAYS MEALS: ", err);
          });
      } catch (e) {
        console.log(e);
      }
    }
  }

  useEffect(loadPage, [isAuthenticated, isLoading]);

  if (!isAuthenticated) {
    redirect("/");
  }

  const [state, setState] = useState({
    totals: {
      calorieMax: 2000,
      calorieTotal: 1050,
      proteinMax: 50,
      proteinTotal: 20,
      carbsMax: 70,
      carbsTotal: 25,
      co2percent: 0.5,
    },
    todaysMeals: [
      {
        name: "Burger",
        calories: 750,
        protein: 10,
        carbs: 4,
        co2: 0.4,
      },
    ],
    mealCreation: {
      name: "Item",
      calories: 0,
      protein: 0,
      carbs: 0,
      co2: 0,
    },
  });

  async function getNutritionData() {}

  // getAccessTokenSilently().then((token) => {console.log(token);});

  return (
    <div>
      {isAuthenticated && user && (
        <div className="w-full h-full">
          <Navbar name={user.name ?? ""} image={user.picture ?? ""} />

          <div className="flex flex-col md:grid md:grid-cols-2 p-10 md:p-24 md:gap-24">
            <DailyTotals {...(state.totals as DailyTotalsProps)} />

            {state.todaysMeals.map((meal) => (
              <div className="flex flex-col">
                <h3 className="text-lg">{meal.name}</h3>

                <table>
                  <tr>
                    <td>Calories</td>
                    <td>{meal.calories}</td>
                  </tr>
                  <tr>
                    <td>Protein</td>
                    <td>{meal.protein}g</td>
                  </tr>
                  <tr>
                    <td>Carbs</td>
                    <td>{meal.carbs}</td>
                  </tr>
                  <tr>
                    <td>CO2</td>
                    <td>{meal.co2}</td>
                  </tr>
                </table>
              </div>
            ))}

            <MealCreator {...(state.mealCreation as MealCreationProps)} />
          </div>
        </div>
      )}
    </div>
  );
}
