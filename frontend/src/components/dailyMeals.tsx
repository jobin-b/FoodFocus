import React from "react";

export interface Meal {
    name: string,
    calories: number,
    protein: number,
    carbs: number,
    co2: number
}

function DailyMeals(meals: any[]){
    console.log(meals);
    return (
        // <div>
            {/* <div className="flex flex-col w-full">
                <h2>Meals You've Eaten</h2>
                {
                    
                    meals ?
                    (meals.map((meal: any) =>
                         (
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
                        )
                    )) : null
                }
            </div> */}
        //</div>
    )

}

export default DailyMeals